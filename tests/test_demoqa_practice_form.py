from qa_guru_hw10_tests.pages.registration_page import RegistrationPage


def test_filling_form():
    page = RegistrationPage()
    page.open()
    page.fill_name('John', 'Doe')
    page.fill_email('jdoe@test.com')
    page.fill_gender_male()
    page.fill_user_number('9123456789')
    page.fill_date_of_birth('1988', 'May', '31')
    page.fill_subject('Computer science')
    page.fill_hobbies('Sports', 'Music')
    page.upload_picture('avatar.jpg')
    page.fill_address('Москва')
    page.fill_state('NCR')
    page.fill_city('Delhi')
    page.submit()

    # TESTS
    page.assert_registration_success()

    # Checking table size
    page.assert_table_size()

    # Checking values and that they are corresponding row labels
    page.assert_table_values('Student Name', 'John Doe')
    page.assert_table_values('Student Email', 'jdoe@test.com')
    page.assert_table_values('Gender', 'Male')
    page.assert_table_values('Mobile', '9123456789')
    page.assert_table_values('Date of Birth', '31 May,1988')
    page.assert_table_values('Subjects', 'Computer Science')
    page.assert_table_values('Hobbies', 'Sports, Music')
    page.assert_table_values('Picture', 'avatar.jpg')
    page.assert_table_values('Address', 'Москва')
    page.assert_table_values('State and City', 'NCR Delhi')
