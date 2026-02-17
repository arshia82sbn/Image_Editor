from abc import ABC, abstractmethod
from typing import Tuple

from PIL import Image


class ImageRepository(ABC):
    """Abstract base class for image persistence."""

    @abstractmethod
    def load(self, path: str) -> Image.Image:
        """Loads an image from the given path.

        Args:
            path (str): Path to the image file.

        Returns:
            Image.Image: The loaded image.
        """
        pass

    @abstractmethod
    def save(self, image: Image.Image, path: str) -> None:
        """Saves an image to the given path.

        Args:
            image (Image.Image): The image to save.
            path (str): Path where the image should be saved.
        """
        pass

    @abstractmethod
    def resize(self, image: Image.Image, size: Tuple[int, int]) -> Image.Image:
        """Resizes an image to fit within the specified dimensions.

        Args:
            image (Image.Image): The image to resize.
            size (Tuple[int, int]): The maximum (width, height) allowed.

        Returns:
            Image.Image: The resized image.
        """
        pass
