import pytest
import os
from PIL import Image
from image_editor.infra.repository import FileSystemImageRepository

def test_repository_resize():
    repo = FileSystemImageRepository()
    img = Image.new("RGB", (100, 200))
    resized = repo.resize(img, (50, 50))
    # Should maintain aspect ratio: (100, 200) -> (25, 50)
    assert resized.size == (25, 50)

def test_repository_save_and_load(tmp_path):
    repo = FileSystemImageRepository()
    img = Image.new("RGB", (10, 10), color="blue")
    file_path = str(tmp_path / "test.png")
    repo.save(img, file_path)
    assert os.path.exists(file_path)

    loaded = repo.load(file_path)
    assert loaded.size == (10, 10)
    # Check blue color (0, 0, 255)
    assert loaded.getpixel((0, 0)) == (0, 0, 255)

def test_repository_load_missing_file():
    repo = FileSystemImageRepository()
    with pytest.raises(FileNotFoundError):
        repo.load("non_existent_file.png")
