import carla
import cv2
import csv
import time
import numpy as np

from pathlib import Path
from queue import Queue
import random


# ==================================================
# USER CONFIGURATION
# ==================================================

TARGET_FPS = 15

RECORD_SECONDS = 60

TARGET_FRAMES = (
    TARGET_FPS *
    RECORD_SECONDS
)

# ==================================================


def main():

    client = carla.Client(
        "localhost",
        2000
    )

    client.set_timeout(
        10.0
    )

    world = client.get_world()

    original_settings = (
        world.get_settings()
    )

    settings = world.get_settings()

    settings.synchronous_mode = True

    settings.fixed_delta_seconds = (
        1.0 / TARGET_FPS
    )

    world.apply_settings(
        settings
    )

    blueprint_library = (
        world.get_blueprint_library()
    )

    # ----------------------------------
    # Vehicle
    # ----------------------------------

    vehicle_bp = (
        blueprint_library.filter(
            "vehicle.tesla.model3"
        )[0]
    )

    vehicle = None
    
    spawn_points = (
        world.get_map()
        .get_spawn_points()
    )

    random.shuffle(
        spawn_points
    )

    for spawn_point in spawn_points:

        try:

            vehicle = world.spawn_actor(
                vehicle_bp,
                spawn_point
            )

            print(
                f"Spawn Location: "
                f"{spawn_point.location}"
            )

            break

        except RuntimeError:

            continue

    # for spawn_point in (
    #     world.get_map()
    #     .get_spawn_points()
    # ):

    #     try:

    #         vehicle = world.spawn_actor(
    #             vehicle_bp,
    #             spawn_point
    #         )

    #         break

    #     except RuntimeError:

    #         continue

    if vehicle is None:

        print(
            "No free spawn point found"
        )

        return

    vehicle.set_autopilot(
        True
    )

    print(
        f"Vehicle spawned: "
        f"{vehicle.id}"
    )

    # ----------------------------------
    # Camera
    # ----------------------------------

    camera_bp = (
        blueprint_library.find(
            "sensor.camera.rgb"
        )
    )

    camera_bp.set_attribute(
        "sensor_tick",
        "0.0"
    )

    camera_bp.set_attribute(
        "role_name",
        "rgb_front"
    )

    camera_transform = (
        carla.Transform(
            carla.Location(
                x=1.5,
                z=2.4
            )
        )
    )

    camera = world.spawn_actor(
        camera_bp,
        camera_transform,
        attach_to=vehicle
    )

    print(
        f"Camera spawned: "
        f"{camera.id}"
    )

    image_queue = Queue()

    camera.listen(
        image_queue.put
    )

    # ----------------------------------
    # Recording Directory
    # ----------------------------------

    timestamp = time.strftime(
        "%Y%m%d_%H%M%S"
    )

    session_dir = Path(
        f"recordings/session_{timestamp}"
    )

    session_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    csv_file = open(
        session_dir / "timestamps.csv",
        "w",
        newline=""
    )

    csv_writer = csv.writer(
        csv_file
    )

    csv_writer.writerow([
        "frame_id",
        "carla_frame",
        "carla_timestamp"
    ])

    # ----------------------------------
    # First Image
    # ----------------------------------

    world.tick()

    first_image = (
        image_queue.get()
    )

    print(
        "\n=== Recorder Configuration ==="
    )

    print(
        f"Target FPS      : "
        f"{TARGET_FPS}"
    )

    print(
        f"Record Seconds  : "
        f"{RECORD_SECONDS}"
    )

    print(
        f"Target Frames   : "
        f"{TARGET_FRAMES}"
    )

    print(
        f"Camera Width    : "
        f"{first_image.width}"
    )

    print(
        f"Camera Height   : "
        f"{first_image.height}"
    )

    print(
        f"\nRecording directory:\n"
        f"{session_dir}\n"
    )

    start_time = time.time()

    received_images = 0

    try:

        for frame_id in range(
            1,
            TARGET_FRAMES + 1
        ):

            if frame_id == 1:

                image = first_image

            else:

                world.tick()

                image = (
                    image_queue.get()
                )

            received_images += 1

            image_np = np.frombuffer(
                image.raw_data,
                dtype=np.uint8
            )

            image_np = image_np.reshape(
                (
                    image.height,
                    image.width,
                    4
                )
            )

            image_np = image_np[:, :, :3]

            filename = (
                session_dir /
                f"frame_{frame_id:06d}.jpg"
            )

            cv2.imwrite(
                str(filename),
                image_np,
                [
                    cv2.IMWRITE_JPEG_QUALITY,
                    90
                ]
            )

            csv_writer.writerow([
                frame_id,
                image.frame,
                image.timestamp
            ])

            if frame_id % 100 == 0:

                print(
                    f"Saved={frame_id}"
                )

    finally:

        duration = (
            time.time() -
            start_time
        )

        csv_file.close()

        # print("Recorder completed")
        # input(
        #     "Press Enter to destroy actors..."
        # )

        camera.stop()

        camera.destroy()

        
        # print("Recorder completed")
        # input(
        #     "Press Enter to destroy actors..."
        # )

        vehicle.set_autopilot(
            False
        )

        time.sleep(1)

        vehicle.destroy()

        world.apply_settings(
            original_settings
        )

        print(
            "\n===== Recording Summary ====="
        )

        print(
            f"Images Received : "
            f"{received_images}"
        )

        print(
            f"Saved Frames : "
            f"{TARGET_FRAMES}"
        )

        print(
            f"Elapsed Time : "
            f"{duration:.2f} sec"
        )

        print(
            f"Dataset Path : "
            f"{session_dir}"
        )

        print(
            "============================="
        )


if __name__ == "__main__":
    main()