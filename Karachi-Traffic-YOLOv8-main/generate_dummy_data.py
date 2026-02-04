import os
import cv2
import numpy as np

# Define paths
base_dir = "dataset"
train_img_dir = os.path.join(base_dir, "train", "images")
train_lbl_dir = os.path.join(base_dir, "train", "labels")
val_img_dir = os.path.join(base_dir, "val", "images")
val_lbl_dir = os.path.join(base_dir, "val", "labels")

# Create directories
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(train_lbl_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(val_lbl_dir, exist_ok=True)

def create_dummy_sample(img_path, lbl_path, cls_id):
    # Create a blank black image
    img = np.zeros((640, 640, 3), dtype=np.uint8)
    
    # Draw a colored rectangle (fake vehicle)
    # Different colors for different classes to simulate variety
    color = tuple(np.random.randint(0, 255, 3).tolist())
    cv2.rectangle(img, (100, 100), (400, 400), color, -1)
    
    # Save image
    cv2.imwrite(img_path, img)
    
    # Save label (class x_center y_center width height)
    # 0.5 0.5 0.5 0.5 represents the center box we drew
    with open(lbl_path, "w") as f:
        f.write(f"{cls_id} 0.5 0.5 0.46 0.46\n")

print("Generating dummy dataset for testing...")

# Generate 10 training samples for 'Rickshaw' (Class ID 4 from our list)
# And 10 for 'Car' (Class ID 3)
for i in range(10):
    create_dummy_sample(os.path.join(train_img_dir, f"rickshaw_{i}.jpg"), os.path.join(train_lbl_dir, f"rickshaw_{i}.txt"), 4)
    create_dummy_sample(os.path.join(train_img_dir, f"car_{i}.jpg"), os.path.join(train_lbl_dir, f"car_{i}.txt"), 3)

# Generate 2 validation samples
for i in range(2):
    create_dummy_sample(os.path.join(val_img_dir, f"rickshaw_val_{i}.jpg"), os.path.join(val_lbl_dir, f"rickshaw_val_{i}.txt"), 4)
    create_dummy_sample(os.path.join(val_img_dir, f"car_val_{i}.jpg"), os.path.join(val_lbl_dir, f"car_val_{i}.txt"), 3)

print("Dummy dataset created at ./dataset")
print("You can now run 'python train.py' to verify the pipeline works!")
print("NOTE: This is FAKE data. The model will define black boxes as Rickshaws.")
print("To get real results, delete these files and replace them with REAL images.")
