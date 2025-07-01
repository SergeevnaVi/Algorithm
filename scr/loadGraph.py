from PyQt6.QtGui import QPalette, QColor, QImage, QPixmap
from scr.navigation import Navigation
from PyQt6.QtWidgets import QMessageBox, QFileDialog, QGraphicsScene, QTableWidgetItem, QTableWidget
import networkx as nx
import matplotlib.pyplot as plt
from scr.algorithms import Algorithm
import csv
import time
import os


class LoadingGraphPage:
    def __init__(self, parent):
        self.parent = parent
        self.ui = parent.ui
        self.graph = {}
        self.directed = False
        self.navigation = Navigation(self.ui)
        self.task_type = None
        self.file_loaded = False
        self.graph_image_path = None
        self.time_taken = 0

        self.ui.pushButton_loading.clicked.connect(self.handle_csv_upload)
        self.ui.pushButton_run.clicked.connect(self.handle_run_algorithm)
        self.ui.comboBox_task.currentIndexChanged.connect(self.set_task_type_from_combobox)


    def set_task_type_from_combobox(self, index):
        """Устанавливает тип задачи на основе выбора в comboBox_task."""
        selected_text = self.ui.comboBox_task.itemText(index)
        if selected_text == "Задача коммивояжера":
            self.task_type = "tsp"
        elif selected_text == "Кратчайший путь":
            self.task_type = "dijkstra"
        elif selected_text == "Минимальное остовное дерево":
            self.task_type = "kruskal"
        print(f"Тип задачи: {self.task_type}")

    def handle_run_algorithm(self):
        """Запуск алгоритма на основе выбора"""
        self.directed = self.ui.checkBox.isChecked()
        ogr_route = self.ui.lineEdit_ogr.text()  # Получаем значение ограничения маршрутов

        if not self.file_loaded:
            self.handle_manual_input()
        self.load_graph_image()

        result = None

        start_time = time.time()

        # В зависимости от выбранного алгоритма, запускаем нужный метод
        if self.task_type == "tsp":
            print("Запуск алгоритма TSP...")
            result = Algorithm.tsp(self.graph)

        elif self.task_type == "dijkstra":
            start_node = self.ui.lineEdit_start.text()
            end_node = self.ui.lineEdit_end.text()
            if start_node and end_node:
                if start_node in self.graph and end_node in self.graph:
                    print(f"Запуск алгоритма Dijkstra с начальной вершиной: {start_node}, конечной: {end_node} и ограничением: {ogr_route}")
                    result = Algorithm.dijkstra(self.graph, start_node, end_node, ogr_route)
                else:
                    self.show_error("Одна из вершин не найдена в графе")
                    return
            else:
                self.show_error("Введите начальную и конечную вершину")
                return

        elif self.task_type == "kruskal":
            print("Запуск алгоритма Kruskal...")
            result = Algorithm.kruskal(self.graph)

        self.time_taken = time.time() - start_time

        self.ui.stackedWidget.setCurrentIndex(4)

        # Перенаправляем на страницу с результатами
        if result:
            self.update_result_table(result)
        else:
            self.show_error("Не удалось получить результат алгоритма.")


    def handle_csv_upload(self):
        """Загрузка CSV"""
        file_path, _ = QFileDialog.getOpenFileName(self.parent, "Выберите файл CSV", "", "CSV Files (*.csv)")
        if file_path:
            if self.load_csv(file_path):
                self.file_loaded = True

    def load_csv(self, file_path):
        """Загрузка данных из CSV файла в граф"""
        self.graph = {}
        try:
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    if len(row) < 3:
                        self.show_error(f"Ошибка в данных: строка должна содержать 3 элемента, но в строке найдено {len(row)}: {row}")
                        return False

                    node1, node2, weight = row[0], row[1], row[2]


                    try:
                        weight = float(weight)
                    except ValueError:
                        self.show_error(f"Ошибка в данных: некорректный вес в строке {row}")
                        return False

                    # Если вес корректен, добавляем в граф
                    if node1 not in self.graph:
                        self.graph[node1] = {}
                    self.graph[node1][node2] = weight
                    if not self.directed:
                        if node2 not in self.graph:
                            self.graph[node2] = {}
                        self.graph[node2][node1] = weight

            # После загрузки графа, отобразить его
            self.load_graph_image()
            return True
        except FileNotFoundError:
            self.show_error(f"Файл не найден: {file_path}")
            return False
        except Exception as e:
            self.show_error(f"Произошла ошибка при чтении файла: {e}")
            return False

    def load_graph_image(self):
        """Отобразить граф в graphicsView"""
        # Создаем граф из данных
        G = nx.Graph()
        if not self.graph:
            print("Ошибка: граф пустой!")  # Выводим сообщение, если граф пустой
            return
        else:
            print("Граф не пустой, загружаем данные...")
            for node1, neighbors in self.graph.items():
                for node2, weight in neighbors.items():
                    G.add_edge(node1, node2, weight=weight)

        # Рисуем граф с использованием matplotlib
        try:
            plt.figure(figsize=(4, 2))  # Размер картинки
            pos = nx.spring_layout(G)  # Выбор макета для отображения
            nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")

            # Определяем путь для сохранения изображения в папке проекта
            image_dir = ".../Algorithm/images"  # Укажите свой путь к файлу
            os.makedirs(image_dir, exist_ok=True)
            image_path = os.path.join(image_dir, f"graph_{int(time.time())}.png")

            # Сохраняем граф в файл
            plt.savefig(image_path, format='png')
            self.graph_image_path = image_path
            print(f"Изображение графа сохранено в: {self.graph_image_path}")

            # Загружаем изображение из файла в QImage для отображения
            image = QImage()
            if image.load(self.graph_image_path):
                print("Изображение успешно загружено в QImage из файла.")
            else:
                print("Ошибка при загрузке изображения в QImage из файла.")
                return

            pixmap = QPixmap(image)
            if pixmap.isNull():
                print("Ошибка: QPixmap пустое!")
                return

            scene = QGraphicsScene()
            scene.addPixmap(pixmap)
            self.ui.graphicsView.setScene(scene)
            self.ui.graphicsView.viewport().update()

            plt.close()

        except Exception as e:
            print(f"Ошибка при рисовании и сохранении графа: {e}")
            return


    def handle_manual_input(self):
        """Загрузка данных вручную через таблицу"""
        self.graph = {}
        for row in range(self.ui.tableWidget.rowCount()):
            node1_item = self.ui.tableWidget.item(row, 0)
            node2_item = self.ui.tableWidget.item(row, 1)
            weight_item = self.ui.tableWidget.item(row, 2)

            if node1_item and node2_item and weight_item:
                node1 = node1_item.text()
                node2 = node2_item.text()
                try:
                    weight = float(weight_item.text())
                except ValueError:
                    self.show_error(f"Ошибка в значении веса в строке {row + 1}")
                    return

                if node1 not in self.graph:
                    self.graph[node1] = {}
                self.graph[node1][node2] = weight
                if not self.directed:
                    if node2 not in self.graph:
                        self.graph[node2] = {}
                    self.graph[node2][node1] = weight
            elif any([node1_item, node2_item, weight_item]):
                self.show_error(f"Ошибка: не все поля заполнены в строке {row + 1}")
                return

        print("Граф после ручного ввода:", self.graph)
        self.load_graph_image()


    def update_result_table(self, result):
        """Обновление таблицы с результатами на странице result"""
        table = self.parent.ui.stackedWidget.widget(4).findChild(QTableWidget, "tableWidget_2")
        report_data_from_table = []

        if table:
            print(f"Данные: {report_data_from_table}")
            table.clearContents()
            table.setRowCount(0)

            if self.task_type == "tsp":
                path, length = result
                if not path: # Проверяем, является ли путь пустым (что означает, что маршрут не найден)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Icon.Warning)
                    msg.setText("В заданном графе не найден гамильтонов цикл.")
                    msg.setWindowTitle("Результат")
                    # Создаём палитру для диалогового окна
                    dark_palette = QPalette()
                    dark_palette.setColor(QPalette.ColorRole.Window, QColor("#2b2b2b"))
                    dark_palette.setColor(QPalette.ColorRole.WindowText, QColor("white"))
                    dark_palette.setColor(QPalette.ColorRole.Button, QColor("#3c3c3c"))
                    dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor("white"))
                    msg.setPalette(dark_palette)
                    msg.exec()
                    # Можно также очистить поля пути и длины в таблице или отобразить специальное сообщение
                    table.setRowCount(1)
                    table.setItem(0, 0, QTableWidgetItem("Не найден"))
                    table.setItem(0, 1, QTableWidgetItem("∞"))
                    table.setItem(0, 2, QTableWidgetItem(str(self.time_taken)))
                    report_data_from_table.append({"Путь": "Не найден", "Длина": "∞", "Время": str(self.time_taken)})
                else:
                    table.setRowCount(1)
                    table.setItem(0, 0, QTableWidgetItem(' -> '.join(path)))
                    table.setItem(0, 1, QTableWidgetItem(str(length)))
                    table.setItem(0, 2, QTableWidgetItem(str(self.time_taken)))
                    report_data_from_table.append({"Путь": ' -> '.join(path), "Длина": str(length), "Время": str(self.time_taken)})
            elif self.task_type == "dijkstra":
                path, length = result
                table.setRowCount(1)
                table.setItem(0, 0, QTableWidgetItem(' -> '.join(path)))
                table.setItem(0, 1, QTableWidgetItem(str(length)))
                table.setItem(0, 2, QTableWidgetItem(str(self.time_taken)))
                report_data_from_table.append({"Путь": ' -> '.join(path), "Длина": str(length), "Время": str(self.time_taken)})
            
            elif self.task_type == "kruskal":
                mst = result  # список рёбер: [(node1, node2, weight), ...]
                
                if not mst:
                    table.setRowCount(1)
                    table.setItem(0, 0, QTableWidgetItem("Не найден"))
                    table.setItem(0, 1, QTableWidgetItem("∞"))
                    table.setItem(0, 2, QTableWidgetItem(str(self.time_taken)))
                    report_data_from_table.append({"Ребро": "Не найден", "Вес": "∞", "Время": str(self.time_taken)})
                else:
                    edges_str = ' | '.join([f'{u}->{v}({w})' for u, v, w in mst])
                    total_weight = sum(w for _, _, w in mst)

                    table.setRowCount(1)
                    table.setItem(0, 0, QTableWidgetItem(edges_str))
                    table.setItem(0, 1, QTableWidgetItem(str(total_weight)))
                    table.setItem(0, 2, QTableWidgetItem(str(self.time_taken)))

                    report_data_from_table.append({
                        "Рёбра": edges_str,
                        "Общий вес": str(total_weight),
                        "Время": str(self.time_taken)
                    })

            print(f"Данные: {report_data_from_table}")
            self.parent.result.set_report_data(self.graph_image_path, report_data_from_table)
        else:
            print("Ошибка: таблица не найдена на странице результатов.")
            self.parent.result.set_report_data(self.graph_image_path, [])


    def show_error(self, message):
        """Отображение окна с ошибкой"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle("Ошибка")
        # Создаём палитру для интерфейса
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.ColorRole.Window, QColor("#2b2b2b"))  # фон
        dark_palette.setColor(QPalette.ColorRole.WindowText, QColor("white"))  # текст
        dark_palette.setColor(QPalette.ColorRole.Button, QColor("#3c3c3c"))  # фон кнопки
        dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor("white"))  # текст кнопки
        msg.setPalette(dark_palette)
        msg.exec()
