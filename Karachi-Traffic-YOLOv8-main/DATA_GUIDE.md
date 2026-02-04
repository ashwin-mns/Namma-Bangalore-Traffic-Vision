# 📊 Dataset & Training Guide

## 🎯 Target Classes (19 Types)
The model is now configured to detect exactly these 19 classes:
1. Person
2. Motorcycle
3. Cycle
4. Car
5. Rickshaw
6. Truck
7. JCB (Excavator)
8. Cattle Vehicle
9. Van
10. Crane
11. Bus
12. Jeep
13. Aeroplane
14. Tractor
15. Helicopter
16. Jet
17. Train
18. Lorry
19. Road Roller

## 🖼️ Achieving "Different Angles"
To get precise detection from all angles without needing millions of photos, I have enabled **advanced augmentation** in `train.py`.
- **Rotation**: +/- 15 degrees
- **Perspective**: Simulates 3D tilting
- **Mosaic**: Mixes images to handle crowding
- **Flipping**: Mirroring images

**You just need to provide standard images; the script will generate the angles for you!**

## 📥 Where to get Data (Datasets)
For common vehicles (Car, Bus, Bike), use standard datasets (COCO, OpenImages).
For **RARE** vehicles, use these links:

- **JCB / Excavators**:
  - [Kaggle Excavator Dataset](https://www.kaggle.com/datasets?search=excavator)
  - [Roboflow Construction Vehicles](https://universe.roboflow.com/search?q=excavator)

- **Road Rollers / Cranes**:
  - [Construction Equipment on Roboflow](https://universe.roboflow.com/search?q=road+roller)

- **Cattle Truck**:
  - Search for "Livestock transport truck" on Google Images or Roboflow.
  - *Tip*: You may need to label these manually using [Roboflow Labeling Tool](https://roboflow.com/annotate).

## 🚀 How to Train
1. Download images for each class.
2. Organize them in `dataset/train/images`.
3. Run:
   ```bash
   python train.py
   ```
