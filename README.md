# advanced_pytests


Pytest exercises that build upon the basic_pytest repository  
- conftest.py 
    - file tested value declared in fixture across multiple tests in different functions
- parametrization 
    - tested functions and fixture parametrization 
- ran multiple tests in parallel, using 'pytest-xdist' plugin 


Explored several options for customizing a test run: 
- stopped test suite after a certain number of test failures
    - '--maxfail=num' option
- running test without specifying the file 
- using pytest -k flag
- skipping and pre-failing tests using xfail and skip decorators 
- running tests based on custom marks