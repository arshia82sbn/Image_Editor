from typing import Optional, Tuple

from PIL import Image

from image_editor.core.commands import Command, FilterCommand
from image_editor.core.filters import get_filter
from image_editor.core.repository import ImageRepository
from image_editor.models.pen import PenConfig
from image_editor.models.state import EditorState


class ImageEditor:
    """Facade for the image editor application logic.

    Manages the state, commands, and repository interactions.
    """

    def __init__(self, repository: ImageRepository) -> None:
        """Initializes the editor with a repository.

        Args:
            repository (ImageRepository): The repository to use for image operations.
        """
        self.state = EditorState()
        self.pen = PenConfig()
        self.repository = repository

    def open_image(self, file_path: str, canvas_size: Tuple[int, int]) -> Image.Image:
        """Opens and resizes an image using the repository.

        Args:
            file_path (str): Path to the image file.
            canvas_size (Tuple[int, int]): Size to resize the image to.

        Returns:
            Image.Image: The opened and resized image.
        """
        image = self.repository.load(file_path)
        resized = self.repository.resize(image, canvas_size)

        self.state.file_path = file_path
        self.state.original_image = resized.copy()
        self.state.current_image = resized.copy()
        self.state.history = []

        return self.state.current_image

    def save_current_image(self, file_path: str) -> None:
        """Saves the current image using the repository.

        Args:
            file_path (str): Path to save the image to.
        """
        if self.state.current_image:
            self.repository.save(self.state.current_image, file_path)

    def apply_command(self, command: Command, push_to_history: bool = True) -> Image.Image:
        """Executes a command on the current image and optionally saves to history.

        Args:
            command (Command): The command to execute.
            push_to_history (bool): Whether to save the current state to history.

        Returns:
            Image.Image: The updated image.

        Raises:
            ValueError: If no image is loaded.
        """
        if not self.state.current_image:
            raise ValueError("No image loaded.")

        if push_to_history:
            self.state.push_history(self.state.current_image)

        self.state.current_image = command.execute(self.state.current_image)
        return self.state.current_image

    def apply_filter(self, filter_name: str) -> Image.Image:
        """Applies a named filter to the current image.

        Args:
            filter_name (str): Name of the filter.

        Returns:
            Image.Image: The updated image.
        """
        strategy = get_filter(filter_name)
        command = FilterCommand(strategy)
        return self.apply_command(command)

    def undo(self) -> Optional[Image.Image]:
        """Reverts the last change.

        Returns:
            Optional[Image.Image]: The previous image state.
        """
        previous = self.state.pop_history()
        if previous:
            self.state.current_image = previous
            return self.state.current_image
        return None

    def clear(self) -> Optional[Image.Image]:
        """Clears all changes and reverts to the original image.

        Returns:
            Optional[Image.Image]: The original image.
        """
        if self.state.original_image and self.state.current_image:
            self.state.push_history(self.state.current_image)
            self.state.current_image = self.state.original_image.copy()
            return self.state.current_image
        return None

    def set_pen_color(self, color: str) -> None:
        """Sets the pen color.

        Args:
            color (str): Hex color code.
        """
        self.pen.color = color

    def set_pen_size(self, size: int) -> None:
        """Sets the pen size.

        Args:
            size (int): Pen diameter in pixels.
        """
        self.pen.size = size
