# 2. Створити класс з властивостями, що задаються при ініцілізації:
# - Параметр login(str). Значення за замовчування - порожня строка.
# - Параметр password(str). Значення за замовчуванням - порожня строка.
# - Метод sign_in_enabled.  Який повертає True, якщо логін і пароль заповнені і False, якщо хоча б одне з полів пусте
import logging

import pytest


class LoginForm:

    # Задаємо значення за замовчуванням при інінціалізації
    def __init__(self, login="", password=""):
        self.login = login
        self.password = password

    # Метод sign_in_enabled. Який повертає True, якщо логін і пароль заповнені і False, якщо хоча б одне з полів пусте
    def sign_in_enabled(self):
        return bool(self.login) and bool(self.password)


# А також створити:
# - Фікстуру рівня классу, що буде створювати обʼєкт та передавати його в тест
# - Фікстури рівня функції, що буду заповнювати поля

@pytest.fixture(scope="class")
def login_form():
    print("Before")
    yield LoginForm()
    print("After")


@pytest.fixture(scope="function")
def set_password(login_form):
    login_form.password = "SomPwd"
    yield
    login_form.password = ""


@pytest.fixture(scope="function")
def set_login(login_form):
    login_form.login = "SomLogin"
    yield
    login_form.login = ""


@pytest.fixture(scope="function")
def fill_form(login_form):
    login_form.login = "SomLogin"
    login_form.password = "SomPwd"
    yield
    login_form.login = ""
    login_form.password = ""


# Написати тести:
# - 2 поля пусті, тож sign_in_enabled -> False
class TestLoginForm:
    log = logging.getLogger("[TestLog]")

    def test_default(self, login_form):
        """
        - Pre-conditions:
            - Create object without login and password
        - Steps:
            - Verify "button" state
        """
        # Перевіряємо стан
        assert not login_form.sign_in_enabled(), f"Actual value: {login_form.sign_in_enabled()}"  # == False

        # Виводимо меседж
        self.log.info("За замовчуванням кнопка не доступна")

    # - 1 поле заповнене, тож sign_in_enabled -> False
    def test_set_only_password(self, login_form, set_password):
        """
        - Pre-conditions:
            - Create object with password only
        - Steps:
            - Verify "button" state
        """
        # Перевіряємо стан
        assert login_form.password
        assert not login_form.sign_in_enabled(), f"Actual value: {login_form.sign_in_enabled()}"  # == False

        # Виводимо меседж
        self.log.info("Копна не доступна коли заповнене лише одне поле")

    @pytest.mark.smoke
    def test_set_only_login(self, login_form, set_login):
        """
        - Pre-conditions:
            - Create object with login only
        - Steps:
            - Verify "button" state
        """
        # Перевіряємо стан
        assert not login_form.sign_in_enabled(), f"Actual value: {login_form.sign_in_enabled()}"  # == False

        # Виводимо меседж
        self.log.info("Копна не доступна коли заповнене лише одне поле")

    # - 2 поля заповнені, тож sign_in_enabled ->True. А якщо замінити одне зі значень на None або порожню строку, то sign_in_enabled -> False.
    def test_fill_all(self, login_form, fill_form):
        """
        - Pre-conditions:
            - Create object with login and password
        - Steps:
            - Verify "button" state
            - Clear password
            - Verify "button" state
        """
        # Перевіряємо стан
        assert login_form.sign_in_enabled(), f"Actual value: {login_form.sign_in_enabled()}"  # == True

        # Виводимо меседж
        self.log.info("Кнопка доступна при заповненні всіх полів")

        # Чистимо пароль
        login_form.password = ""

        # Перевіряємо стан
        assert not login_form.sign_in_enabled(), f"Actual value: {login_form.sign_in_enabled()}"  # == False

        # Виводимо меседж
        self.log.info("Кнопка не доступна після очистки одного з полів")


@pytest.mark.smoke
def test_set_only_login(login_form, set_login):
    """
    - Pre-conditions:
        - Create object with login only
    - Steps:
        - Verify "button" state
    """
    print(login_form)
    print(id(login_form))
    # Перевіряємо стан
    assert not login_form.sign_in_enabled(), f"Actual value: {login_form.sign_in_enabled()}"  # == False


def test_fill_all(login_form, fill_form):
    """
    - Pre-conditions:
        - Create object with login and password
    - Steps:
        - Verify "button" state
        - Clear password
        - Verify "button" state
    """
    print(login_form)
    print(id(login_form))
    # Перевіряємо стан
    assert login_form.sign_in_enabled(), f"Actual value: {login_form.sign_in_enabled()}"  # == True

    # Чистимо пароль
    login_form.password = ""

    # Перевіряємо стан
    assert not login_form.sign_in_enabled(), f"Actual value: {login_form.sign_in_enabled()}"  # == False
