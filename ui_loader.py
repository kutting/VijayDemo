from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


def load_ui(path, parent=None):
    loader = QUiLoader()
    file = QFile(path)

    if not file.open(QFile.ReadOnly):
        raise RuntimeError(f"Cannot open UI file: {path}")

    widget = loader.load(file, parent)
    file.close()

    if widget is None:
        raise RuntimeError(f"Failed to load UI file: {path}")

    return widget
