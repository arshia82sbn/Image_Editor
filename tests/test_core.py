import pytest
from PIL import Image
from unittest.mock import MagicMock
from image_editor.core.editor import ImageEditor
from image_editor.core.filters import GrayscaleFilter, BlurFilter
from image_editor.core.commands import DrawOvalCommand
from image_editor.models.pen import PenConfig
from image_editor.core.repository import ImageRepository

def test_editor_init():
    mock_repo = MagicMock(spec=ImageRepository)
    editor = ImageEditor(mock_repo)
    assert editor.state.current_image is None
    assert editor.pen.size == 5

def test_grayscale_filter():
    img = Image.new("RGB", (10, 10), color="red")
    f = GrayscaleFilter()
    filtered = f.apply(img)
    assert filtered.mode == "L"

def test_blur_filter():
    img = Image.new("RGB", (10, 10), color="red")
    f = BlurFilter()
    filtered = f.apply(img)
    assert filtered.size == (10, 10)

def test_draw_command():
    img = Image.new("RGB", (100, 100), color="white")
    pen = PenConfig(color="#000000", size=5)
    cmd = DrawOvalCommand(10, 10, 20, 20, pen)
    updated = cmd.execute(img)
    # Check if a pixel in the oval is black
    assert updated.getpixel((15, 15)) == (0, 0, 0)

def test_editor_undo():
    mock_repo = MagicMock(spec=ImageRepository)
    editor = ImageEditor(mock_repo)
    img = Image.new("RGB", (100, 100), color="white")
    editor.state.current_image = img
    editor.state.original_image = img.copy()

    pen = PenConfig(color="#000000", size=5)
    cmd = DrawOvalCommand(0, 0, 10, 10, pen)
    editor.apply_command(cmd)

    assert len(editor.state.history) == 1

    editor.undo()
    assert len(editor.state.history) == 0
    # Should be white again
    assert editor.state.current_image.getpixel((5, 5)) == (255, 255, 255)

def test_editor_open_image_calls_repository():
    mock_repo = MagicMock(spec=ImageRepository)
    img = Image.new("RGB", (100, 100))
    mock_repo.load.return_value = img
    mock_repo.resize.return_value = img

    editor = ImageEditor(mock_repo)
    editor.open_image("test.png", (50, 50))

    mock_repo.load.assert_called_once_with("test.png")
    mock_repo.resize.assert_called_once()
    assert editor.state.file_path == "test.png"

def test_editor_apply_command_no_image():
    mock_repo = MagicMock(spec=ImageRepository)
    editor = ImageEditor(mock_repo)
    with pytest.raises(ValueError, match="No image loaded"):
        editor.apply_command(MagicMock())
