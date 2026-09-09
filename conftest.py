import pytest  # Импортируем pytest
from playwright.sync_api import sync_playwright, \
    Page  # Имопртируем класс страницы, будем использовать его для аннотации типов

pytest_plugins = [
    "fixtures.browsers",
    "fixtures.pages",
]
