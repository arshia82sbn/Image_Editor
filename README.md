# Image Editor

A professional image editing and drawing tool built with Python and Pillow.

## Features
- **Image Loading/Saving**: Support for various image formats through a pluggable Repository pattern.
- **Drawing Tools**: Freehand, Rectangle, Line, and Text tools implemented via the Command pattern.
- **Filters**: Black & White, Blur, Emboss, Sharpen, and Smooth filters using the Strategy pattern.
- **Undo/Redo**: Robust history management for reverting or reapplying changes.
- **Customization**: Flexible pen color and size selection.

## Architecture & Design Patterns
The project follows a clean architecture with a clear separation of concerns:
- **api/**: Public interfaces, including the Tkinter GUI.
- **core/**: Business logic, commands, filters, and repository interfaces.
- **infra/**: Infrastructure implementations (e.g., file system repository).
- **models/**: Data classes and editor state.

### Design Patterns Used:
1. **Facade**: `ImageEditor` provides a simple interface to the complex editing logic.
2. **Command**: Drawing operations are encapsulated as objects, enabling undo/redo.
3. **Strategy**: Filters are implemented as interchangeable strategies.
4. **Repository**: Decouples business logic from image persistence details.
5. **Factory**: Used for creating filter strategies.

## Installation
```bash
pip install .
```

## Usage
```bash
image-editor
```

## Development
To install development dependencies and run tests:
```bash
pip install -e .[dev]
pytest
mypy src
ruff check src
```
