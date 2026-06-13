import cv2
import glob
import os
from pathlib import Path


# =====================================
# CONFIGURATION
# =====================================

TARGET_WIDTH = 640

TARGET_HEIGHT = 480

# INPUT_DIR = (
#     "recordings/session_20260604_210505"
# )

dir_name = "session_20260610_175544"

INPUT_DIR = Path(
    "recordings"
) / dir_name

OUTPUT_DIR = (
    "recordings/"+dir_name+"_"+str(TARGET_WIDTH)+"x"+str(TARGET_HEIGHT)
)



# =====================================


def main():

    image_files = sorted(
        INPUT_DIR.glob("*.jpg")
    )
    # image_files = sorted(
    #     glob.glob(
    #         os.path.join(
    #             INPUT_DIR,
    #             "*.jpg"
    #         )
    #     )
    # )

    if len(image_files) == 0:

        print(
            "No images found"
        )

        return

    Path(
        OUTPUT_DIR
    ).mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        f"Found "
        f"{len(image_files)} images"
    )

    print(
        f"Resizing to "
        f"{TARGET_WIDTH}x{TARGET_HEIGHT}"
    )

    for index, image_path in enumerate(
        image_files,
        start=1
    ):

        image = cv2.imread(
            str(image_path)
        )

        if image is None:

            print(
                f"Failed: {image_path}"
            )

            continue

        resized = cv2.resize(
            image,
            (
                TARGET_WIDTH,
                TARGET_HEIGHT
            ),
            interpolation=cv2.INTER_AREA
        )

        filename = os.path.basename(
            image_path
        )

        output_path = os.path.join(
            OUTPUT_DIR,
            filename
        )

        cv2.imwrite(
            output_path,
            resized
        )

        if index % 100 == 0:

            print(
                f"Processed={index}"
            )

    print(
        "\nResize completed."
    )

    print(
        f"Output: {OUTPUT_DIR}"
    )


if __name__ == "__main__":
    main()