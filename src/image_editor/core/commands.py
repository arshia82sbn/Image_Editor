from abc import ABC, abstractmethod

from PIL import Image, ImageDraw

from image_editor.core.filters import FilterStrategy
from image_editor.models.pen import PenConfig


class Command(ABC):
    """Abstract base class for editor commands."""

    @abstractmethod
    def execute(self, image: Image.Image) -> Image.Image:
        """Executes the command on the given image.

        Args:
            image (Image.Image): The image to modify.

        Returns:
            Image.Image: The modified image.
        """
        pass

class DrawOvalCommand(Command):
    """Command to draw an oval (used for freehand)."""

    def __init__(self, x1: int, y1: int, x2: int, y2: int, pen: PenConfig):
        self.coords = (x1, y1, x2, y2)
        self.pen = pen

    def execute(self, image: Image.Image) -> Image.Image:
        """Draws an ellipse on the image."""
        draw = ImageDraw.Draw(image)
        draw.ellipse(self.coords, fill=self.pen.color, outline=self.pen.color)
        return image

class DrawRectangleCommand(Command):
    """Command to draw a rectangle."""

    def __init__(self, x1: int, y1: int, x2: int, y2: int, pen: PenConfig):
        self.coords = (x1, y1, x2, y2)
        self.pen = pen

    def execute(self, image: Image.Image) -> Image.Image:
        """Draws a rectangle on the image."""
        draw = ImageDraw.Draw(image)
        draw.rectangle(self.coords, outline=self.pen.color, width=self.pen.size)
        return image

class DrawLineCommand(Command):
    """Command to draw a line."""

    def __init__(self, x1: int, y1: int, x2: int, y2: int, pen: PenConfig):
        self.coords = (x1, y1, x2, y2)
        self.pen = pen

    def execute(self, image: Image.Image) -> Image.Image:
        """Draws a line on the image."""
        draw = ImageDraw.Draw(image)
        draw.line(self.coords, fill=self.pen.color, width=self.pen.size)
        return image

class DrawTextCommand(Command):
    """Command to draw text."""

    def __init__(self, x: int, y: int, text: str, pen: PenConfig):
        self.pos = (x, y)
        self.text = text
        self.pen = pen

    def execute(self, image: Image.Image) -> Image.Image:
        """Draws text on the image."""
        draw = ImageDraw.Draw(image)
        # In a real app we might want to load a font, but for now use default
        draw.text(self.pos, self.text, fill=self.pen.color)
        return image

class FilterCommand(Command):
    """Command to apply a filter."""

    def __init__(self, filter_strategy: FilterStrategy) -> None:
        self.filter_strategy = filter_strategy

    def execute(self, image: Image.Image) -> Image.Image:
        """Applies the strategy to the image."""
        return self.filter_strategy.apply(image)
