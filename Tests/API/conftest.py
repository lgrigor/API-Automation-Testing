import pytest


@pytest.fixture(scope='class', autouse=True)
def class_setup_teardown():
    print('start of class')
    yield
    print('end of class')


@pytest.fixture(scope='function', autouse=True)
def test_setup_teardown():
    print('start of the test')
    yield
    print('end of the test')
