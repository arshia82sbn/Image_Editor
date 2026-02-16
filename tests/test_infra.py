import pytest
import os
from PIL import Image
from image_editor.infra.image_handler import load_image, save_image, resize_to_fit

def test_resize_to_fit():
    img = Image.new("RGB", (100, 200))
    resized = resize_to_fit(img, (50, 50))
    # Should maintain aspect ratio: (100, 200) -> (25, 50)
    assert resized.size == (25, 50)

def test_save_and_load(tmp_path):
    img = Image.new("RGB", (10, 10), color="blue")
    file_path = str(tmp_path / "test.png")
    save_image(img, file_path)
    assert os.path.exists(file_path)

    loaded = load_image(file_path)
    assert loaded.size == (10, 10)
    assert loaded.getpixel((0, 0)) == (0, 0, 255)
