# 🛺 Namma Bangalore Traffic Vision - YOLOv8

**Namma Bangalore Traffic Vision** is an AI-powered application designed to detect and classify vehicles in real-time on the busy streets of Bengaluru. It is optimized to recognize local vehicles like **Autos, Tempos, and BMTC Buses**.

Built with [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) and [Streamlit](https://streamlit.io/), this project provides a user-friendly web interface for performing object detection on both images and videos.

## ✨ Features

- **🚀 Real-time Object Detection**: Powered by the state-of-the-art YOLOv8 model.
- **🖼️ Image Analysis**: Upload any traffic image to instantly detect and visualize vehicles.
- **🎥 Video Processing**: Support for video file uploads with frame-by-frame detection.
- **🔴 Live Camera**: Real-time detection using your webcam.
- **🎛️ Interactive Controls**:
  - Adjust **Confidence Threshold** dynamically.
  - specific frame skipping for smoother video playback.
  - Switch between model versions (Nano vs. Medium).
- **📊 Detailed Insights**: View confidence scores and class names for every detection.

## 🛠️ Tech Stack

- **Python**: Core programming language.
- **YOLOv8 (Ultralytics)**: Object detection model.
- **Streamlit**: Web application framework.
- **OpenCV**: Image and video processing.
- **Pillow**: Image manipulation.

## 📦 Installation Requirement

Ensure you have Python 3.8+ installed.

1. **Clone the Repository** (if applicable) or navigate to the project folder:
   ```bash
   cd Karachi-Traffic-YOLOv8-main
   ```

2. **Install Dependencies**:
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

## 🚦 Usage Guide

### 1. Running the Web Application
To verify detection and interact with the UI:
```bash
streamlit run app.py
```
This will automatically open the app in your default web browser (usually at `http://localhost:8501`).

### 2. Using the App
- **Image Tab**: Click "Browse files" to upload a traffic image (`.jpg`, `.png`). The model will process it and show the results side-by-side.
- **Video Tab**: Upload a video file (`.mp4`, `.avi`). Click "Start Video Processing" to see the detections in action. Use the slider to speed up processing by skipping frames.
- **Live Camera Tab**: Enable the camera checkbox to start real-time detection via webcam.

## 🧠 Training a Custom Model (Rickshaws/Suzukis)

The default `yolov8n.pt` model detects common vehicles (cars, trucks, buses, bikes). To detect local vehicles like **Rickshaws** or **Suzukis**, you need to train a custom model.

1. **Prepare Dataset**: Organize your images and labels in YOLO format.
2. **Configure Data**: Create a `data.yaml` file pointing to your dataset paths.
   ```yaml
   train: ./dataset/train/images
   val: ./dataset/valid/images
   nc: number_of_classes
   names: ['Rickshaw', 'Suzuki', ...]
   ```
3. **Run Training**:
   Edit `train.py` to uncomment the training function, then run:
   ```bash
   python train.py
   ```
   *Note: This requires a GPU for reasonable training times.*

## 📂 Project Structure

```
Karachi-Traffic-YOLOv8-main/
├── app.py                # Main Streamlit application
├── train.py              # Script for training custom YOLOv8 models
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── README_SETUP.md       # Setup specific instructions
└── yolov8n.pt            # Pre-trained YOLOv8 Nano model (downloaded on first run)
```

## 🤝 Contributing
Feel free to open issues or submit pull requests if you have improved models or new features!

---
*Developed for AI traffic analysis.*
