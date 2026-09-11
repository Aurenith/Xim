from pathlib import Path
import shutil


BASE_DIR = Path(__file__).resolve().parent.parent
VISDRONE_DIR = BASE_DIR / "dataset" / "final"
WEAPON_DIR = BASE_DIR / "dataset" / "final" / "weapon_detection"
OUTPUT_DIR = BASE_DIR / "dataset" / "combined"


VISDRONE_SPLITS = ("train", "val", "test")
WEAPON_SPLITS = ("train", "val")


def copy_split(source_dir: Path, output_dir: Path, remap_to_weapon: bool = False) -> int:
    image_output = output_dir / "images"
    label_output = output_dir / "labels"
    image_output.mkdir(parents=True, exist_ok=True)
    label_output.mkdir(parents=True, exist_ok=True)

    copied = 0
    for image in source_dir.joinpath("images").iterdir():
        if not image.is_file():
            continue

        label = source_dir / "labels" / f"{image.stem}.txt"
        if not label.exists():
            continue

        shutil.copy2(image, image_output / image.name)
        if remap_to_weapon:
            lines = []
            for line in label.read_text().splitlines():
                parts = line.split()
                if len(parts) == 5:
                    parts[0] = "10"
                    lines.append(" ".join(parts))
            (label_output / label.name).write_text("\n".join(lines) + "\n")
        else:
            shutil.copy2(label, label_output / label.name)
        copied += 1

    return copied


def merge_datasets() -> None:
    for split in VISDRONE_SPLITS:
        copy_split(VISDRONE_DIR / split, OUTPUT_DIR / split)

    for split in WEAPON_SPLITS:
        copy_split(WEAPON_DIR / split, OUTPUT_DIR / split, remap_to_weapon=True)


if __name__ == "__main__":
    merge_datasets()
    print(f"Combined dataset written to: {OUTPUT_DIR}")
