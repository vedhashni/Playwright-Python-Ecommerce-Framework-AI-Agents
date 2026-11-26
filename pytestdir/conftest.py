
import pytest

@pytest.fixture(scope = "session")
def globalsession():
    print("globalsession")