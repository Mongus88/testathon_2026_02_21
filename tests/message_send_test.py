from playwright.sync_api import expect

from pages.base_page import BasePage

def test_message_send(page):

    base_page = BasePage(page)
    base_page.open_base_page()
    base_page.fill_name(keyword="Zsíros B. Ödön")
    base_page.fill_email(keyword="kurta@cthul.hu")
    base_page.fill_phone(keyword="06901234567")
    base_page.fill_subject(keyword="teszt üzenet 01")
    base_page.fill_message(keyword="A teszt üzenetnek minimum 20 karakternek kell lennie.")
    base_page.click_submit()

    expect(page.get_by_text("teszt üzenet 01")).to_be_visible()
