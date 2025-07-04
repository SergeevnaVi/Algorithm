# Form implementation generated from reading ui file 'алгоритмы.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Algorithm(object):
    def setupUi(self, Algorithm):
        Algorithm.setObjectName("Algorithm")
        Algorithm.resize(635, 670)
        self.centralwidget = QtWidgets.QWidget(parent=Algorithm)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    background-color: #F4F6F7;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 20, 591, 591))
        self.stackedWidget.setObjectName("stackedWidget")
        self.auth = QtWidgets.QWidget()
        self.auth.setObjectName("auth")
        self.label_9 = QtWidgets.QLabel(parent=self.auth)
        self.label_9.setGeometry(QtCore.QRect(110, 30, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: black;")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.comboBox_role = QtWidgets.QComboBox(parent=self.auth)
        self.comboBox_role.setGeometry(QtCore.QRect(150, 160, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_role.setFont(font)
        self.comboBox_role.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #D5D8DC;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"QComboBox::item {\n"
"    color: black;\n"
"}\n"
"\n"
"")
        self.comboBox_role.setEditable(False)
        self.comboBox_role.setObjectName("comboBox_role")
        self.comboBox_role.addItem("")
        self.comboBox_role.addItem("")
        self.comboBox_role.addItem("")
        self.lineEdit_login_auth = QtWidgets.QLineEdit(parent=self.auth)
        self.lineEdit_login_auth.setGeometry(QtCore.QRect(150, 210, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_login_auth.setFont(font)
        self.lineEdit_login_auth.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #D5D8DC;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}")
        self.lineEdit_login_auth.setInputMask("")
        self.lineEdit_login_auth.setObjectName("lineEdit_login_auth")
        self.lineEdit_pass_auth = QtWidgets.QLineEdit(parent=self.auth)
        self.lineEdit_pass_auth.setGeometry(QtCore.QRect(150, 260, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_pass_auth.setFont(font)
        self.lineEdit_pass_auth.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #D5D8DC;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}")
        self.lineEdit_pass_auth.setInputMask("")
        self.lineEdit_pass_auth.setObjectName("lineEdit_pass_auth")
        self.pushButton_enter = QtWidgets.QPushButton(parent=self.auth)
        self.pushButton_enter.setGeometry(QtCore.QRect(150, 330, 281, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_enter.setFont(font)
        self.pushButton_enter.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.pushButton_registration = QtWidgets.QPushButton(parent=self.auth)
        self.pushButton_registration.setGeometry(QtCore.QRect(150, 390, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_registration.setFont(font)
        self.pushButton_registration.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_registration.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: black;\n"
"    border: none;\n"
"    font-weight: normal;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    color: black;\n"
"}")
        self.pushButton_registration.setFlat(True)
        self.pushButton_registration.setObjectName("pushButton_registration")
        self.stackedWidget.addWidget(self.auth)
        self.registration = QtWidgets.QWidget()
        self.registration.setObjectName("registration")
        self.label_registration = QtWidgets.QLabel(parent=self.registration)
        self.label_registration.setGeometry(QtCore.QRect(90, 30, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_registration.setFont(font)
        self.label_registration.setStyleSheet("color: black;")
        self.label_registration.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_registration.setObjectName("label_registration")
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.registration)
        self.lineEdit_name.setGeometry(QtCore.QRect(150, 150, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #D5D8DC;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}")
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.pushButton_registration_db = QtWidgets.QPushButton(parent=self.registration)
        self.pushButton_registration_db.setGeometry(QtCore.QRect(150, 360, 281, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_registration_db.setFont(font)
        self.pushButton_registration_db.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_registration_db.setObjectName("pushButton_registration_db")
        self.lineEdit_login = QtWidgets.QLineEdit(parent=self.registration)
        self.lineEdit_login.setGeometry(QtCore.QRect(150, 200, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #D5D8DC;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}")
        self.lineEdit_login.setInputMask("")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.lineEdit_pass = QtWidgets.QLineEdit(parent=self.registration)
        self.lineEdit_pass.setGeometry(QtCore.QRect(150, 250, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_pass.setFont(font)
        self.lineEdit_pass.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #D5D8DC;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}")
        self.lineEdit_pass.setInputMask("")
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.lineEdit_phone = QtWidgets.QLineEdit(parent=self.registration)
        self.lineEdit_phone.setGeometry(QtCore.QRect(150, 300, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_phone.setFont(font)
        self.lineEdit_phone.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #D5D8DC;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}")
        self.lineEdit_phone.setInputMask("")
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.stackedWidget.addWidget(self.registration)
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.label = QtWidgets.QLabel(parent=self.main)
        self.label.setGeometry(QtCore.QRect(110, 40, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox_task = QtWidgets.QComboBox(parent=self.main)
        self.comboBox_task.setGeometry(QtCore.QRect(150, 170, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_task.setFont(font)
        self.comboBox_task.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #D5D8DC;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"QComboBox::item {\n"
"    color: black;\n"
"}\n"
"")
        self.comboBox_task.setObjectName("comboBox_task")
        self.comboBox_task.addItem("")
        self.comboBox_task.addItem("")
        self.comboBox_task.addItem("")
        self.comboBox_task.addItem("")
        self.pushButton_resume = QtWidgets.QPushButton(parent=self.main)
        self.pushButton_resume.setGeometry(QtCore.QRect(150, 310, 281, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_resume.setFont(font)
        self.pushButton_resume.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_resume.setObjectName("pushButton_resume")
        self.stackedWidget.addWidget(self.main)
        self.loading_graph = QtWidgets.QWidget()
        self.loading_graph.setObjectName("loading_graph")
        self.label_2 = QtWidgets.QLabel(parent=self.loading_graph)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: black;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.loading_graph)
        self.tableWidget.setGeometry(QtCore.QRect(50, 100, 481, 161))
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    background-color: #FFFFFF;\n"
"    alternate-background-color: #F2F2F2;\n"
"    gridline-color: #D5D8DC;\n"
"    selection-background-color: #AED6F1;\n"
"    font-size: 12pt;\n"
"}")
        self.tableWidget.setRowCount(15)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(146)
        self.widget = QtWidgets.QWidget(parent=self.loading_graph)
        self.widget.setGeometry(QtCore.QRect(0, 280, 591, 161))
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_ogr = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_ogr.setStyleSheet("QLineEdit, QComboBox {\n"
"    background-color: #FBFCFC;\n"
"    border: 1px solid #D5D8DC;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.lineEdit_ogr.setObjectName("lineEdit_ogr")
        self.gridLayout.addWidget(self.lineEdit_ogr, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 3, 2, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 4)
        self.lineEdit_start = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_start.setStyleSheet("QLineEdit, QComboBox {\n"
"    background-color: #FBFCFC;\n"
"    border: 1px solid #D5D8DC;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.lineEdit_start.setObjectName("lineEdit_start")
        self.gridLayout.addWidget(self.lineEdit_start, 2, 0, 1, 1)
        self.lineEdit_end = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_end.setStyleSheet("QLineEdit, QComboBox {\n"
"    background-color: #FBFCFC;\n"
"    border: 1px solid #D5D8DC;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.lineEdit_end.setObjectName("lineEdit_end")
        self.gridLayout.addWidget(self.lineEdit_end, 2, 1, 1, 1)
        self.pushButton_loading = QtWidgets.QPushButton(parent=self.loading_graph)
        self.pushButton_loading.setGeometry(QtCore.QRect(230, 490, 161, 41))
        self.pushButton_loading.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_loading.setObjectName("pushButton_loading")
        self.pushButton_back = QtWidgets.QPushButton(parent=self.loading_graph)
        self.pushButton_back.setGeometry(QtCore.QRect(30, 490, 161, 41))
        self.pushButton_back.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_run = QtWidgets.QPushButton(parent=self.loading_graph)
        self.pushButton_run.setGeometry(QtCore.QRect(430, 490, 161, 41))
        self.pushButton_run.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_run.setObjectName("pushButton_run")
        self.stackedWidget.addWidget(self.loading_graph)
        self.result = QtWidgets.QWidget()
        self.result.setObjectName("result")
        self.label_7 = QtWidgets.QLabel(parent=self.result)
        self.label_7.setGeometry(QtCore.QRect(100, 10, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: black;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.result)
        self.graphicsView.setGeometry(QtCore.QRect(0, 81, 341, 251))
        self.graphicsView.setObjectName("graphicsView")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.result)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 350, 581, 201))
        self.tableWidget_2.setStyleSheet("QTableWidget {\n"
"    background-color: #FFFFFF;\n"
"    alternate-background-color: #F2F2F2;\n"
"    gridline-color: #D5D8DC;\n"
"    selection-background-color: #AED6F1;\n"
"    font-size: 12pt;\n"
"}")
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(185)
        self.pushButton_compare = QtWidgets.QPushButton(parent=self.result)
        self.pushButton_compare.setGeometry(QtCore.QRect(360, 190, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_compare.setFont(font)
        self.pushButton_compare.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_compare.setObjectName("pushButton_compare")
        self.pushButton_download = QtWidgets.QPushButton(parent=self.result)
        self.pushButton_download.setGeometry(QtCore.QRect(360, 130, 201, 41))
        self.pushButton_download.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_download.setObjectName("pushButton_download")
        self.pushButton_back_2 = QtWidgets.QPushButton(parent=self.result)
        self.pushButton_back_2.setGeometry(QtCore.QRect(360, 250, 201, 41))
        self.pushButton_back_2.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_back_2.setObjectName("pushButton_back_2")
        self.stackedWidget.addWidget(self.result)
        self.developer = QtWidgets.QWidget()
        self.developer.setObjectName("developer")
        self.label_8 = QtWidgets.QLabel(parent=self.developer)
        self.label_8.setGeometry(QtCore.QRect(90, 10, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: black;")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_testing = QtWidgets.QPushButton(parent=self.developer)
        self.pushButton_testing.setGeometry(QtCore.QRect(400, 390, 171, 41))
        self.pushButton_testing.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_testing.setObjectName("pushButton_testing")
        self.pushButton_add = QtWidgets.QPushButton(parent=self.developer)
        self.pushButton_add.setGeometry(QtCore.QRect(20, 390, 171, 41))
        self.pushButton_add.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_on_main = QtWidgets.QPushButton(parent=self.developer)
        self.pushButton_on_main.setGeometry(QtCore.QRect(190, 520, 211, 41))
        self.pushButton_on_main.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_on_main.setObjectName("pushButton_on_main")
        self.comboBox_task_2 = QtWidgets.QComboBox(parent=self.developer)
        self.comboBox_task_2.setGeometry(QtCore.QRect(40, 90, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_task_2.setFont(font)
        self.comboBox_task_2.setStyleSheet("QComboBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #D5D8DC;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"QComboBox::item {\n"
"    color: black;\n"
"}\n"
"")
        self.comboBox_task_2.setObjectName("comboBox_task_2")
        self.comboBox_task_2.addItem("")
        self.comboBox_task_2.addItem("")
        self.comboBox_task_2.addItem("")
        self.comboBox_task_2.addItem("")
        self.tableWidget_3 = QtWidgets.QTableWidget(parent=self.developer)
        self.tableWidget_3.setGeometry(QtCore.QRect(40, 160, 511, 211))
        self.tableWidget_3.setStyleSheet("QTableWidget {\n"
"    background-color: #FFFFFF;\n"
"    alternate-background-color: #F2F2F2;\n"
"    gridline-color: #D5D8DC;\n"
"    selection-background-color: #AED6F1;\n"
"    font-size: 12pt;\n"
"}")
        self.tableWidget_3.setRowCount(15)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(155)
        self.pushButton_edit = QtWidgets.QPushButton(parent=self.developer)
        self.pushButton_edit.setGeometry(QtCore.QRect(210, 390, 171, 41))
        self.pushButton_edit.setStyleSheet("QPushButton {\n"
"    background-color: #A9CCE3;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E86C1;\n"
"}")
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.stackedWidget.addWidget(self.developer)
        Algorithm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Algorithm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 26))
        self.menubar.setObjectName("menubar")
        Algorithm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Algorithm)
        self.statusbar.setObjectName("statusbar")
        Algorithm.setStatusBar(self.statusbar)

        self.retranslateUi(Algorithm)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(Algorithm)

    def retranslateUi(self, Algorithm):
        _translate = QtCore.QCoreApplication.translate
        Algorithm.setWindowTitle(_translate("Algorithm", "MainWindow"))
        self.label_9.setText(_translate("Algorithm", "Вход в систему"))
        self.comboBox_role.setItemText(0, _translate("Algorithm", "Выберите роль"))
        self.comboBox_role.setItemText(1, _translate("Algorithm", "Пользователь"))
        self.comboBox_role.setItemText(2, _translate("Algorithm", "Разработчик"))
        self.lineEdit_login_auth.setPlaceholderText(_translate("Algorithm", "Введите логин"))
        self.lineEdit_pass_auth.setPlaceholderText(_translate("Algorithm", "Введите пароль"))
        self.pushButton_enter.setText(_translate("Algorithm", "Войти"))
        self.pushButton_registration.setText(_translate("Algorithm", "Регистрация для пользователя"))
        self.label_registration.setText(_translate("Algorithm", "Регистрация пользователя"))
        self.lineEdit_name.setPlaceholderText(_translate("Algorithm", "Введите имя"))
        self.pushButton_registration_db.setText(_translate("Algorithm", "Зарегистрироваться"))
        self.lineEdit_login.setPlaceholderText(_translate("Algorithm", "Введите логин"))
        self.lineEdit_pass.setPlaceholderText(_translate("Algorithm", "Введите пароль"))
        self.lineEdit_phone.setPlaceholderText(_translate("Algorithm", "Введите номер телефона"))
        self.label.setText(_translate("Algorithm", "Оптимизатор графов"))
        self.comboBox_task.setItemText(0, _translate("Algorithm", "Выберите задачу"))
        self.comboBox_task.setItemText(1, _translate("Algorithm", "Задача коммивояжера"))
        self.comboBox_task.setItemText(2, _translate("Algorithm", "Кратчайший путь"))
        self.comboBox_task.setItemText(3, _translate("Algorithm", "Минимальное остовное дерево"))
        self.pushButton_resume.setText(_translate("Algorithm", "Продолжить"))
        self.label_2.setText(_translate("Algorithm", "Загрузка графа и настройка"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Algorithm", "Узел 1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Algorithm", "Узел 2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Algorithm", "Вес"))
        self.label_3.setText(_translate("Algorithm", "Стартовая вершина"))
        self.label_5.setText(_translate("Algorithm", "<html><head/><body><p>Ограничения маршрутов</p></body></html>"))
        self.checkBox.setText(_translate("Algorithm", "Учитывать направленность"))
        self.label_4.setText(_translate("Algorithm", "Конечная вершина"))
        self.label_6.setText(_translate("Algorithm", "Настройки параметров для алгоритма"))
        self.pushButton_loading.setText(_translate("Algorithm", "Загрузить граф"))
        self.pushButton_back.setText(_translate("Algorithm", "Назад"))
        self.pushButton_run.setText(_translate("Algorithm", "Запустить алгоритм"))
        self.label_7.setText(_translate("Algorithm", "Результат"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Algorithm", "Путь"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Algorithm", "Длина"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Algorithm", "Время"))
        self.pushButton_compare.setText(_translate("Algorithm", "Сравнить с другим \n"
"алгоритмом"))
        self.pushButton_download.setText(_translate("Algorithm", "Скачать отчёт (PDF/CSV)"))
        self.pushButton_back_2.setText(_translate("Algorithm", "Назад"))
        self.label_8.setText(_translate("Algorithm", "Разработчик"))
        self.pushButton_testing.setText(_translate("Algorithm", "Тестировать"))
        self.pushButton_add.setText(_translate("Algorithm", "Добавить"))
        self.pushButton_on_main.setText(_translate("Algorithm", "На главную"))
        self.comboBox_task_2.setItemText(0, _translate("Algorithm", "Выберите задачу"))
        self.comboBox_task_2.setItemText(1, _translate("Algorithm", "Задача коммивояжера"))
        self.comboBox_task_2.setItemText(2, _translate("Algorithm", "Кратчайший путь"))
        self.comboBox_task_2.setItemText(3, _translate("Algorithm", "Минимальное остовное дерево"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Algorithm", "Узел 1"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Algorithm", "Узел 2"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Algorithm", "Вес"))
        self.pushButton_edit.setText(_translate("Algorithm", "Редактировать"))
