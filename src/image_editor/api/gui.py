import tkinter as tk
from tkinter import colorchooser, filedialog, ttk
from typing import Callable, Optional

from PIL import Image, ImageTk

from image_editor.core.commands import (
    DrawLineCommand,
    DrawOvalCommand,
    DrawRectangleCommand,
    DrawTextCommand,
)
from image_editor.core.editor import ImageEditor
from image_editor.infra.repository import FileSystemImageRepository


class ImageEditorApp:
    """The main GUI application for the Image Editor."""

    def __init__(self, root: tk.Tk):
        """Initializes the application.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("Image Drawing Tool")
        self.root.geometry("1100x700")
        self.root.config(bg="white")

        # Initialize core with infra implementation
        self.repository = FileSystemImageRepository()
        self.editor = ImageEditor(self.repository)

        self.current_tool = "Free Draw"
        self.temp_item: Optional[int] = None
        self.start_x = 0
        self.start_y = 0
        self._current_photo: Optional[ImageTk.PhotoImage] = None

        self._setup_ui()

    def _setup_ui(self) -> None:
        """Sets up the user interface components."""
        self._setup_sidebar()
        self._setup_canvas()

    def _setup_sidebar(self) -> None:
        """Creates and populates the sidebar."""
        self.sidebar = tk.Frame(self.root, width=200, height=700, bg="#47CDD2")
        self.sidebar.pack(side="left", fill="y")

        self._setup_action_buttons()
        self._setup_tool_selection()
        self._setup_text_input()
        self._setup_pen_size_controls()
        self._setup_filter_selection()

    def _setup_action_buttons(self) -> None:
        """Adds main action buttons to the sidebar."""
        tk.Button(self.sidebar, text="Add Image", command=self._add_image).pack(pady=10, fill="x", padx=10)
        tk.Button(self.sidebar, text="Undo", command=self._undo).pack(pady=5, fill="x", padx=10)
        tk.Button(self.sidebar, text="Clear", command=self._clear).pack(pady=5, fill="x", padx=10)
        tk.Button(self.sidebar, text="Change Color", command=self._change_color).pack(pady=5, fill="x", padx=10)
        tk.Button(self.sidebar, text="Save Image", command=self._save_image).pack(pady=10, fill="x", padx=10)

    def _setup_tool_selection(self) -> None:
        """Adds tool selection radio buttons."""
        tk.Label(self.sidebar, text="Tools", bg="#47CDD2").pack(pady=(10, 0))
        tools = ["Free Draw", "Rectangle", "Line", "Text"]
        self.tool_var = tk.StringVar(value="Free Draw")
        for tool in tools:
            tk.Radiobutton(self.sidebar, text=tool, variable=self.tool_var, value=tool,
                           command=self._update_tool).pack(anchor="w", padx=20)

    def _setup_text_input(self) -> None:
        """Adds text entry for the text tool."""
        self.text_entry = tk.Entry(self.sidebar)
        self.text_entry.pack(pady=5, padx=10)
        self.text_entry.insert(0, "Enter text here")

    def _setup_pen_size_controls(self) -> None:
        """Adds pen size selection controls."""
        tk.Label(self.sidebar, text="Pen Size", bg="#47CDD2").pack(pady=(10, 0))
        self.size_var = tk.IntVar(value=5)

        def make_set_size(s: int) -> Callable[[], None]:
            return lambda: self.editor.set_pen_size(s)

        size_frame = tk.Frame(self.sidebar, bg="#47CDD2")
        size_frame.pack(fill="x", padx=10)
        for size in [3, 5, 7]:
            tk.Radiobutton(size_frame, text=str(size), variable=self.size_var, value=size,
                           command=make_set_size(size), bg="#47CDD2").pack(side="left", expand=True)

    def _setup_filter_selection(self) -> None:
        """Adds filter selection dropdown."""
        tk.Label(self.sidebar, text="Select Filter", bg="#47CDD2").pack(pady=(20, 0))
        self.filter_combobox = ttk.Combobox(self.sidebar, values=[
            "Black and White", "Blur", "Emboss", "Sharpen", "Smooth"
        ])
        self.filter_combobox.pack(pady=5, padx=10)
        self.filter_combobox.bind("<<ComboboxSelected>>", self._apply_filter)

    def _setup_canvas(self) -> None:
        """Creates and binds the drawing canvas."""
        self.canvas = tk.Canvas(self.root, width=900, height=700, bg="white")
        self.canvas.pack(side="right", expand=True, fill="both")

        self.canvas.bind("<B1-Motion>", self._on_canvas_drag)
        self.canvas.bind("<Button-1>", self._on_canvas_click)
        self.canvas.bind("<ButtonRelease-1>", self._on_canvas_release)

    def _update_tool(self) -> None:
        self.current_tool = self.tool_var.get()

    def _add_image(self) -> None:
        file_path = filedialog.askopenfilename()
        if file_path:
            self.root.update()
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()

            image = self.editor.open_image(file_path, (canvas_width, canvas_height))
            self._display_image(image)

    def _save_image(self) -> None:
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            self.editor.save_current_image(file_path)

    def _undo(self) -> None:
        image = self.editor.undo()
        if image:
            self._display_image(image)

    def _clear(self) -> None:
        image = self.editor.clear()
        if image:
            self._display_image(image)

    def _change_color(self) -> None:
        color = colorchooser.askcolor(title="Select Pen Color")[1]
        if color:
            self.editor.set_pen_color(color)

    def _apply_filter(self, event: tk.Event) -> None:
        filter_name = self.filter_combobox.get()
        if filter_name:
            image = self.editor.apply_filter(filter_name)
            self._display_image(image)

    def _display_image(self, image: Image.Image) -> None:
        photo = ImageTk.PhotoImage(image)
        self._current_photo = photo
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=photo, anchor="nw")

    def _on_canvas_click(self, event: tk.Event) -> None:
        self.start_x = event.x
        self.start_y = event.y

        if not self.editor.state.current_image:
            return

        if self.current_tool in ["Free Draw", "Rectangle", "Line"]:
            self.editor.state.push_history(self.editor.state.current_image)

        if self.current_tool == "Text":
            text = self.text_entry.get()
            command = DrawTextCommand(event.x, event.y, text, self.editor.pen)
            image = self.editor.apply_command(command)
            self._display_image(image)

    def _on_canvas_drag(self, event: tk.Event) -> None:
        if not self.editor.state.current_image:
            return

        if self.current_tool == "Free Draw":
            command = DrawOvalCommand(
                event.x - self.editor.pen.size, event.y - self.editor.pen.size,
                event.x + self.editor.pen.size, event.y + self.editor.pen.size,
                self.editor.pen
            )
            image = self.editor.apply_command(command, push_to_history=False)
            self._display_image(image)

        elif self.current_tool in ["Rectangle", "Line"]:
            if self.temp_item:
                self.canvas.delete(self.temp_item)

            if self.current_tool == "Rectangle":
                self.temp_item = self.canvas.create_rectangle(
                    self.start_x, self.start_y, event.x, event.y,
                    outline=self.editor.pen.color, width=self.editor.pen.size
                )
            else: # Line
                self.temp_item = self.canvas.create_line(
                    self.start_x, self.start_y, event.x, event.y,
                    fill=self.editor.pen.color, width=self.editor.pen.size
                )

    def _on_canvas_release(self, event: tk.Event) -> None:
        if not self.editor.state.current_image:
            return

        if self.current_tool == "Rectangle":
            rect_cmd = DrawRectangleCommand(self.start_x, self.start_y, event.x, event.y, self.editor.pen)
            image = self.editor.apply_command(rect_cmd, push_to_history=False)
            self._display_image(image)
        elif self.current_tool == "Line":
            line_cmd = DrawLineCommand(self.start_x, self.start_y, event.x, event.y, self.editor.pen)
            image = self.editor.apply_command(line_cmd, push_to_history=False)
            self._display_image(image)

        self.temp_item = None

def main() -> None:
    """Entry point for the application."""
    root = tk.Tk()
    _ = ImageEditorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
