import re

from playwright.sync_api import Page, expect


def test_get_started_link_opens_installation_docs(page: Page) -> None:
    """Verify the Get started link opens the installation guide."""

    page.get_by_role("link", name="Get started").click()

    expect(page).to_have_url(re.compile(r"/docs/intro/?$"))
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def test_testing_documentation_link_opens_intro_docs(page: Page) -> None:
    """Verify the Testing documentation link opens the intro docs."""

    page.get_by_role("link", name="Testing documentation").click()

    expect(page).to_have_url(re.compile(r"/docs/intro/?$"))
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()