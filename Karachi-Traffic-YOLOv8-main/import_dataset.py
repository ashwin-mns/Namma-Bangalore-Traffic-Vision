import os
import zipfile
import shutil

# Configuration
PROJECT_ROOT = os.getcwd()
DATASET_DIR = os.path.join(PROJECT_ROOT, "dataset")
TEMP_EXTRACT_DIR = os.path.join(PROJECT_ROOT, "temp_extracted")

def find_zip_file():
    for file in os.listdir(PROJECT_ROOT):
        if file.endswith(".zip"):
            return os.path.join(PROJECT_ROOT, file)
    return None

def import_dataset():
    # 1. Find Zip
    zip_path = find_zip_file()
    if not zip_path:
        print("❌ No .zip file found in the project folder.")
        print("   Please download the dataset ZIP from Roboflow and drop it here.")
        return

    print(f"📦 Found archive: {os.path.basename(zip_path)}")
    
    # 2. Extract
    print("   Extracting...")
    if os.path.exists(TEMP_EXTRACT_DIR):
        shutil.rmtree(TEMP_EXTRACT_DIR)
    os.makedirs(TEMP_EXTRACT_DIR)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(TEMP_EXTRACT_DIR)

    # 3. Clean existing dummy/old data
    print("   Cleaning old/dummy data in 'dataset/'...")
    if os.path.exists(DATASET_DIR):
        shutil.rmtree(DATASET_DIR)
    os.makedirs(DATASET_DIR)

    # 4. Move Files (Smart Move)
    # Roboflow export usually has 'train', 'valid', 'test' folders at root or nested
    found_data = False
    
    for root, dirs, files in os.walk(TEMP_EXTRACT_DIR):
        # Check if this folder looks like a subset (train/valid/test)
        folder_name = os.path.basename(root).lower()
        
        target_subset = None
        if folder_name in ['train', 'training']:
            target_subset = 'train'
        elif folder_name in ['valid', 'val', 'validation']:
            target_subset = 'val'
        elif folder_name in ['test', 'testing']:
            target_subset = 'test'
            
        if target_subset:
            print(f"   PLEASE WAIT: Processing '{target_subset}' set...")
            
            # Destination paths
            dest_images = os.path.join(DATASET_DIR, target_subset, "images")
            dest_labels = os.path.join(DATASET_DIR, target_subset, "labels")
            os.makedirs(dest_images, exist_ok=True)
            os.makedirs(dest_labels, exist_ok=True)
            
            # Identify structure: is it 'train/images' & 'train/labels' OR just 'train/' with mixed files?
            # We look inside the source 'root'
            
            # Case A: Subfolders 'images' and 'labels' exist
            src_images_dir = os.path.join(root, "images")
            src_labels_dir = os.path.join(root, "labels")
            
            if os.path.exists(src_images_dir) and os.path.exists(src_labels_dir):
                # Copy content of images
                for f in os.listdir(src_images_dir):
                    shutil.move(os.path.join(src_images_dir, f), os.path.join(dest_images, f))
                # Copy content of labels
                for f in os.listdir(src_labels_dir):
                    shutil.move(os.path.join(src_labels_dir, f), os.path.join(dest_labels, f))
                found_data = True
            
            # Case B: Mixed files in the folder (less common for YOLOv8 but possible)
            else:
                for f in os.listdir(root):
                    src_file = os.path.join(root, f)
                    if os.path.isfile(src_file):
                        if f.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                            shutil.move(src_file, os.path.join(dest_images, f))
                            found_data = True
                        elif f.endswith('.txt'):
                            shutil.move(src_file, os.path.join(dest_labels, f))

    # 5. Cleanup
    shutil.rmtree(TEMP_EXTRACT_DIR)
    
    if found_data:
        print("\n✅ SUCCESS: Dataset imported!")
        print(f"   Files organized in: {DATASET_DIR}")
        print("   You can now run: python train.py")
    else:
        print("\n⚠️ WARNING: Extracted the zip but couldn't find standard 'train/valid' folders.")
        print(f"   Please check the extracted contents in {TEMP_EXTRACT_DIR}")

if __name__ == "__main__":
    import_dataset()
