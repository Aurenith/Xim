from pathlib import Path

from ultralytics import YOLO

project_root = Path(__file__).resolve().parents[2]
model_path = project_root / "models" / "pretrained" / "yolov8n.pt"
image_dir = project_root / "ml" / "dataset" / "final" / "test" / "images"

model_path = Path("C:\\Users\\Nishidh\\Desktop\\sih-value-ideas\\Xim\\ml\\models\\trained\\visdrone-3\\weights\\best.pt")
if not model_path.exists():
    raise FileNotFoundError(f"Model not found: {model_path}")

image_candidates = sorted(image_dir.glob("*.jpg")) + sorted(image_dir.glob("*.png"))
if not image_candidates:
    raise FileNotFoundError(f"No test image found in {image_dir}")

source_image = image_candidates[0]
output_dir = project_root / "ml" / "training" / "outputs"
output_dir.mkdir(parents=True, exist_ok=True)
output_image = output_dir / f"prediction_{source_image.stem}.jpg"

model = YOLO(str("C:\\Users\\Nishidh\\Desktop\\sih-value-ideas\\Xim\\ml\\models\\trained\\visdrone-3\\weights\\best.pt"))
results = model(str("C:\\Users\\Nishidh\\Desktop\\sih-value-ideas\\Xim\\ml\\dataset\\final\\test\\images\\image.png"), conf=0.5)

# results = model.track("C:\\Users\\Nishidh\\Desktop\\sih-value-ideas\\Xim\\bcc18f85ff646b7a111ba7348568749a.mp4", conf=0.5, persist=True, show=True, save=True, save_txt=True, save_conf=True, device="cpu")

for result in results:
    annotated_image = result.plot()
    output_image.write_bytes(b"")
    result.save(filename=str(output_image))
    print(f"Saved prediction to: {output_image}")
    print(f"Using input image: {source_image}")
    print(f"Detected {len(result.boxes)} objects")
    break

