from ultralytics import YOLO
import cv2

# Load the standard model (since custom isn't trained yet)
model = YOLO("yolov8n.pt")

# Path to the uploaded image (Rickshaw)
img_path = r"C:\Users\ashwi\.gemini\antigravity\brain\7b2f034a-5dd5-4d7e-86a6-55b8c5a701d4\uploaded_media_1770225824379.png"

# Run inference
results = model.predict(img_path)

# Count the classes
counts = {}
for box in results[0].boxes:
    cls_id = int(box.cls[0])
    name = model.names[cls_id]
    counts[name] = counts.get(name, 0) + 1

# Display Output
print("\n" + "="*30)
print(" DETECTION OUTPUT")
print("="*30)
print(f"Image: {img_path}")
print("-" * 20)
total = sum(counts.values())
print(f"Total Vehicles: {total}")
print("-" * 20)
for name, count in counts.items():
    print(f"{name} : {count} NOS")
print("="*30 + "\n")
