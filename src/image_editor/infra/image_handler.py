from typing import Tuple
from PIL import Image
import os

def load_image(file_path: str) -> Image.Image:
    """Loads an image from the specified file path.

    Args:
        file_path (str): The path to the image file.

    Returns:
        Image.Image: The loaded PIL Image object.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If the file cannot be opened as an image.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Image file not found: {file_path}")

    return Image.open(file_path)

def save_image(image: Image.Image, file_path: str) -> None:
    """Saves the given image to the specified file path.

    Args:
        image (Image.Image): The PIL Image object to save.
        file_path (str): The path where the image should be saved.
    """
    image.save(file_path)

def resize_to_fit(image: Image.Image, max_size: Tuple[int, int]) -> Image.Image:
    """Resizes an image to fit within the specified dimensions while maintaining aspect ratio.

    Args:
        image (Image.Image): The image to resize.
        max_size (Tuple[int, int]): The maximum (width, height) allowed.

    Returns:
        Image.Image: The resized image.
    """
    resampling = getattr(Image, "Resampling", Image).LANCZOS
    # Create a copy to avoid modifying the original
    img_copy = image.copy()
    img_copy.thumbnail(max_size, resampling)
    return img_copy
