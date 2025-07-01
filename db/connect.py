import bcrypt
import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="your_host",
            database="graph",
            user="your_user",
            password="your_psw"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None
    

def check_user(login, password):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM registration_user WHERE login = %s"
        cursor.execute(query, (login,))
        user_list = cursor.fetchall()
        user = user_list[0] if user_list else None

        cursor.close()
        connection.close()

        if user:
            if bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
                return user['id']
        return None
    return None

def create_user(name, login, password, phone):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        query = "INSERT INTO registration_user (name, login, password, phone) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (name, login, hashed_password, phone))
            connection.commit()
            cursor.close()
            connection.close()
            return True, None
        except mysql.connector.errors.IntegrityError as e:
            if "Duplicate entry" in str(e):
                if "login" in str(e):
                    return False, "Этот логин уже зарегистрирован"
                elif "phone" in str(e):
                    return False, "Этот номер телефона уже зарегистрирован"
            return False, "Произошла ошибка при регистрации пользователя"
        finally:
            cursor.close()
            connection.close()
    return False, "Не удалось подключиться к базе данных"

def check_admin(login, password):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM auth_admin WHERE login = %s"
        cursor.execute(query, (login,))
        admin = cursor.fetchone()
        connection.close()

        if admin:
            if admin and bcrypt.checkpw(password.encode("utf-8"), admin["password"].encode("utf-8")):
                return admin
            return None
    return None