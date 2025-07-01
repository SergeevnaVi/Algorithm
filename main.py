import sys
from scr.auth import Registration
from scr.result_page import ResultPage
from scr.loadGraph import LoadingGraphPage
from scr.navigation import Navigation
from scr.developer_page import DeveloperPage, Developer
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import pyqtSlot
from algorithm import Ui_Algorithm

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Algorithm()
        self.ui.setupUi(self)

        # Устанавливаем название окна
        self.setWindowTitle("Algorithm")

        # Запрещаем изменение размера окна
        self.setFixedSize(self.width(), self.height())

        self.registration = Registration(self.ui)
        self.navigation = Navigation(self.ui)
        self.loading_graph_page = LoadingGraphPage(self)
        self.result = ResultPage(self.ui)
        self.developer = Developer(1, "admin")

        self.developer_page = DeveloperPage(self)
        # Устанавливаем кол-во строк по умолчанию
        self._developer_page_row_count = 15
        self.ui.stackedWidget.addWidget(self.developer_page)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.go_to_load_button = self.ui.pushButton_resume
        self.go_to_load_button.blockSignals(True)

        # Подключаем сигнал изменения индекса comboBox_task к функции разблокировки
        self.ui.comboBox_task.currentIndexChanged.connect(self.enable_go_to_load)
        # Подключаем сигнал currentChanged stackedWidget к методу очистки таблицы разработчика в developer_page
        self.ui.stackedWidget.currentChanged.connect(self._on_stacked_widget_changed)

        self.ui.pushButton_enter.clicked.connect(self.registration.handle_signin)
        self.ui.pushButton_registration.clicked.connect(self.navigation.go_to_page_registr)
        self.ui.pushButton_registration_db.clicked.connect(self.registration.handle_signup)

        self.ui.pushButton_resume.clicked.connect(self.navigation.go_to_loading_graph)
        self.ui.pushButton_back.clicked.connect(self.navigation.go_to_main)
        self.ui.pushButton_back_2.clicked.connect(self.navigation.go_to_loading_graph)
        self.ui.pushButton_on_main.clicked.connect(self.navigation.go_to_auth)

        self.ui.pushButton_download.clicked.connect(self.result.download_report)
        self.ui.pushButton_compare.clicked.connect(self.result.compare_with_other_algorithm)

        self.ui.pushButton_loading.clicked.connect(self.loading_graph_page.handle_run_algorithm)
        self.ui.pushButton_run.clicked.connect(self.loading_graph_page.handle_run_algorithm)
        self.ui.comboBox_task.currentIndexChanged.connect(self.loading_graph_page.set_task_type_from_combobox)


    def enable_go_to_load(self, index):
        """Разблокирует сигнал clicked кнопки "Продолжить", если выбрана задача."""
        if index != 0:
            self.go_to_load_button.blockSignals(False)
        else:
            self.go_to_load_button.blockSignals(True)
            

    @pyqtSlot(int)
    def _on_stacked_widget_changed(self, index):
        """Обрабатывает смену страниц в stackedWidget."""
        if index == 5:
            self.developer_page.tableWidget_3.setRowCount(self._developer_page_row_count)
            for row in range(self.developer_page.tableWidget_3.rowCount()):
                for col in range(self.developer_page.tableWidget_3.columnCount()):
                    item = QTableWidgetItem("")
                    self.developer_page.tableWidget_3.setItem(row, col, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Установка черного текста по умолчанию
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.WindowText, QColor("black"))
    palette.setColor(QPalette.ColorRole.Text, QColor("black"))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor("black"))
    palette.setColor(QPalette.ColorRole.PlaceholderText, QColor("gray"))
    app.setPalette(palette)

    window = MainApp()
    window.show()
    sys.exit(app.exec())