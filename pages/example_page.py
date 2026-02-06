from playwright.sync_api import Page

from pages.base_page import BasePage


class ExamplePage(BasePage):
    URL = "https://example.com"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def heading(self):
        return self.locator("h1")

    def open(self) -> None:
        self.goto(self.URL)

    def expect_heading(self, text: str) -> None:
        assert self.heading.text_content() == text
