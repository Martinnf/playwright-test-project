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


@pytest.mark.parametrize(
    ("link_name", "href_pattern"),
    [
        ("Get started", re.compile(r"/docs/intro/?$")),
        ("Testing documentation", re.compile(r"/docs/intro/?$")),
        (
            "Star microsoft/playwright on GitHub",
            re.compile(r"github\.com/microsoft/playwright/?$"),
        ),
    ],
)
def test_primary_links_have_expected_targets(
    page: Page,
    link_name: str,
    href_pattern: re.Pattern[str],
) -> None:
    """Check each primary homepage link against its expected destination.

    Pytest runs this test once for every link_name and href_pattern pair above.
    On each run, Playwright finds the link by its visible name and verifies that
    the href attribute matches the expected URL pattern without clicking it.
    """

    expect(page.get_by_role("link", name=link_name)).to_have_attribute(
        "href", href_pattern
    )
