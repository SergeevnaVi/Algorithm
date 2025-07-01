# 🧠 Алгоритмы маршрутизации: Коммивояжёр, Дейкстра, Крускал

Интерактивное приложение с графическим интерфейсом для работы с алгоритмами на графах:
- 🔁 Задача Коммивояжёра (TSP)
- 🛣 Алгоритм Дейкстры (поиск кратчайшего пути)
- 🌐 Алгоритм Крускала (минимальное остовное дерево)

## 📌 Возможности

### 👤 Пользователь:
- 🔐 Авторизация
- 📥 Ввод графа вручную или загрузка из файла (таблица смежности)
- ⚙ Запуск алгоритма
- 📊 Просмотр результата на графике и в таблице
- 📁 Экспорт результатов в PDF или CSV
- 📈 Сравнение разных алгоритмов

### 🛠 Администратор:
- 🔧 Добавление/редактирование/тестирование алгоритмов
- 📤 Публикация алгоритмов для пользователей

---

## 🚀 Как запустить
```
git clone git clone https://github.com/SergeevnaVi/Algorithm.git
```
```
cd Algorithm
```
```
pip install -r requirements.txt
```
```
python main.py
```


## 🧱 Технологии

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyQt6](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![bcrypt](https://img.shields.io/badge/bcrypt-%23000000.svg?style=for-the-badge&logo=python&logoColor=white)
![reportlab](https://img.shields.io/badge/reportlab-%23000000.svg?style=for-the-badge&logo=python&logoColor=white)
![csv](https://img.shields.io/badge/csv-%23000000.svg?style=for-the-badge&logo=python&logoColor=white)
![itertools](https://img.shields.io/badge/itertools-%23000000.svg?style=for-the-badge&logo=python&logoColor=white)
![heapq](https://img.shields.io/badge/heapq-%23000000.svg?style=for-the-badge&logo=python&logoColor=white)

## 🗂 Структура проекта
```
├── main.py
├── algorithm.py
├── images/
├── files/
│   └── *.csv
├── test_csv/
│   └── *.csv
├── scr/
│   ├── algorithms.py
│   ├── auth.py
│   ├── developer_page.py
|   ├── loadGraph.py
|   ├── navigation.py
|   ├── result_page.py
├── db/
│   └── connect.py
├── auto_test/
│   ├── test_algorithms.py
│   ├── test_auth.py
├── requirements.txt
├── arial unicode ms.otf
└── README.md

```
## 📥 Пример входных данных
```
("A", "B", 5)
("A", "C", 2)
("B", "C", 1)

- Стартовая вершина: "A"
- Конечная вершина: "C"
- Максимальная длина пути: 6
- Учитывать направленность графа: нет (граф неориентированный)
```
## 🖼 Интерфейс
<details>
<summary> 🔐 Страница авторизации (нажмите, чтобы раскрыть)</summary>
 
[![authorization][1]][1]
 
[1]: readme_assets/authorization.png

▶️ Описание:
Пользователь или администратор вводит логин и пароль для входа в систему. Реализована проверка с использованием хэшей и подключением к базе данных MySQL.
 
</details>

<details>
<summary> 📁 Загрузка графа из файла или с помощью ручного ввода</summary>
 
[![graph_loading][3]][3]
 
[3]: readme_assets/graph_loading.png

▶️ Описание:
Пользователь может загрузить граф из .csv-файла или ввести данные вручную. Учитываются вершины, рёбра и веса, возможна настройка направленности графа.
 
</details>


<details>
<summary> 🧮 Отображение результата алгоритма</summary>
 
[![result][4]][4]
 
[4]: readme_assets/result.png

▶️ Описание:
После выполнения алгоритма (например, Дейкстры, TSP или Крускала) отображается маршрут, его длина, и визуализация графа.

</details>

<details>
<summary> 📊 Сравнение результатов алгоритмов</summary>
 
[![comparison_result][2]][2]
 
[2]: readme_assets/comparison_result.png

▶️ Описание:
После запуска алгоритмов можно сравнить их по длине пути и времени выполнения. Результаты отображаются в таблице.
 
</details>
