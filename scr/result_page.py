from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox, QTableWidget
from PyQt6.QtCore import pyqtSlot
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class ResultPage(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.graph_image_path = None
        self.report_data = []
        self.other_algorithm_data = None

    def set_report_data(self, graph_image_path, report_data):
        self.graph_image_path = graph_image_path
        self.report_data = report_data

    def get_report_data_from_table(self):
        """Извлекает данные 'Путь', 'Длина', 'Время' из таблицы результатов."""
        table = self.ui.stackedWidget.widget(4).findChild(QTableWidget, "tableWidget_2")
        table_data = []
        if table and table.rowCount() > 0:
            headers = [table.horizontalHeaderItem(i).text() for i in range(table.columnCount())]
            path_col = headers.index('Путь') if 'Путь' in headers else -1
            length_col = headers.index('Длина') if 'Длина' in headers else -1
            time_col = headers.index('Время') if 'Время' in headers else -1

            for row in range(table.rowCount()):
                row_data = {}
                if path_col != -1 and table.item(row, path_col) is not None:
                    row_data['Путь'] = table.item(row, path_col).text()
                if length_col != -1 and table.item(row, length_col) is not None:
                    try:
                        row_data['result_length'] = float(table.item(row, length_col).text())
                    except ValueError:
                        print(f"Предупреждение: Не удалось преобразовать длину в float в строке {row + 1}")
                if time_col != -1 and table.item(row, time_col) is not None:
                    try:
                        row_data['execution_time'] = float(table.item(row, time_col).text())
                    except ValueError:
                        print(f"Предупреждение: Не удалось преобразовать время в float в строке {row + 1}")
                if row_data:
                    table_data.append(row_data)
        return table_data

    def compare_with_other_algorithm(self):
        current_algorithm_data = self.get_report_data_from_table() # Используем данные из таблицы
        print(f"Данные текущего алгоритма перед сравнением: {current_algorithm_data}")

        other_algorithm_data = self.get_other_algorithm_data()
        print(f"Данные другого алгоритма после загрузки: {other_algorithm_data}")

        if not current_algorithm_data:
            QMessageBox.warning(self.ui.stackedWidget.widget(4), "Внимание",
                                "Нет данных текущего алгоритма для сравнения.")
            return

        if not other_algorithm_data:
            QMessageBox.warning(self.ui.stackedWidget.widget(4), "Внимание",
                                "Не удалось получить данные другого алгоритма для сравнения.")
            return

        comparison_result = self.compare_algorithms(current_algorithm_data, other_algorithm_data)
        self.display_comparison_results(comparison_result)

    def get_other_algorithm_data(self):
        """
        Открывает диалоговое окно для выбора файла с данными другого алгоритма.
        Возвращает данные из выбранного файла в формате списка словарей (с ключами
        'result_length' и 'execution_time') или None в случае ошибки.
        """
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self.ui.stackedWidget.widget(4),
            "Выберите файл с данными другого алгоритма",
            "",
            "CSV файлы (*.csv);;Все файлы (*)"
        )

        if file_path:
            try:
                with open(file_path, 'r', encoding='windows-1251') as f:
                    lines = f.readlines()
                    if len(lines) < 2:
                        QMessageBox.warning(self.ui.stackedWidget.widget(4), "Внимание",
                                            "Файл данных другого алгоритма пуст или содержит недостаточно строк.")
                        return None

                    header_string = lines[0].strip()
                    headers = [header.strip() for header in header_string.split(',')]

                    # Поддержка расширенного формата: Путь, Длина, Время
                    path_idx = headers.index('Путь') if 'Путь' in headers else None
                    len_idx = headers.index('Длина') if 'Длина' in headers else None
                    time_idx = headers.index('Время') if 'Время' in headers else None

                    results = []
                    for i, line in enumerate(lines[1:], start=2):
                        values = [v.strip() for v in line.strip().split(',')]
                        row = {}
                        if path_idx is not None and len(values) > path_idx:
                            row['Путь'] = values[path_idx]
                        if len_idx is not None and len(values) > len_idx:
                            try:
                                row['result_length'] = float(values[len_idx])
                            except ValueError:
                                print(f"Ошибка преобразования длины на строке {i}")
                        if time_idx is not None and len(values) > time_idx:
                            try:
                                row['execution_time'] = float(values[time_idx])
                            except ValueError:
                                print(f"Ошибка преобразования времени на строке {i}")
                        if row:
                            results.append(row)

                    return results if results else None
            
            except Exception as e:
                print(f"Ошибка при чтении файла другого алгоритма: {e}")
                QMessageBox.critical(self.ui.stackedWidget.widget(4), "Ошибка",
                                         f"Произошла ошибка при чтении выбранного файла: {e}")
                return None
        else:
            return None

    def compare_algorithms(self, current_data, other_data):
        """
        Сравнивает время выполнения и длину результатов двух алгоритмов.
        """
        if not current_data or not other_data:
            return "Нет данных для сравнения."

        current_algorithm_info = current_data[0] if current_data else {}
        other_algorithm_info = other_data[0] if other_data else {}

        current_time = current_algorithm_info.get('execution_time')
        other_time = other_algorithm_info.get('execution_time')
        current_length = current_algorithm_info.get('result_length')
        other_length = other_algorithm_info.get('result_length')
        current_algorithm_name = current_algorithm_info.get('algorithm_name', 'Текущий алгоритм')
        other_algorithm_name = other_algorithm_info.get('algorithm_name', 'Другой алгоритм')

        comparison_results = {}

        if current_time is not None and other_time is not None:
            time_difference = other_time - current_time
            comparison_results[f"Время выполнения ({current_algorithm_name})"] = f"{current_time:.4f} сек." if isinstance(current_time, (int, float)) else str(current_time)
            comparison_results[f"Время выполнения ({other_algorithm_name})"] = f"{other_time:.4f} сек." if isinstance(other_time, (int, float)) else str(other_time)
            comparison_results["Разница во времени"] = f"{time_difference:.4f} сек." if isinstance(time_difference, (int, float)) else "Нет данных"
        else:
            comparison_results["Время выполнения"] = "Нет данных для сравнения времени."

        if current_length is not None and other_length is not None:
            length_difference = other_length - current_length
            comparison_results[f"Длина результата ({current_algorithm_name})"] = current_length
            comparison_results[f"Длина результата ({other_algorithm_name})"] = other_length
            comparison_results["Разница в длине"] = length_difference
        else:
            comparison_results["Длина результата"] = "Нет данных для сравнения длины."

        return {"Сравнение алгоритмов": comparison_results}

    def display_comparison_results(self, results):
        """
        Выводит результаты сравнения времени и длины в QMessageBox.
        """
        if isinstance(results, str):
            QMessageBox.information(self.ui.stackedWidget.widget(4), "Результаты сравнения", results)
            return

        message = "Результаты сравнения алгоритмов:\n"
        if "Сравнение алгоритмов" in results:
            for key, value in results["Сравнение алгоритмов"].items():
                message += f"  {key}: {value}\n"
        else:
            message = "Нет данных для сравнения."

        QMessageBox.information(self.ui.stackedWidget.widget(4), "Результаты сравнения", message)


    @pyqtSlot()
    def download_report(self):
        options = QFileDialog.Option(0)
        options |= QFileDialog.Option.DontUseNativeDialog
        formats = "PDF (*.pdf);;CSV (*.csv)"
        selected_filter = ""
        file_name, selected_filter = QFileDialog.getSaveFileName(
            self.ui.stackedWidget.widget(4),
            "Сохранить отчет",
            "",
            formats,
            initialFilter=selected_filter,
            options=options
        )

        if file_name:
            if selected_filter == "PDF (*.pdf)" and not file_name.lower().endswith(".pdf"):
                file_name += ".pdf"
            elif selected_filter == "CSV (*.csv)" and not file_name.lower().endswith(".csv"):
                file_name += ".csv"

            if file_name.lower().endswith(".pdf"):
                self.generate_pdf_report(file_name)
            elif file_name.lower().endswith(".csv"):
                self.generate_csv_report(file_name)
            else:
                QMessageBox.warning(self.ui.stackedWidget.widget(4), "Ошибка",
                                    "Неподдерживаемый формат файла.")

    def generate_csv_report(self, file_path):
        if not self.report_data:
            QMessageBox.warning(self.ui.stackedWidget.widget(4), "Внимание",
                                "Нет данных для сохранения в CSV.")
            return
        try:
            df = pd.DataFrame(self.report_data)
            df.to_csv(file_path, index=False, encoding='windows-1251')
            QMessageBox.information(self.ui.stackedWidget.widget(4), "Успех",
                                    f"Отчет успешно сохранен в {file_path}")
        except Exception as e:
            QMessageBox.critical(self.ui.stackedWidget.widget(4), "Ошибка",
                                 f"Произошла ошибка при сохранении CSV: {e}")

    def generate_pdf_report(self, file_path):
        pdfmetrics.registerFont(TTFont('ArialUnicodeMS', 'arial unicode ms.otf'))

        doc = SimpleDocTemplate(file_path, pagesize=letter)
        elements = []
        styles = getSampleStyleSheet()
        normal_style = styles['Normal']
        normal_style.fontName = 'ArialUnicodeMS'
        h1_style = styles['h1']
        h1_style.fontName = 'ArialUnicodeMS'

        elements.append(Paragraph("Отчет о работе алгоритма", h1_style))
        elements.append(Spacer(1, 12))

        if self.graph_image_path:
            try:
                img = ImageReader(self.graph_image_path)
                img_width, img_height = img.getSize()
                available_width = letter[0] - 2 * 72
                aspect_ratio = img_height / float(img_width)
                scaled_width = min(available_width, img_width)
                scaled_height = scaled_width * aspect_ratio
                from reportlab.platypus import Image

                img_reportlab = Image(self.graph_image_path, width=scaled_width, height=scaled_height)
                elements.append(img_reportlab)
                elements.append(Spacer(1, 12))
            except FileNotFoundError:
                elements.append(Paragraph("Изображение графа не найдено.", normal_style))
                elements.append(Spacer(1, 12))
            except Exception as e:
                elements.append(Paragraph(f"Ошибка при добавлении изображения графа: {e}", normal_style))
                elements.append(Spacer(1, 12))
        else:
            elements.append(Paragraph("Изображение графа отсутствует.", normal_style))
            elements.append(Spacer(1, 12))

        if self.report_data:
            headers = list(self.report_data[0].keys())
            table_data = [headers] + [list(item.values()) for item in self.report_data]
            table_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'ArialUnicodeMS'),  # Заголовок таблицы
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTNAME', (0, 1), (-1, -1), 'ArialUnicodeMS'),  # Данные таблицы
            ])
            table = Table(table_data)
            table.setStyle(table_style)
            elements.append(table)
        else:
            elements.append(Paragraph("Нет табличных данных для отчета.", normal_style))

        try:
            doc.build(elements)
            QMessageBox.information(self.ui.stackedWidget.widget(4), "Успех",
                                    f"Отчет успешно сохранен в {file_path}")
        except Exception as e:
            QMessageBox.critical(self.ui.stackedWidget.widget(4), "Ошибка",
                                 f"Произошла ошибка при создании PDF: {e}")
            

