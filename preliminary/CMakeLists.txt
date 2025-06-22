cmake_minimum_required(VERSION 3.20)
project(TinyML_FREERTOS_H750 C ASM)

# 平台设置
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR cortex-m7)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)

# 工具链
set(TOOLCHAIN_PATH /opt/gcc-arm-none-eabi-13.2/bin)
set(CMAKE_C_COMPILER ${TOOLCHAIN_PATH}/arm-none-eabi-gcc)
set(CMAKE_ASM_COMPILER ${TOOLCHAIN_PATH}/arm-none-eabi-gcc)

# 编译器参数
set(CPU_FLAGS "-mcpu=cortex-m7 -mthumb -mfloat-abi=hard -mfpu=fpv5-d16")
set(COMMON_FLAGS "-Wall -O2 -ffunction-sections -fdata-sections")
set(CMAKE_C_FLAGS "${CPU_FLAGS} ${COMMON_FLAGS}")
set(CMAKE_ASM_FLAGS "${CPU_FLAGS} ${COMMON_FLAGS}")
set(CMAKE_EXE_LINKER_FLAGS "${CPU_FLAGS} -T${CMAKE_SOURCE_DIR}/STM32H750XBHX_FLASH.ld -Wl,--gc-sections")

# 宏定义
add_definitions(-DUSE_HAL_DRIVER -DSTM32H750xx -DARM_MATH_CM7 -D__START=_start)

# Include 目录（包含 CMSIS-DSP）
include_directories(
  Core/Inc
  Drivers/CMSIS/Include
  Drivers/CMSIS/Core/Include
  Drivers/CMSIS/Device/ST/STM32H7xx/Include
  Drivers/STM32H7xx_HAL_Driver/Inc
  Middlewares/Third_Party/FreeRTOS/Source/include
  Middlewares/Third_Party/FreeRTOS/Source/CMSIS_RTOS
  Middlewares/Third_Party/FreeRTOS/Source/portable/GCC/ARM_CM7
  Drivers/CMSIS/DSP/Include
  Drivers/CMSIS/DSP/Include/dsp
)

# 源文件
file(GLOB CORE_SRCS    Core/Src/*.c)
file(GLOB STARTUP_SRCS Core/Startup/*.s)
file(GLOB HAL_SRCS     Drivers/STM32H7xx_HAL_Driver/Src/*.c)

file(GLOB FREERTOS_SRCS
  Middlewares/Third_Party/FreeRTOS/Source/*.c
  Middlewares/Third_Party/FreeRTOS/Source/portable/GCC/ARM_CM7/port.c
  Middlewares/Third_Party/FreeRTOS/Source/portable/MemMang/heap_4.c
)

# 移除 HAL 模板文件
list(REMOVE_ITEM HAL_SRCS
  ${CMAKE_SOURCE_DIR}/Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_hal_msp_template.c
  ${CMAKE_SOURCE_DIR}/Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_hal_timebase_rtc_alarm_template.c
)

# CMSIS-DSP 源码（你可以根据使用的函数再删减）
set(DSP_SRCS
  Drivers/CMSIS/DSP/Source/TransformFunctions/arm_cfft_q15.c
  Drivers/CMSIS/DSP/Source/TransformFunctions/arm_cfft_radix4_q15.c
  Drivers/CMSIS/DSP/Source/BasicMathFunctions/arm_mult_q15.c
  Drivers/CMSIS/DSP/Source/BasicMathFunctions/arm_abs_q15.c
)

# 添加目标
add_executable(${PROJECT_NAME}
  ${CORE_SRCS}
  ${STARTUP_SRCS}
  ${HAL_SRCS}
  ${FREERTOS_SRCS}
  ${DSP_SRCS}
)

# 设置输出为 .elf
set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".elf")

# 添加 bin/hex 文件导出
add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
  COMMAND ${TOOLCHAIN_PATH}/arm-none-eabi-objcopy -O binary ${PROJECT_NAME}.elf ${PROJECT_NAME}.bin
  COMMAND ${TOOLCHAIN_PATH}/arm-none-eabi-objcopy -O ihex   ${PROJECT_NAME}.elf ${PROJECT_NAME}.hex
)
