import cv2
import time
import glob
import os
from pathlib import Path

# =====================================
# CONFIGURATION
# =====================================

# DATASET_DIR = (
#     "recordings/recordings/session_20260604_210505"
# )

DATASET_DIR = Path(
    "recordings"
) / "session_20260610_175544"

VIEW_FPS = 35

# =====================================


def main():

    image_files = sorted(
        DATASET_DIR.glob("*.jpg")
    )

    # image_files = sorted(
    #     glob.glob(
    #         os.path.join(
    #             DATASET_DIR,
    #             "*.jpg"
    #         )
    #     )
    # )

    if len(image_files) == 0:

        print(
            "No images found"
        )

        return

    print(
        f"Loaded "
        f"{len(image_files)} images"
    )

    frame_delay = (
        1.0 / VIEW_FPS
    )

    frame_count = 0

    start_time = time.time()

    for image_path in image_files:

        loop_start = time.time()

        frame = cv2.imread(
            str(image_path)
        )

        if frame is None:

            continue

        frame_count += 1

        elapsed = (
            time.time()
            - start_time
        )

        visualization_fps = (
            frame_count /
            elapsed
        )

        cv2.putText(
            frame,
            f"View FPS: "
            f"{visualization_fps:.2f}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Frame: "
            f"{frame_count}/"
            f"{len(image_files)}",
            (10, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "Dataset Viewer",
            frame
        )

        if (
            cv2.waitKey(1)
            & 0xFF
            == ord("q")
        ):

            break

        elapsed_loop = (
            time.time()
            - loop_start
        )

        remaining = (
            frame_delay
            - elapsed_loop
        )

        if remaining > 0:

            time.sleep(
                remaining
            )

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()