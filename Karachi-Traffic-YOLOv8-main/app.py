import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
import numpy as np
from PIL import Image

# Setup page config
st.set_page_config(page_title="Bangalore Traffic AI", page_icon="🛺", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* Global Settings & Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main Background - Dark Gradient */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        background-attachment: fixed;
    }

    /* Glassmorphism Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Headings */
    .main-header {
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF9933, #FFFFFF, #138808); /* Indian Flag gradient hint */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 20px;
        font-size: 3rem;
        text-shadow: 0 0 30px rgba(255, 153, 51, 0.3);
    }

    .sub-header {
        color: #94a3b8;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 400;
        font-size: 1.2rem;
    }

    /* Buttons - Glassy & Professional */
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.5);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.6);
        background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
    }

    /* Inputs & Selectboxes */
    .stSelectbox > div > div, .stSlider > div > div > div {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px;
        color: white;
    }

    /* File Uploader */
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.03);
        padding: 2rem;
        border-radius: 12px;
        border: 1px dashed rgba(255, 255, 255, 0.2);
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 4px;
        color: #cbd5e1;
        padding: 10px 20px;
        font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
        background-color: rgba(59, 130, 246, 0.1) !important;
        color: #60a5fa !important;
        border-bottom: 2px solid #3b82f6;
    }
    
    /* Metrics/Info Box */
    .stAlert {
        background-color: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.2);
        color: #e2e8f0;
    }
    
    /* Image Captions */
    [data-testid="stImageCaption"] {
        color: #94a3b8;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>🛺 Namma Bangalore Traffic Vision</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-header'>Real-time Vehicle Detection with YOLOv8</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙️ Settings")
confidence = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.25, 0.05)
model_path = st.sidebar.selectbox("Model Type", ["yolov8n.pt", "yolov8m.pt", "yolov8l.pt", "yolov8x.pt"], index=0)
st.sidebar.info("Note: Larger models (l/x) are more accurate but require more powerful hardware.")

if st.sidebar.button("Reset Model"):
    model_path = "yolov8n.pt"

# Load Model
try:
    model = YOLO(model_path)
except Exception as e:
    st.error(f"Error loading model: {e}. using 'yolov8n.pt' as fallback.")
    model = YOLO('yolov8n.pt')

# Helper for sidebar stats
def display_counts(counts_dict):
    st.markdown("### 📊 Vehicle Counts")
    
    # Calculate total
    total_count = sum(counts_dict.values())
    st.markdown(f"## **Total: {total_count}**")
    st.divider()
    
    # Display individual counts
    csv_data = "Vehicle Type,Count\n"
    for name, count in counts_dict.items():
        st.write(f"**{name}**: {count} NOS")
        csv_data += f"{name},{count}\n"
    
    # Download Button
    st.markdown("---")
    st.download_button(
        label="📥 Download Report",
        data=csv_data,
        file_name="traffic_report.csv",
        mime="text/csv"
    )


# Main Content
tab1, tab2, tab3 = st.tabs(["🖼️ Image Detection", "🎥 Video Detection", "🔴 Live Camera"])

with tab1:
    st.header("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        image = Image.open(uploaded_file)
        
        with col1:
            st.image(image, caption='Uploaded Image', use_column_width=True)
            
        with st.spinner('Detecting...'):
            results = model.predict(image, conf=confidence)
            
            # Visualize results
            res_plotted = results[0].plot()
            res_image = Image.fromarray(res_plotted[..., ::-1]) # RGB to BGR fix if needed, usually plot returns BGR
            # Actually plot() returns a numpy array in BGR (OpenCV format)
            # So we need to convert BGR to RGB for PIL/Streaamlit
            res_image = Image.fromarray(res_plotted[..., ::-1]) 

        with col2:
            st.image(res_image, caption='Detected Image', use_column_width=True)
            
        # Show detections data
        st.write("### 📊 Detection Results")
        
        # Calculate counts for this image
        counts = {}
        for box in results[0].boxes:
            cls = int(box.cls[0])
            name = model.names[cls]
            counts[name] = counts.get(name, 0) + 1
            
            # Detailed list (optional, can keep or remove)
            # conf = float(box.conf[0])
            # st.write(f"- **{name}**: {conf:.2f} confidence")

        # Use the helper to show the stats box
        with st.sidebar:
             st.empty()
             display_counts(counts)

with tab2:
    st.header("Upload a Video")
    uploaded_video = st.file_uploader("Choose a video...", type=['mp4', 'avi', 'mov'])

    if uploaded_video is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(uploaded_video.read())
        
        # Video Settings
        st.sidebar.markdown("---")
        st.sidebar.subheader("🎥 Video Settings")
        frame_skip = st.sidebar.slider("Frame Skip (Higher = Faster)", 1, 10, 3)

        if st.button("Start Video Processing"):
            vf = cv2.VideoCapture(tfile.name)
            stframe = st.empty()
            
            # Counter state
            unique_ids = set()
            class_counts = {}

            # Create placeholder for stats
            stats_placeholder = st.sidebar.empty()

            frame_count = 0
            while vf.isOpened():
                ret, frame = vf.read()
                if not ret:
                    break
                
                frame_count += 1
                if frame_count % frame_skip != 0:
                    continue
                
                # Run tracking (not just prediction)
                results = model.track(frame, conf=confidence, persist=True)
                res_plotted = results[0].plot()
                
                # Count logic
                if results[0].boxes.id is not None:
                    boxes = results[0].boxes
                    track_ids = boxes.id.int().cpu().tolist()
                    cls_ids = boxes.cls.int().cpu().tolist()
                    
                    for track_id, cls_id in zip(track_ids, cls_ids):
                        unique_ids.add(track_id)
                        name = model.names[cls_id]
                        if name not in class_counts:
                            class_counts[name] = set()
                        class_counts[name].add(track_id)

                # Display stats in sidebar (real-time)
                # Convert sets to lengths for display
                display_data = {k: len(v) for k, v in class_counts.items()}
                
                # Display frame
                stframe.image(res_plotted, channels="BGR", use_column_width=True)

                # Overlay counts on sidebar using the helper (clears previous)
                with stats_placeholder.container():
                    display_counts(display_data)
                
            vf.release()

with tab3:
    st.header("🔴 Live Camera Analysis")
    st.write("Click the checkbox to start the webcam feed.")
    st.info("Note: To stop the camera, uncheck the box.")

    run_camera = st.checkbox("Start Camera")

    if run_camera:
        cam_placeholder = st.empty()
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            st.error("Could not open webcam.")

        # Counter state
        class_counts = {}
        
        # Stats placeholder
        stats_placeholder = st.sidebar.empty()

        # Loop to capture frames
        while run_camera:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to capture image from camera.")
                break

            # Run tracking
            results = model.track(frame, conf=confidence, persist=True)
            res_plotted = results[0].plot()

            # Count logic
            if results[0].boxes.id is not None:
                boxes = results[0].boxes
                track_ids = boxes.id.int().cpu().tolist()
                cls_ids = boxes.cls.int().cpu().tolist()
                
                for track_id, cls_id in zip(track_ids, cls_ids):
                    name = model.names[cls_id]
                    if name not in class_counts:
                        class_counts[name] = set()
                    class_counts[name].add(track_id)
            
            # Display frame
            cam_placeholder.image(res_plotted, channels="BGR", use_column_width=True)

            # Sidebar live update
            display_data = {k: len(v) for k, v in class_counts.items()}
            with stats_placeholder.container():
                 display_counts(display_data)

        cap.release()
