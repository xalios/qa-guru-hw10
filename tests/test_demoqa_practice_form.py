import qa_guru_hw10_tests.data.users as users
from qa_guru_hw10_tests.pages.registration_page import RegistrationPage


def test_filling_form():
    page = RegistrationPage()
    page.open()
    page.register(users.john)
    page.assert_registration(users.john)
