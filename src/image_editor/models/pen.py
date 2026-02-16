from dataclasses import dataclass

@dataclass
class PenConfig:
    """Configuration for the drawing pen.

    Attributes:
        color (str): Hex color code of the pen.
        size (int): Diameter of the pen in pixels.
    """
    color: str = "#000000"
    size: int = 5
