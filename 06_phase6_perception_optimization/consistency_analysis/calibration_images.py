import random
import shutil
from pathlib import Path

src = Path("/home/hamza/ros2_cv_ws/scripts/phase4/recordings/session_20260605_181953_A_640x480")
dst = Path("/home/hamza/ros2_cv_ws/scripts/phase6/calibration_images")

dst.mkdir(exist_ok=True)

images = list(src.glob("*.jpg"))

for img in random.sample(images, 500):
    shutil.copy(img, dst / img.name)