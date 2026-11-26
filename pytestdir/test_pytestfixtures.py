import pytest

#module scope
@pytest.fixture(scope = "module")
def modulecheck():
    print("Hello world")

def test_initial(modulecheck):
    print("Initial")

@pytest.mark.smoke # it groups testcases with a tag name eg:smoke
def test_second(modulecheck):
    print("Second")

#function scope
@pytest.fixture(scope = "function")
def functioncheck():
    print("Function test")
    return "pass"

#yield keyword is used for setup and teardown process concept,
# where it pauses the execution and retain the execution atlast
@pytest.fixture(scope = "function")
def demo():
    print("Demo")
    yield #pause
    print("Demo1")

@pytest.mark.smoke
def test_func1(functioncheck,demo):
    print("Func1")
    assert functioncheck == "pass"

# skip keyword is used  to skip specific testcase
@pytest.mark.skip
def test_func2(functioncheck):
    print("Func2")


#session scope through conftest file
def test_session1(globalsession):
    print("Session1")