from playwright.sync_api import expect

class BasePage:

    def __init__(self, page):
        self.page = page
        self.name_field = page.get_by_test_id("ContactName")
        self.email_field = page.get_by_test_id("ContactEmail")
        self.phone_field = page.get_by_test_id("ContactPhone")
        self.subject_field = page.get_by_test_id("ContactSubject")
        self.message_field = page.get_by_test_id("ContactDescription")
        self.submit_button = page.get_by_role("button", name="Submit")

    def base_page_check(self):
        expect(self.page).to_have_url("https://automation.testathon.hu/")

    def open_base_page(self):
        self.page.goto("https://automation.testathon.hu/")
        self.base_page_check()

    def fill_name(self, keyword):
        self.name_field.click()
        self.name_field.fill(keyword)

    def fill_email(self, keyword):
        self.email_field.click()
        self.email_field.fill(keyword)

    def fill_phone(self, keyword):
        self.phone_field.click()
        self.phone_field.fill(keyword)

    def fill_subject(self, keyword):
        self.subject_field.click()
        self.subject_field.fill(keyword)

    def fill_message(self, keyword):
        self.message_field.click()
        self.message_field.fill(keyword)

    def fill_submit(self, keyword):
        self.submit_button.click()
        self.submit_button.fill(keyword)

    def click_submit(self):
        self.submit_button.click()

