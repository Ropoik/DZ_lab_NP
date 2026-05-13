import numpy as np
from PIL import Image
from pathlib import Path

def stretch(img):
    in_min, in_max = img.min(), img.max()
    if in_min == in_max:
        return np.full_like(img, 128, dtype=np.uint8)
    return ((img - in_min) * (255.0 / (in_max - in_min))).astype(np.uint8)

input_folder = "lunar_images"
output_folder = Path(input_folder) / "processed"
output_folder.mkdir(exist_ok=True)

for f in Path(input_folder).glob("lunar*_raw*"):
    data = np.array(Image.open(f).convert('L'))
    stretched = stretch(data)
    out_name = output_folder / f"{f.stem.replace('_raw', '')}_stretched.png"
    Image.fromarray(stretched).save(out_name)