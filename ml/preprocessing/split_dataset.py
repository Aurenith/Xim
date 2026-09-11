from pathlib import Path
import random
import shutil


BASE_DIR = Path(__file__).resolve().parent.parent

SOURCE_DIR = BASE_DIR / "dataset" / "converted"

IMAGE_DIR = SOURCE_DIR / "images"
LABEL_DIR = SOURCE_DIR / "labels"

OUTPUT_DIR = BASE_DIR / "dataset" / "final"


TRAIN_RATIO = 0.80
VAL_RATIO = 0.10
TEST_RATIO = 0.10

RANDOM_SEED = 42


def split_dataset():

    random.seed(RANDOM_SEED)

    images = list(
        IMAGE_DIR.glob("*.jpeg")
    )

    random.shuffle(images)

    total = len(images)

    train_end = int(
        total * TRAIN_RATIO
    )

    val_end = int(
        total * (TRAIN_RATIO + VAL_RATIO)
    )

    train_images = images[:train_end]

    val_images = images[
        train_end:val_end
    ]

    test_images = images[
        val_end:
    ]

    print(f"Total: {total}")
    print(f"Train: {len(train_images)}")
    print(f"Val: {len(val_images)}")
    print(f"Test: {len(test_images)}")

    copy_files(
        train_images,
        "train"
    )

    copy_files(
        val_images,
        "val"
    )

    copy_files(
        test_images,
        "test"
    )


def copy_files(images, split):

    image_output = (
        OUTPUT_DIR
        / split
        / "images"
    )

    label_output = (
        OUTPUT_DIR
        / split
        / "labels"
    )

    image_output.mkdir(
        parents=True,
        exist_ok=True
    )

    label_output.mkdir(
        parents=True,
        exist_ok=True
    )

    for image in images:

        label = (
            LABEL_DIR
            / f"{image.stem}.txt"
        )

        shutil.copy2(
            image,
            image_output / image.name
        )

        if label.exists():

            shutil.copy2(
                label,
                label_output / label.name
            )


if __name__ == "__main__":
    split_dataset()