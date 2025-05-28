from ultralytics import YOLO

if __name__ == "__main__":
    # Load YOLOv8n (nano) model for training
    model = YOLO("yolo11n.pt")  # Starts from pretrained weights

    # Train
    model.train(
        data="Dataset/data.yaml",  # path to your data.yaml
        epochs=50,
        imgsz=640,
        batch=16,
        name="yolov11n_model_name",
        device=0
    )
