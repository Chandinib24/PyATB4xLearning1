#create the booking test case
#verify that booking id is not null
#verify status code


#Request module--request

import pytest #pip install pytest
import allure #pip install allure-pytest
import requests

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.testcase("TMS-456")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url="https://restful-booker.herokuapp.com/booking/1"
    response_Data=requests.get(url)
    print(response_Data.text)
    print(response_Data.json())
    print(response_Data.headers)
    assert response_Data.status_code==200

@allure.title("*** Get request with negative Id  ****")
@allure.description("TC#2-- Verify the Get request with negative ID works. ")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_request_by_nagative_id():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    assert response_data.status_code == 404

@allure.title("*** Get request with Invalid Id  ****")
@allure.description("TC#3-- Verify the Get request invalid ID works. ")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_request_by_invalid_id():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    assert response_data.status_code == 404

@allure.title("*** Get request with non existing Id  ****")
@allure.description("TC#4-- Verify the Get request non existing ID works. ")
@allure.testcase("TC#4")
@pytest.mark.smoke
def test_get_request_by_non_exist_id():
    url = "https://restful-booker.herokuapp.com/booking/3535353"
    response_data = requests.get(url)
    assert response_data.status_code == 402
@allure.title("*** Get request with blank Id  ****")
@allure.description("TC#5-- Verify the Get request blank ID works. ")
@allure.testcase("TC#5")
@pytest.mark.smoke
def test_get_request_by_blank_id():
    url = "https://restful-booker.herokuapp.com/booking/"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 400