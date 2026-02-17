# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2023-10-27
### Changed
- Refactored architecture to use the **Repository pattern** for image persistence.
- De-coupled core logic from infrastructure by introducing `ImageRepository` interface.
- Refactored GUI in `ImageEditorApp` for better maintainability and readability by decomposing large UI setup methods.
- Enhanced `pyproject.toml` with stricter `ruff` linting rules and `mypy` type checking.

### Added
- `FileSystemImageRepository` for local file system interactions.
- Mock-based unit tests for `ImageEditor`.
- Edge-case testing for image loading and command application.

## [0.1.0] - 2023-10-27
### Added
- Initial refactored version of the Image Editor.
- Modular architecture with `api`, `core`, `infra`, and `models`.
- Strategy pattern for filters.
- Command pattern for drawing operations.
- Type hints and Google-style docstrings.
- Unit tests and CI configuration.
