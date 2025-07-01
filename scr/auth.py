from db.connect import check_user, check_admin, create_user
from scr.navigation import Navigation
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMessageBox


class Registration:
    def __init__(self, ui):
        self.ui = ui
        self.current_user_id = None
        self.navigation = Navigation(self.ui)

        # Изначально отключаем кнопку "Войти"
        self.ui.pushButton_enter.setEnabled(False)

        # Подключаем сигнал изменения текста комбобокса к функции проверки
        self.ui.comboBox_role.currentTextChanged.connect(self.check_role_selection)

    def check_role_selection(self, text):
        """Включает кнопку "Войти", если выбрана роль."""
        if text != "Выберите роль":
            self.ui.pushButton_enter.setEnabled(True)
        else:
            self.ui.pushButton_enter.setEnabled(False)

    def handle_signup(self):
        name = self.ui.lineEdit_name.text()
        login = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_pass.text()
        phone = self.ui.lineEdit_phone.text()

        if not name or not login or not password or not phone:
            self.show_error("Заполните все поля!")
            return
        if len(phone) != 11 or not phone.isdigit():
            self.show_error("Неверный формат номера телефона!")
            return
        if len(password) < 8:
            self.show_error("Пароль должен быть не менее 8 символов!")
            return
        
        success, message = create_user(name, login, password, phone)
        if success:
            self.show_success("Регистрация прошла успешно")

            self.current_user_id = check_user(login, password)
            if self.current_user_id:
                self.navigation.go_to_main()
            else:
                self.show_error("Ошибка при получении ID пользователя!")
        else:
            self.show_error(message)


    def handle_signin(self):
        role = self.ui.comboBox_role.currentText()
        login = self.ui.lineEdit_login_auth.text()
        password = self.ui.lineEdit_pass_auth.text()

        if not login or not password:
            self.show_error("Заполните все поля!")
            return
        
        if role == "Выберите роль":
            QMessageBox.warning(self.ui, "Ошибка", "Пожалуйста, выберите роль")
            return
        
        if role == "Пользователь":
            user = check_user(login, password)
            if user:
                self.current_user_id = user
                self.show_success("Вход выполнен как пользователь")
                self.navigation.go_to_main()
            else:
                self.show_error("Неверный логин или пароль")
        
        elif role == "Разработчик":
            admin = check_admin(login, password)
            if admin:
                self.show_success("Вход выполнен как разработчик")
                self.navigation.go_to_developer()
            else:
                self.show_error("Неверный логин или пароль")


    def show_error(self, message):
        """Отображение окна с ошибкой"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle("Ошибка")
        self.set_message_palette(msg)
        msg.exec()

    def show_success(self, message):
        """Отображение окна с успешным сообщением"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle("Успех")
        self.set_message_palette(msg)
        msg.exec()

    def set_message_palette(self, msg):
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.ColorRole.Window, QColor("#2b2b2b"))
        dark_palette.setColor(QPalette.ColorRole.WindowText, QColor("white"))
        dark_palette.setColor(QPalette.ColorRole.Button, QColor("#3c3c3c"))
        dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor("white"))
        msg.setPalette(dark_palette)


class MainPage:
    def __init__(self, ui):
        self.ui = ui
        self.navigation = Navigation(self.ui)

    def handle_task_selection(self):
        selected_task = self.ui.comboBox_task.currentText()

        if selected_task == "Задача коммивояжера":
            self.navigation.go_to_loading_graph("tsp")
        elif selected_task == "Алгоритм Дейкстры":
            self.navigation.go_to_loading_graph("dijkstra")
        elif selected_task == "Алгоритм Крускала":
            self.navigation.go_to_loading_graph("kruskal")
        else:
            self.show_error("Выберите задачу!")
    
    def show_error(self, message):
        """Отображение окна с ошибкой"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle("Ошибка")
        self.set_message_palette(msg)
        msg.exec()

    def set_message_palette(self, msg):
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.ColorRole.Window, QColor("#2b2b2b"))
        dark_palette.setColor(QPalette.ColorRole.WindowText, QColor("white"))
        dark_palette.setColor(QPalette.ColorRole.Button, QColor("#3c3c3c"))
        dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor("white"))
        msg.setPalette(dark_palette)
