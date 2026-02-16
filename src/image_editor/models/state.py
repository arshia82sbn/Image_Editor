from typing import List, Optional
from PIL import Image
from dataclasses import dataclass, field

@dataclass
class EditorState:
    """Represents the state of the image editor.

    Attributes:
        current_image (Optional[Image.Image]): The image currently being edited.
        original_image (Optional[Image.Image]): The original image loaded.
        history (List[Image.Image]): Stack of previous image states for undo.
        file_path (Optional[str]): Path to the current image file.
    """
    current_image: Optional[Image.Image] = None
    original_image: Optional[Image.Image] = None
    history: List[Image.Image] = field(default_factory=list)
    file_path: Optional[str] = None

    def push_history(self, image: Image.Image) -> None:
        """Pushes a copy of the given image onto the history stack.

        Args:
            image (Image.Image): The image to save in history.
        """
        self.history.append(image.copy())

    def pop_history(self) -> Optional[Image.Image]:
        """Pops the last image from the history stack.

        Returns:
            Optional[Image.Image]: The previous image state, or None if history is empty.
        """
        if not self.history:
            return None
        return self.history.pop()
