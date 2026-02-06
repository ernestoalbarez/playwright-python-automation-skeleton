def test_smoke_page_load(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
