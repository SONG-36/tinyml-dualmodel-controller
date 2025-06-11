# TinyML Dual-Model Controller

An offline embedded AI control system based on STM32H750, integrating dual machine learning models: **voice keyword recognition** and **face detection**, powered by **TensorFlow Lite Micro** and managed with **FreeRTOS**.

本项目是一个基于 STM32H750 的离线嵌入式 AI 系统，集成了语音关键词识别与人脸检测两种模型，适用于物联网、车载、门禁等边缘设备场景，具备低功耗、低延迟、强通用性特点。

---

##  Features

- Voice keyword spotting (using MFCC + CNN, GSC dataset)
- Face detection (Tiny BlazeFace or custom CNN)
- Model inference with TFLite Micro (int8 quantized)
- Multi-task management via FreeRTOS
- Abstracted task registration structure (OOP-style in C)
- ⏱Inference latency < 60ms, RAM usage < 300KB

---

## Project Structure