from abc import ABC, abstractmethod

from PIL import Image, ImageFilter, ImageOps


class FilterStrategy(ABC):
    """Abstract base class for image filters."""

    @abstractmethod
    def apply(self, image: Image.Image) -> Image.Image:
        """Applies the filter to the given image.

        Args:
            image (Image.Image): The image to filter.

        Returns:
            Image.Image: The filtered image.
        """
        pass

class GrayscaleFilter(FilterStrategy):
    """Converts the image to grayscale."""

    def apply(self, image: Image.Image) -> Image.Image:
        """Applies grayscale filter."""
        return ImageOps.grayscale(image)

class BlurFilter(FilterStrategy):
    """Applies a blur effect to the image."""

    def apply(self, image: Image.Image) -> Image.Image:
        """Applies blur filter."""
        return image.filter(ImageFilter.BLUR)

class SharpenFilter(FilterStrategy):
    """Applies a sharpening effect to the image."""

    def apply(self, image: Image.Image) -> Image.Image:
        """Applies sharpen filter."""
        return image.filter(ImageFilter.SHARPEN)

class SmoothFilter(FilterStrategy):
    """Applies a smoothing effect to the image."""

    def apply(self, image: Image.Image) -> Image.Image:
        """Applies smooth filter."""
        return image.filter(ImageFilter.SMOOTH)

class EmbossFilter(FilterStrategy):
    """Applies an emboss effect to the image."""

    def apply(self, image: Image.Image) -> Image.Image:
        """Applies emboss filter."""
        return image.filter(ImageFilter.EMBOSS)

def get_filter(name: str) -> FilterStrategy:
    """Factory function to get a filter by name.

    Args:
        name (str): Name of the filter.

    Returns:
        FilterStrategy: The filter object.

    Raises:
        ValueError: If the filter name is not recognized.
    """
    filters = {
        "Black and White": GrayscaleFilter(),
        "Blur": BlurFilter(),
        "Sharpen": SharpenFilter(),
        "Smooth": SmoothFilter(),
        "Emboss": EmbossFilter(),
    }
    # Case insensitive lookup
    for key in filters:
        if key.lower() == name.lower():
            return filters[key]
    raise ValueError(f"Unknown filter: {name}")
