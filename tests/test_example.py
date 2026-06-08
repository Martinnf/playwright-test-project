import re
import pytest
from playwright.sync_api import Page, expect

def test_has_title(page: Page) -> None:
    """Verify the homepage title mentions Playwright."""

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_hero_heading_is_visible(page: Page) -> None:
    """Verify the hero heading is visible on the homepage."""

    expect(
        page.get_by_role(
            "heading",
            name=re.compile("Playwright enables reliable web automation"),
        )
    ).to_be_visible()


@pytest.mark.parametrize(
    "section_name",
    ["Built for testing", "Built for AI agents", "Powerful tooling"],
)
def test_core_sections_are_visible(page: Page, section_name: str) -> None:
    """Verify each core homepage section heading is visible."""

    expect(page.get_by_role("heading", name=section_name)).to_be_visible()


