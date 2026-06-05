import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function", autouse=True)
def goto_homepage(page: Page) -> None:
    page.goto("https://playwright.dev/")