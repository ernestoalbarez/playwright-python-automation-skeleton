from playwright.sync_api import Locator, Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, url: str) -> None:
        self.page.goto(url)

    def expect_title(self, title: str) -> None:
        assert self.page.title() == title

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)
