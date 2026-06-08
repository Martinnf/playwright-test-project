import typing

import pytest
from playwright.sync_api import Page
from pytest_html.report_data import ReportData


@pytest.fixture(scope="function", autouse=True)
def goto_homepage(page: Page) -> None:
    page.goto("https://playwright.dev/")



# --- HTML Report Generation ---


def pytest_html_report_title(report: ReportData) -> None:
    report.title = "Test Automation Report"


def pytest_html_results_table_header(cells: list) -> None:
    cells.insert(2, "<th>Description</th>")


def pytest_html_results_table_row(report: object, cells: list) -> None:
    description = getattr(report, "description", "N/A")
    html_description = description.strip().replace("\n", "<br>")

    cells.insert(2, f'<td style="white-space: pre-wrap;">{html_description}</td>')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Function) -> typing.Generator[None, None, None]:
    outcome = yield
    if outcome is not None:
        report = outcome.get_result()
        report.description = str(item.function.__doc__)