from playwright.sync_api import Page


class BasePage:
    
    URL: str = ""  # Override in subclasses
    
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self) -> None:
        if not self.URL:
            raise NotImplementedError("Subclass must define URL class attribute")
        self.page.goto(self.URL)
    
    @property
    def current_url(self) -> str:
        return self.page.url
    
    @property
    def title(self) -> str:
        return self.page.title()

    
