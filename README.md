# 🛺 Namma Bangalore Traffic Vision (YOLOv8)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-green?style=for-the-badge&logo=python&logoColor=white)

**Namma Bangalore Traffic Vision** is an advanced AI-powered traffic monitoring system designed specifically for the chaotic and diverse traffic conditions of Indian cities like Bangalore. Unlike generic models, this project is tailored to detect local vehicles such as **Auto Rickshaws, Tempos, BMTC Buses, JCBs, and more.**

Built with **YOLOv8** for state-of-the-art detection and **Streamlit** for a premium, dark-themed user interface.

## ✨ Key Features

- **🚀 Real-time Detection**: High-speed inference using YOLOv8 (Nano to X models).
- **🔴 Live Camera & Video**: Support for webcam feeds and video file analysis.
- **🔢 Unique Vehicle Counting**: Tracks vehicles (ByteTrack) and counts unique instances to avoid double-counting.
- **📊 Auto-Generated Reports**: Export traffic data to CSV with a single click.
- **🎨 Premium UI**: Glassmorphism design with a "Dark/Midnight" aesthetic.
- **🧠 19-Class Support**: Customized to detect:
  `Rickshaw`, `Tempo`, `JCB`, `Cattle Vehicle`, `Road Roller`, `BMTC Bus`, and 13 others.

## 🛠️ Project Structure

```
Bangalore-Traffic-Vision/
├── app.py                  # The main Streamlit Application
├── train.py                # script to train custom models with Augmentation
├── import_dataset.py       # 🪄 Auto-importer for Roboflow Datasets
├── generate_dummy_data.py  # Script to test the pipeline without real data
├── data.yaml               # YOLOv8 Configuration for 19 classes
└── requirements.txt        # Dependencies
```

## 🚀 Quick Start Guide

### 1. Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/your-username/Bangalore-Traffic-Vision.git
cd Bangalore-Traffic-Vision
pip install -r requirements.txt
```

### 2. Run the App
Launch the interface immediately:
```bash
streamlit run app.py
```
*Note: Default model (`yolov8n.pt`) may identify Rickshaws as Cars. See 'Training' below.*

### 3. Training Custom Model (The Magic Step)
To make the AI smart enough to distinguish a **Rickshaw** from a **Car**, follow these simple steps:

1.  **Get Data**: Download a Rickshaw dataset from [Roboflow Universe](https://universe.roboflow.com/search?q=rickshaw).
2.  **Import**: Drop the downloaded `.zip` file into the project folder.
3.  **Run Auto-Import**:
    ```bash
    python import_dataset.py
    ```
4.  **Train**:
    ```bash
    python train.py
    ```
    *This uses advanced data augmentation (rotation, perspective, mosaic) to handle different angles automatically!*

## 🚘 Supported Classes
The system is configured to detect **19 distinct classes**:
1.  Person
2.  Motorcycle
3.  Cycle
4.  Car
5.  **Rickshaw (Auto)**
6.  Truck
7.  **JCB (Excavator)**
8.  **Cattle Vehicle**
9.  Van
10. Crane
11. **BMTC Bus**
12. Jeep
13. Aeroplane
14. Tractor
15. Helicopter
16. Jet
17. Train
18. Lorry
19. Road Roller

## 📊 Result Export
After running a session, look at the Sidebar stats.
Click **"📥 Download Report"** to get a `.csv` file with the total counts for that session.

---
**Author**: Developed for AI Traffic Solutions.
**License**: MIT

<img width="1908" height="774" alt="Screenshot 2026-02-04 230154" src="https://github.com/user-attachments/assets/24685599-068e-4790-aaf2-ab1a669cd3a7" />

<img width="1327" height="359" alt="Screenshot 2026-02-04 230130" src="https://github.com/user-attachments/assets/5f0b0ed9-c61e-4a4c-9e04-f77f9ceb7b30" />

<img width="354" height="705" alt="Screenshot 2026-02-04 230206" src="https://github.com/user-attachments/assets/993bd14d-f8eb-40a8-a676-a0fb4bfe34bb" />

