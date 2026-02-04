# 🛺 Karachi Traffic Vision - Setup Guide

This project is set up to run vehicle detection using YOLOv8.

## 🚀 Quick Start

### 1. Install Dependencies
Open a terminal in this folder and run:
```bash
pip install -r requirements.txt
```

### 2. Run the App
Start the web interface:
```bash
streamlit run app.py
```
This will open the app in your browser locally (usually at `http://localhost:8501`).

---

## 🧠 Model Information
By default, this app uses `yolov8n.pt` (Standard YOLOv8 Nano), which can detect:
- Car
- Bus
- Truck
- Motorcycle (Bike)

**Note:** It will likely detect "Rickshaws" as "Cars" or "Trucks" until you train a custom model.

---

## 🏋️ Training Custom Model
If you want to train the model specifically for Rickshaws and Suzukis:

1. **Prepare Dataset**: Organize your annotated images in a folder structure compatible with YOLOv8.
2. **Create config**: Update `data.yaml` to point to your dataset.
3. **Run Training**:
   ```bash
   python train.py
   ```
