from playwright.sync_api import Locator, Page, expect


class DocsIntroPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def installation_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Installation")

    def expect_loaded(self) -> None:
        expect(self.installation_heading).to_be_visible()