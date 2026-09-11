import os

# Temporary workaround for OpenMP DLL conflict on Windows
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from pathlib import Path
from ultralytics import YOLO

project_root = Path(__file__).resolve().parents[2]

model_path = (
    project_root
    / "ml"
    / "models"
    / "trained"
    / "weapon_detection"
    / "weights"
    / "best.pt"
)

video_path = (
    project_root
    / "bcc18f85ff646b7a111ba7348568749a.mp4"
)

if not model_path.exists():
    raise FileNotFoundError(
        f"Model not found: {model_path}"
    )

if not video_path.exists():
    raise FileNotFoundError(
        f"Video not found: {video_path}"
    )


model = YOLO(str(model_path))

print(f"Model: {model_path}")
print(f"Video: {video_path}")

results = model.track(
    source=str(video_path),

    conf=0.5,

    # Keep tracker IDs between frames
    persist=True,

    # ByteTrack
    tracker="bytetrack.yaml",

    # Show video
    show=True,

    # Save annotated video
    save=True,

    # Save tracking labels
    save_txt=True,
    save_conf=True,

    # CPU
    device="cpu",

    # Prevent RAM accumulation
    stream=True,

    # Output
    name="video_tracking",
    exist_ok=True,
)



for frame_number, result in enumerate(results, start=1):

    if result.boxes is not None:
        boxes = result.boxes

        print(
            f"Frame {frame_number}: "
            f"{len(boxes)} objects detected"
        )
