import cv2
import numpy as np

from pathlib import Path
from ultralytics import YOLO

# ==================================================
# CONFIG
# ==================================================

IMAGE_DIR = (
    "/home/hamza/ros2_cv_ws/scripts/phase4/recordings/session_20260605_181953_A_640x480/"
)

FP32_MODEL = (
    "/home/hamza/ros2_cv_ws/scripts/phase6/test/yolov8m-seg.pt"
)

TRT_FP16_MODEL = (
    "/home/hamza/ros2_cv_ws/scripts/phase6/engines/yolov8m-seg-trt-fp16.engine"
)

TRT_INT8_MODEL = (
    "/home/hamza/ros2_cv_ws/scripts/phase6/engines/yolov8m-seg-trt-int8.engine"
)

IOU_THRESHOLD = 0.50

# ==================================================


def box_iou(box1, box2):

    xA = max(box1[0], box2[0])
    yA = max(box1[1], box2[1])

    xB = min(box1[2], box2[2])
    yB = min(box1[3], box2[3])

    inter_w = max(0, xB - xA)
    inter_h = max(0, yB - yA)

    inter_area = inter_w * inter_h

    area1 = (
        (box1[2] - box1[0])
        * (box1[3] - box1[1])
    )

    area2 = (
        (box2[2] - box2[0])
        * (box2[3] - box2[1])
    )

    union = area1 + area2 - inter_area

    if union <= 0:
        return 0.0

    return inter_area / union


def extract_detections(results):

    detections = []

    boxes = results[0].boxes

    if boxes is None:
        return detections

    xyxy = boxes.xyxy.cpu().numpy()
    cls = boxes.cls.cpu().numpy()

    for box, cls_id in zip(
        xyxy,
        cls
    ):
        detections.append({
            "box": box,
            "class": int(cls_id)
        })

    return detections


def create_stats():

    return {
        "total_fp32": 0,
        "matched": 0,
        "class_matches": 0,
        "missed": 0,
        "added": 0,
        "ious": []
    }


def compare_models(
    fp32_dets,
    test_dets
):

    matched = 0

    class_matches = 0

    used_test = set()

    ious = []

    for fp_det in fp32_dets:

        best_iou = 0.0
        best_idx = -1

        for idx, test_det in enumerate(test_dets):

            if idx in used_test:
                continue

            iou = box_iou(
                fp_det["box"],
                test_det["box"]
            )

            if iou > best_iou:
                best_iou = iou
                best_idx = idx

        if (
            best_idx >= 0
            and best_iou >= IOU_THRESHOLD
        ):

            used_test.add(best_idx)

            matched += 1

            ious.append(best_iou)

            if (
                fp_det["class"]
                ==
                test_dets[best_idx]["class"]
            ):
                class_matches += 1

    total_fp32 = len(fp32_dets)

    missed = total_fp32 - matched

    added = len(test_dets) - matched

    return {
        "total_fp32": total_fp32,
        "matched": matched,
        "class_matches": class_matches,
        "missed": missed,
        "added": max(0, added),
        "ious": ious
    }


def update_stats(
    stats,
    result
):

    stats["total_fp32"] += result["total_fp32"]

    stats["matched"] += result["matched"]

    stats["class_matches"] += result["class_matches"]

    stats["missed"] += result["missed"]

    stats["added"] += result["added"]

    stats["ious"].extend(
        result["ious"]
    )


def print_report(
    title,
    stats
):

    total_fp32 = stats["total_fp32"]

    matched = stats["matched"]

    class_matches = stats["class_matches"]

    detection_agreement = (
        matched / total_fp32 * 100
        if total_fp32 > 0
        else 0
    )

    class_agreement = (
        class_matches / matched * 100
        if matched > 0
        else 0
    )

    mean_iou = (
        np.mean(stats["ious"])
        if len(stats["ious"]) > 0
        else 0
    )

    missed_rate = (
        stats["missed"]
        / total_fp32
        * 100
        if total_fp32 > 0
        else 0
    )

    added_rate = (
        stats["added"]
        / total_fp32
        * 100
        if total_fp32 > 0
        else 0
    )

    print()
    print("=" * 60)
    print(title)
    print("=" * 60)

    print(
        f"Total FP32 Objects  : {total_fp32}"
    )

    print(
        f"Matched Objects     : {matched}"
    )

    print(
        f"Detection Agreement : "
        f"{detection_agreement:.2f}%"
    )

    print(
        f"Class Agreement     : "
        f"{class_agreement:.2f}%"
    )

    print(
        f"Mean Box IoU        : "
        f"{mean_iou:.4f}"
    )

    print(
        f"Missed Objects      : "
        f"{stats['missed']}"
    )

    print(
        f"Missed Rate         : "
        f"{missed_rate:.2f}%"
    )

    print(
        f"Added Objects       : "
        f"{stats['added']}"
    )

    print(
        f"Added Rate          : "
        f"{added_rate:.2f}%"
    )


def main():

    print("Loading models...")

    fp32_model = YOLO(
        FP32_MODEL
    )

    fp16_model = YOLO(
        TRT_FP16_MODEL
    )

    int8_model = YOLO(
        TRT_INT8_MODEL
    )

    images = sorted(
        Path(IMAGE_DIR).glob("*.jpg")
    )

    print(
        f"Found {len(images)} images"
    )

    fp16_stats = create_stats()

    int8_stats = create_stats()

    for idx, image_path in enumerate(images):

        print(
            f"[{idx+1}/{len(images)}] "
            f"{image_path.name}"
        )

        image = cv2.imread(
            str(image_path)
        )

        fp32_results = fp32_model(
            image,
            imgsz=640,
            verbose=False
        )

        fp16_results = fp16_model(
            image,
            imgsz=640,
            verbose=False
        )

        int8_results = int8_model(
            image,
            imgsz=640,
            verbose=False
        )

        fp32_dets = extract_detections(
            fp32_results
        )

        fp16_dets = extract_detections(
            fp16_results
        )

        int8_dets = extract_detections(
            int8_results
        )

        fp16_result = compare_models(
            fp32_dets,
            fp16_dets
        )

        int8_result = compare_models(
            fp32_dets,
            int8_dets
        )

        update_stats(
            fp16_stats,
            fp16_result
        )

        update_stats(
            int8_stats,
            int8_result
        )

    print_report(
        "FP32 vs TRT FP16",
        fp16_stats
    )

    print_report(
        "FP32 vs TRT INT8",
        int8_stats
    )


if __name__ == "__main__":
    main()