# Learning Objective: conftest.py practice and parametrizing test fixtures


import pytest 


@pytest.fixture
def input_value():
    input=10
    return input