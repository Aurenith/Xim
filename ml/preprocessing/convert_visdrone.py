from pathlib import Path
import shutil


# ---------------------------------------------------------
# Path
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

SOURCE_DIR = (
    BASE_DIR
    / "dataset"
    / "train"
    / "VisDrone2019-DET-train"
)

IMAGE_DIR = SOURCE_DIR / "images"
ANNOTATION_DIR = SOURCE_DIR / "annotations"

OUTPUT_DIR = BASE_DIR / "dataset" / "converted"

OUTPUT_IMAGE_DIR = OUTPUT_DIR / "images"
OUTPUT_LABEL_DIR = OUTPUT_DIR / "labels"


# ---------------------------------------------------------
# VisDrone classes
# ---------------------------------------------------------

CLASS_NAMES = {
    1: "pedestrian",
    2: "people",
    3: "bicycle",
    4: "car",
    5: "van",
    6: "truck",
    7: "tricycle",
    8: "awning-tricycle",
    9: "bus",
    10: "motor",
    11: "others",
}


def convert_bbox(
    x,
    y,
    width,
    height,
    image_width,
    image_height
):
    """
    Convert VisDrone bounding box to YOLO format.
    """

    center_x = x + width / 2
    center_y = y + height / 2

    center_x /= image_width
    center_y /= image_height

    width /= image_width
    height /= image_height

    return center_x, center_y, width, height


def convert_dataset():

    OUTPUT_IMAGE_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT_LABEL_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    image_files = list(IMAGE_DIR.glob("*.jpg"))

    print(f"Found {len(image_files)} images")

    converted = 0

    for image_path in image_files:

        annotation_path = (
            ANNOTATION_DIR
            / f"{image_path.stem}.txt"
        )

        if not annotation_path.exists():

            print(
                f"Missing annotation: "
                f"{image_path.name}"
            )

            continue

        # Get image dimensions
        from PIL import Image

        with Image.open(image_path) as image:
            image_width, image_height = image.size

        yolo_labels = []

        with open(
            annotation_path,
            "r"
        ) as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                values = line.split(",")

                if len(values) < 8:
                    continue

                (
                    x,
                    y,
                    width,
                    height,
                    score,
                    class_id,
                    truncation,
                    occlusion
                ) = map(int, values[:8])

                # Ignore invalid objects
                if width <= 0 or height <= 0:
                    continue

                # Ignore ignored regions
                if class_id == 0:
                    continue

                # Ignore "others"
                if class_id == 11:
                    continue

                # Convert VisDrone class IDs
                # to zero-based YOLO IDs
                yolo_class_id = class_id - 1

                (
                    cx,
                    cy,
                    w,
                    h
                ) = convert_bbox(
                    x,
                    y,
                    width,
                    height,
                    image_width,
                    image_height
                )

                yolo_labels.append(
                    f"{yolo_class_id} "
                    f"{cx:.6f} "
                    f"{cy:.6f} "
                    f"{w:.6f} "
                    f"{h:.6f}"
                )

        # Copy image
        output_image = (
            OUTPUT_IMAGE_DIR
            / image_path.name
        )

        shutil.copy2(
            image_path,
            output_image
        )

        # Write YOLO label
        output_label = (
            OUTPUT_LABEL_DIR
            / f"{image_path.stem}.txt"
        )

        with open(
            output_label,
            "w"
        ) as file:

            file.write(
                "\n".join(yolo_labels)
            )

        converted += 1

    print(
        f"\nSuccessfully converted "
        f"{converted} images."
    )

    print(
        f"Output: {OUTPUT_DIR}"
    )


if __name__ == "__main__":
    convert_dataset()