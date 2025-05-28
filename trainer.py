from ultralytics import YOLO

if __name__ == "__main__":
    # Load YOLOv8n (nano) model for training
    model = YOLO("yolo11n.pt")  # Starts from pretrained weights

    # Train
    model.train(
        data="Dataset/data.yaml", 
        epochs=50,
        imgsz=320,
        batch=16,
        name="yolov11n_easeup",
        device=0,            
        mosaic=0, 
    )
