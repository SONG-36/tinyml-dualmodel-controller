#!/bin/bash

# 设置构建目录
BUILD_DIR=build

# 创建构建目录
mkdir -p ${BUILD_DIR}
cd ${BUILD_DIR}

# 执行 CMake 配置，使用指定的 toolchain 文件
cmake -DCMAKE_TOOLCHAIN_FILE=../toolchain-arm-none-eabi.cmake ..

# 编译
make -j$(nproc)

# 编译完成提示
echo " 编译完成，生成文件位于 ${BUILD_DIR} 目录下。"
