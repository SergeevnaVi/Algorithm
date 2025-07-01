import pytest

# Заглушки для функции авторизации пользователя и администратора
def authorize_user(login, password, db_users):
    """
    Проверка авторизации обычного пользователя.
    Возвращает (успех: bool, сообщение: str, user_id: int или None)
    """
    user = db_users.get(login)
    if not user:
        return False, "Пользователь не найден", None
    if user['password'] != password:
        return False, "Неверный пароль", None
    if user['role'] != 'user':
        return False, "Это не пользователь", None
    return True, "Авторизация прошла успешно", user['id']

def authorize_admin(login, password, db_users):
    """
    Проверка авторизации администратора.
    Возвращает (успех: bool, сообщение: str, admin_id: int или None)
    """
    user = db_users.get(login)
    if not user:
        return False, "Администратор не найден", None
    if user['password'] != password:
        return False, "Неверный пароль", None
    if user['role'] != 'admin':
        return False, "Это не администратор", None
    return True, "Авторизация администратора прошла успешно", user['id']

# Фикстура с тестовыми пользователями и админами
@pytest.fixture
def db_users():
    return {
        "user1": {"id": 1, "password": "userpass", "role": "user"},
        "admin1": {"id": 10, "password": "adminpass", "role": "admin"},
        "user2": {"id": 2, "password": "pass2", "role": "user"},
    }

# Тесты авторизации пользователя (успешные и неуспешные)
@pytest.mark.parametrize("login, password, expected_success, expected_message", [
    ("user1", "userpass", True, "Авторизация прошла успешно"),
    ("user1", "wrongpass", False, "Неверный пароль"),
    ("user_not_exist", "pass", False, "Пользователь не найден"),
    ("admin1", "adminpass", False, "Это не пользователь"),  # админ пытается войти как пользователь
])
def test_authorize_user(db_users, login, password, expected_success, expected_message):
    success, message, user_id = authorize_user(login, password, db_users)
    assert success == expected_success
    assert message == expected_message
    if success:
        assert user_id is not None
    else:
        assert user_id is None

# Тесты авторизации администратора (успешные и неуспешные)
@pytest.mark.parametrize("login, password, expected_success, expected_message", [
    ("admin1", "adminpass", True, "Авторизация администратора прошла успешно"),
    ("admin1", "wrongpass", False, "Неверный пароль"),
    ("admin_not_exist", "pass", False, "Администратор не найден"),
    ("user1", "userpass", False, "Это не администратор"),  # пользователь пытается войти как админ
])
def test_authorize_admin(db_users, login, password, expected_success, expected_message):
    success, message, admin_id = authorize_admin(login, password, db_users)
    assert success == expected_success
    assert message == expected_message
    if success:
        assert admin_id is not None
    else:
        assert admin_id is None
