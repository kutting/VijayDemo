from PySide6.QtWidgets import QMainWindow, QApplication
from ui_loader import load_ui


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = load_ui("ui/main_window.ui", self)

        self._connect_actions()

    def _connect_actions(self) -> None:
        self.ui.actionQuit.triggered.connect(QApplication.quit)
        self.ui.actionNew_Report.triggered.connect(self._new_report)
        self.ui.actionConfiguration.triggered.connect(self._open_configuration)

    def _new_report(self) -> None:
        dialog = load_ui("ui/report_parameters_modal.ui", self)
        dialog.exec()

    def _open_configuration(self) -> None:
        dialog = load_ui("ui/configuration_modal.ui", self)
        dialog.exec()

    def show(self) -> None:
        self.ui.show()