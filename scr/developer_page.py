from PyQt6.QtWidgets import (QWidget, QMessageBox, QFileDialog, QTableWidgetItem)
from PyQt6.QtCore import pyqtSlot
from scr.algorithms import Algorithm
import csv
import os

class DeveloperPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_app = parent
        self.developer = self.main_app.developer if self.main_app else Developer(1, "admin")
        self.algorithm_names = list(self.developer.algorithms.keys())
        self.algorithm_functions = self.developer.algorithms
        self.save_counters = {}

         # Получаем доступ к существующим виджетам из UI
        self.comboBox_task_2 = self.main_app.ui.comboBox_task_2
        self.tableWidget_3 = self.main_app.ui.tableWidget_3
        self.add_button = self.main_app.ui.pushButton_add
        self.edit_button = self.main_app.ui.pushButton_edit
        self.testing_button = self.main_app.ui.pushButton_testing

        # Подключаем сигнал кнопки "Добавить"
        self.add_button.clicked.connect(self._save_data_to_csv)
        self.edit_button.clicked.connect(self._load_data_from_csv)
        self.testing_button.clicked.connect(self._test_selected_algorithm)

        # Заполняем ComboBox алгоритмами
        self._populate_algorithms_list()
        for name in self.algorithm_names:
            self.save_counters[name] = 0
        

    def _populate_algorithms_list(self):
        self.comboBox_task_2.clear()
        self.comboBox_task_2.addItem("Выберите алгоритм")
        self.comboBox_task_2.addItems(self.algorithm_names)

    def _load_test_graph_from_csv(self, algorithm_name):
        """Загружает тестовый граф из CSV-файла на основе имени алгоритма."""
        base_dir = "tests_csv"
        os.makedirs(base_dir, exist_ok=True)
        file_path = os.path.join(base_dir, f"{algorithm_name.lower().replace(' ', '_')}_test_graph.csv")

        if not os.path.exists(file_path):
            QMessageBox.warning(self, "Тестирование", f"Файл с тестовым графом '{file_path}' не найден.")
            return None

        graph = {}
        try:
            with open(file_path, 'r', newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    v1 = row.get('Узел 1')
                    v2 = row.get('Узел 2')
                    weight_str = row.get('Вес')
                    if v1 and v2 and weight_str:
                        try:
                            weight = float(weight_str)
                            if v1 not in graph:
                                graph[v1] = {}
                            if v2 not in graph:
                                graph[v2] = {}
                            graph[v1][v2] = weight
                            graph[v2][v1] = weight # Предполагаем неориентированный граф
                        except ValueError:
                            QMessageBox.warning(self, "Ошибка", f"Некорректный вес в файле '{file_path}'.")
                            return None
            return graph
        except FileNotFoundError:
            QMessageBox.critical(self, "Ошибка", f"Файл не найден: {file_path}")
            return None
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при чтении CSV-файла '{file_path}': {e}")
            return None

    def _load_expected_result_from_csv(self, algorithm_name):
        """Загружает ожидаемый результат из CSV-файла, адаптируясь к структуре файла."""
        base_dir = "tests_csv"
        os.makedirs(base_dir, exist_ok=True)
        file_path = os.path.join(base_dir, f"{algorithm_name.lower().replace(' ', '_')}_expected.csv")
        print(f"Попытка загрузить ожидаемый результат из файла: {file_path}")

        if not os.path.exists(file_path):
            QMessageBox.information(self, "Тестирование", f"Файл с ожидаемым результатом '{file_path}' не найден.")
            return {}

        expected_data = {}
        try:
            with open(file_path, 'r', newline='', encoding='windows-1251') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader, None)  # Читаем первую строку как заголовок

                if header and len(header) == 2 and header[0].strip() == 'Тип' and header[1].strip() == 'Значение':
                    # Обработка файла в формате "Тип,Значение" (для TSP)
                    for row in reader:
                        if len(row) == 2:
                            key, value = row
                            expected_data[key.strip()] = value.strip()
                else:
                    # Обработка файла в формате "Вершина,Расстояние" (для Dijkstra)
                    csvfile.seek(0)  # Возвращаемся в начало файла
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if len(row) == 2:
                            key, value = row
                            expected_data[key.strip()] = value.strip()
                        elif len(row) > 0 and algorithm_name == "Кратчайший путь" and 'Начальная вершина' not in expected_data and 'Конечная вершина' not in expected_data:
                            # Попытка прочитать начальную и конечную вершины (если они есть в отдельных строках)
                            if len(row) == 2 and row[0].strip() == 'Начальная вершина':
                                expected_data['Начальная вершина'] = row[1].strip()
                            elif len(row) == 2 and row[0].strip() == 'Конечная вершина':
                                expected_data['Конечная вершина'] = row[1].strip()
                            elif len(row) == 2:
                                expected_data[row[0].strip()] = row[1].strip()
        except FileNotFoundError:
            QMessageBox.critical(self, "Ошибка", f"Файл не найден: {file_path}")
            return {}
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при чтении CSV-файла '{file_path}': {e}")
            return {}
        return expected_data

    def _compare_results(self, algorithm_name, actual_result, expected_data):
        """Сравнивает полученный результат с ожидаемыми данными."""
        if algorithm_name == "Задача коммивояжера":
            if isinstance(actual_result, tuple) and len(actual_result) == 2:
                actual_path_list = actual_result[0]
                actual_cost = actual_result[1]
                expected_path_str = expected_data.get('Путь', '')
                expected_cost_str = expected_data.get('Стоимость', '0.0')

                try:
                    expected_cost = float(expected_cost_str)
                except ValueError:
                    print(f"Предупреждение: Некорректный формат ожидаемой стоимости: {expected_cost_str}")
                    return False

                actual_path_str = '-'.join(actual_path_list)

                return actual_path_str == expected_path_str and abs(actual_cost - expected_cost) < 1e-6
            else:
                print(f"Предупреждение: Неожиданный формат результата для '{algorithm_name}': {actual_result}")
                return False
        elif algorithm_name == "Кратчайший путь":
            if isinstance(actual_result, tuple) and len(actual_result) == 2:
                expected_distance_str = expected_data.get(actual_result[0][-1]) # Берем расстояние до последней вершины в пути
                if expected_distance_str is not None:
                    try:
                        expected_distance = float(expected_distance_str)
                        return abs(actual_result[1] - expected_distance) < 1e-6
                    except ValueError:
                        print(f"Предупреждение: Некорректный формат ожидаемого расстояния: {expected_distance_str}")
                        return False
                else:
                    print(f"Предупреждение: Ожидаемое расстояние не найдено для вершины: {actual_result[0][-1]}")
                    return False
            elif isinstance(actual_result, dict): # Обработка старого формата (если вдруг используется)
                return actual_result == {k: float(v) for k, v in expected_data.items() if k not in ['Начальная вершина', 'Конечная вершина']}
            else:
                print(f"Предупреждение: Неожиданный формат результата для '{algorithm_name}': {actual_result}")
                return False
        elif algorithm_name == "Минимальное остовное дерево":
            if isinstance(actual_result, list):
                expected_edges = set()
                expected_weight = 0.0

                # Извлекаем ожидаемые ребра и вес из словаря expected_data
                for key, value in expected_data.items():
                    if key == 'Ребро':
                        pass # Заголовок, пропускаем
                    elif '-' in key:
                        u, v = sorted(key.split('-'))
                        expected_edges.add(tuple((u, v)))
                    elif key == 'Вес':
                        pass # Заголовок веса, пропускаем
                    elif key == 'Значение':
                        try:
                            expected_weight = float(value)
                        except ValueError:
                            print(f"Предупреждение: Некорректный формат ожидаемого веса: {value}")
                            return False

                actual_edges = set()
                actual_weight = 0
                for u, v, weight in actual_result:
                    actual_edges.add(tuple(sorted((u, v))))
                    actual_weight += weight

                return actual_edges == expected_edges and abs(actual_weight - expected_weight) < 1e-6
            else:
                print(f"Предупреждение: Неожиданный формат результата для '{algorithm_name}': {actual_result}")
                return False
        return False

    def _get_start_node_for_test(self, expected_data, test_graph):
        """Получает начальную вершину для теста кратчайшего пути."""
        start_node = expected_data.get('Начальная вершина')
        if start_node and start_node in test_graph:
            return start_node
        elif test_graph:
            return next(iter(test_graph)) # Если не указана или некорректна, берем первую вершину
        return None

    @pyqtSlot()
    def _test_selected_algorithm(self):
        """Запускает тест для выбранного алгоритма."""
        print("Начало тестирования")
        selected_algorithm_name = self.comboBox_task_2.currentText()
        if selected_algorithm_name == "Выберите алгоритм":
            QMessageBox.warning(self, "Внимание", "Пожалуйста, выберите алгоритм для тестирования.")
            return

        # Загружаем тестовый граф
        test_graph = self._load_test_graph_from_csv(selected_algorithm_name)
        if test_graph is None:
            print("Ошибка: Не удалось загрузить тестовый граф.")
            return

        # Получаем функцию алгоритма
        algorithm_function = self.algorithm_functions.get(selected_algorithm_name)
        if algorithm_function is None:
            QMessageBox.critical(self, "Ошибка", f"Алгоритм '{selected_algorithm_name}' не найден.")
            return

        actual_result = None
        expected_data = self._load_expected_result_from_csv(selected_algorithm_name) # Загружаем ожидаемые данные как обычно

        try:
            if selected_algorithm_name == "Задача коммивояжера":
                actual_result = algorithm_function(test_graph)
                print(f"Результат работы алгоритма (TSP): {actual_result}")
                if not isinstance(actual_result, tuple) or len(actual_result) != 2:
                    print(f"Ошибка: Неожиданный формат результата TSP: {actual_result}")
                    return
            elif selected_algorithm_name == "Кратчайший путь":
                start_node = expected_data.get('Начальная вершина')
                end_node = expected_data.get('Конечная вершина')
                print(f"Загруженные expected_data (Dijkstra): {expected_data}")
                print(f"Определенная начальная вершина (Dijkstra): {start_node}")
                print(f"Определенная конечная вершина (Dijkstra): {end_node}")

                if start_node and end_node and start_node in test_graph and end_node in test_graph:
                    actual_result = algorithm_function(test_graph, start_node, end_node)
                    print(f"Результат работы алгоритма (Dijkstra): {actual_result}")
                    if actual_result is not None and isinstance(actual_result, tuple) and len(actual_result) == 2:
                        actual_result_path, actual_result_distance = actual_result
                    else:
                        QMessageBox.critical(self, "Тестирование", f"Тест для '{selected_algorithm_name}' не пройден. Ожидался кортеж (путь, расстояние), получено: {actual_result}")
                        return
                else:
                    message = "Не удалось определить начальную и/или конечную вершину для теста 'Кратчайший путь'."
                    if not start_node:
                        message += " Начальная вершина не указана."
                    elif start_node not in test_graph:
                        message += f" Начальная вершина '{start_node}' отсутствует в графе."
                    if not end_node:
                        message += " Конечная вершина не указана."
                    elif end_node not in test_graph:
                        message += f" Конечная вершина '{end_node}' отсутствует в графе."
                    QMessageBox.warning(self, "Внимание", message)
                    return
            elif selected_algorithm_name == "Минимальное остовное дерево":
                actual_result = algorithm_function(test_graph) # Передаем test_graph напрямую
                print(f"Результат работы алгоритма (Kruskal): {actual_result}")
                if not isinstance(actual_result, list) or (actual_result and not isinstance(actual_result[0], tuple) and len(actual_result[0]) != 3):
                    print(f"Ошибка: Неожиданный формат результата Kruskal: {actual_result}")
                    return
            else:
                QMessageBox.warning(self, "Внимание", f"Не реализовано тестирование для '{selected_algorithm_name}'.")
                return
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при выполнении алгоритма '{selected_algorithm_name}': {e}")
            return

        # Сравниваем результаты (универсальная часть)
        print(f"Значение actual_result перед вызовом _compare_results: {actual_result}")
        if expected_data:
            test_passed = self._compare_results(selected_algorithm_name, actual_result, expected_data)
            expected_output_str = f"Ожидалось: {expected_data}"
            actual_output_str = f"Получено: {actual_result}"
            if test_passed:
                QMessageBox.information(self, "Тестирование", f"Тест для '{selected_algorithm_name}' пройден успешно!\n{actual_output_str}\n{expected_output_str}")
            else:
                QMessageBox.critical(self, "Тестирование", f"Тест для '{selected_algorithm_name}' не пройден.\n{actual_output_str}\n{expected_output_str}")
        else:
            QMessageBox.warning(self, "Тестирование", "Не удалось загрузить ожидаемый результат.")

    @pyqtSlot()
    def _save_data_to_csv(self):
        selected_algorithm_name = self.comboBox_task_2.currentText()
        if selected_algorithm_name == "Выберите алгоритм":
            QMessageBox.warning(self, "Внимание", "Пожалуйста, выберите алгоритм.")
            return

        # Увеличиваем счетчик для выбранного алгоритма
        self.save_counters[selected_algorithm_name] += 1
        file_number = self.save_counters[selected_algorithm_name]
        default_file_name = f"{selected_algorithm_name}_data_{file_number}.csv"
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Сохранить данные как CSV", default_file_name, "CSV (*.csv)")
        
        if file_path:
            with open(file_path, 'w', newline='', encoding='windows-1251') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["Узел 1", "Узел 2", "Вес"])

                for row in range(self.tableWidget_3.rowCount()):
                    v1_item = self.tableWidget_3.item(row, 0)
                    v2_item = self.tableWidget_3.item(row, 1)
                    weight_item = self.tableWidget_3.item(row, 2)

                    if v1_item and v2_item and weight_item:
                        v1 = v1_item.text()
                        v2 = v2_item.text()
                        weight = weight_item.text()
                        csv_writer.writerow([v1, v2, weight])
                    elif any([v1_item, v2_item, weight_item]):
                        QMessageBox.warning(self, "Предупреждение", f"Строка {row + 1} заполнена не полностью и будет пропущена.")

        QMessageBox.information(self, "Успех", f"Данные для '{selected_algorithm_name}' успешно сохранены в '{file_path}'.")

    @pyqtSlot()
    def _load_data_from_csv(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Открыть CSV файл", "", "CSV (*.csv)")

        if file_path:
            try:
                with open(file_path, 'r', newline='', encoding='windows-1251') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    header = next(csv_reader, None)
                    if header == ["Узел 1", "Узел 2", "Вес"]:
                        self.tableWidget_3.setRowCount(0)
                        for row_data in csv_reader:
                            if len(row_data) == 3:
                                row = self.tableWidget_3.rowCount()
                                self.tableWidget_3.insertRow(row)
                                for col, value in enumerate(row_data):
                                    item = QTableWidgetItem(value)
                                    self.tableWidget_3.setItem(row, col, item)
                            else:
                                QMessageBox.warning(self, "Ошибка", f"Некорректный формат строки в файле: {row_data}")
                    elif header:
                        QMessageBox.warning(self, "Ошибка", "Некорректный заголовок CSV файла. Ожидается: 'Узел 1', 'Узел 2', 'Вес'.")
                    else:
                        QMessageBox.warning(self, "Ошибка", "Файл CSV пуст или не содержит заголовка.")
            except FileNotFoundError:
                QMessageBox.critical(self, "Ошибка", f"Файл не найден: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при чтении файла: {e}")

class Developer:
    def __init__(self, developer_id: int, name: str):
        self.developer_id = developer_id
        self.name = name
        self.algorithms = {}
        self.load_algorithms()
        self.current_graph_data = []

    def load_algorithms(self):
        """Загружает доступные алгоритмы."""
        self.algorithms["Задача коммивояжера"] = Algorithm.tsp
        self.algorithms["Кратчайший путь"] = Algorithm.dijkstra
        self.algorithms["Минимальное остовное дерево"] = Algorithm.kruskal

    def get_available_algorithms(self):
        return list(self.algorithms.keys())