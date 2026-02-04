from ultralytics import YOLO

def train_custom_model():
    # Load a model
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # Train the model
    # Note: You need a 'data.yaml' file that points to your dataset.
    # The data.yaml should look like this:
    # train: ./dataset/train/images
    # val: ./dataset/valid/images
    # nc: 8
    # names: ['Rickshaw', 'Suzuki', 'Cart', 'Car', 'Bus', 'Truck', 'Bike', 'Van']
    
    print("Starting training with advanced augmentation...")
    # Training with data augmentation to handle different angles/lighting
    results = model.train(
        data="data.yaml",
        epochs=100,
        imgsz=640,
        device='0' if 0 else 'cpu', # Let YOLO auto-detect or force CPU if needed. Better: device=0 (gpu) or 'cpu'
        degrees=15.0,      # Rotate images +/- 15 degrees (simulates angles)
        scale=0.5,         # Scale images +/- 50%
        shear=2.5,         # Shear angle
        perspective=0.001, # Perspective distortion (simulates 3D view)
        flipud=0.0,        # No upside down flip
        fliplr=0.5,        # Flip left-right (mirroring)
        mosaic=1.0,        # Mosaic augmentation (mixes 4 images)
        mixup=0.1          # Mixup augmentation
    )
    
    # Evaluate performance
    metrics = model.val()
    print(metrics.box.map)
    
    # Export the model
    success = model.export(format="onnx")
    print("Model exported successfully.")

if __name__ == '__main__':
    # dataset is ready (dummy or real), starting training
    train_custom_model()
    # print("Please configure 'data.yaml' and your dataset folder before running training.")
    # print("Check the code comments for instructions.")
