import yaml
import os
import argparse
import torch
from ultralytics import YOLO


# Workaround for OpenMP DLL conflict on Windows
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from pathlib import Path
from ultralytics import YOLO


def main() -> None:
    """
    Main function to train a YOLO model using the Ultralytics library. 
    It loads a pretrained model, sets up training parameters, and starts the training process. 
    The function also handles file paths for the model, dataset, and output directory.
    """

    parser = argparse.ArgumentParser(description="Train a YOLO model using Ultralytics witha a custom dataset and configuration.")

    parser.add_argument("--cfg", type="str", default="configs/dataset.yml", help="Path to the dataset configuration file.")
    args = parser.parse_args()

    # load and validate the file and config path 
    cfg_path = Path(os.path.dirname(__file__), args.cfg)
    cfg_path = os.path.abspath(cfg_path)

    if not os.path.exists(cfg_path):
        raise FileNotFoundError(f"Dataset configuration file not found: {cfg_path}")

    # load the configuration yaml file safely
    with open(cfg_path, "r") as file:
        confiuration_file: dict = yaml.safe_load(file) or {}


BASE_DIR = Path(__file__).resolve().parent.parent

# MODEL_PATH = (
#     BASE_DIR
#     / "models"
#     / "pretrained"
#     / "best.pt"
# )
MODEL_PATH = (
    BASE_DIR
    / "models"
    / "trained"
    / "visdrone-5"
    / "weights"
    / "best.pt"
)

DATASET_PATH = (
    BASE_DIR
    / "configs"
    / "dataset.yml"
)

OUTPUT_DIR = (
    BASE_DIR
    / "models"
    / "trained"
)


def train():

    print("Loading pretrained model...")

    model = YOLO(str(MODEL_PATH))

    print("Starting training...")


    model.train(
    data=str(DATASET_PATH),

    epochs=10,        # ↓ biggest direct reduction
    imgsz=640,       # ↓ significantly faster than 640
    batch=16,         # ↓ memory usage; may or may not improve speed
    device="cpu",
    workers=4,       # 2–4 is usually reasonable

    project=str(OUTPUT_DIR),
    name="visdrone",
    pretrained=True,
    plots=True,
    verbose=True,
)
if __name__ == "__main__":
    train()