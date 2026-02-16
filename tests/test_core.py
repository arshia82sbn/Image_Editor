import pytest
from PIL import Image
from image_editor.core.editor import ImageEditor
from image_editor.core.filters import GrayscaleFilter, BlurFilter
from image_editor.core.commands import DrawOvalCommand
from image_editor.models.pen import PenConfig

def test_editor_init():
    editor = ImageEditor()
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
    editor = ImageEditor()
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
