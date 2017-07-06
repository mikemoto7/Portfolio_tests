import pytest

@pytest.yield_fixture(scope="function")   # default scope is "function"
def setup():
     # print("Once before every method")
     yield
     # print("Once after every method")

@pytest.yield_fixture(scope="module")
def oneTimeSetup():
     # print("Running one time setUp")
     yield
     # print("Running one time tearDown")




