import pytest
import allure

@pytest.mark.smoke
@allure.title("TC#1-Verify that 2-2 is equal 0")
@allure.description("This is a smoke test case which verifies 2-2 is equal 0")

def test_sub():
    assert 2-2==0


@pytest.mark.smoke
@allure.title("TC#2-Verify that 10+1 is equal 11")
@allure.description("This is a smoke test case which verifies 10+1 is equal 11")
def test_add():
    assert 10+1==11

@pytest.mark.smoke
@allure.title("TC#3-Verify that 10*1 is equal 11")
@allure.description("This is a smoke test case which verifies 10*1 is equal 11")
def test_mul():
    assert 10*1==11

@pytest.mark.skip
@allure.title("TC#4-Verify that 26+31 is equal 57")
@allure.description("This is a smoke test case which verifies 26+31 is equal 57")
def test_add():
    assert 26+31==57