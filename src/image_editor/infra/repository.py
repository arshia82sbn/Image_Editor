from pathlib import Path
from typing import Tuple

from PIL import Image

from image_editor.core.repository import ImageRepository


class FileSystemImageRepository(ImageRepository):
    """Implementation of ImageRepository using the local file system and Pillow."""

    def load(self, path: str) -> Image.Image:
        """Loads an image from the local file system.

        Args:
            path (str): The path to the image file.

        Returns:
            Image.Image: The loaded image.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"Image file not found: {path}")

        return Image.open(path)

    def save(self, image: Image.Image, path: str) -> None:
        """Saves an image to the local file system.

        Args:
            image (Image.Image): The image to save.
            path (str): The destination path.
        """
        image.save(path)

    def resize(self, image: Image.Image, size: Tuple[int, int]) -> Image.Image:
        """Resizes an image using LANCZOS resampling.

        Args:
            image (Image.Image): The image to resize.
            size (Tuple[int, int]): The maximum dimensions.

        Returns:
            Image.Image: The resized image.
        """
        # Maintain compatibility with older Pillow versions if necessary
        resampling = getattr(Image, "Resampling", Image).LANCZOS
        img_copy = image.copy()
        img_copy.thumbnail(size, resampling)
        return img_copy
