import pytest

from Portfolio import Portfolio

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestPortfolio():

    # @pytest.fixture(autouse=True)
    # def classSetup(self, oneTimeSetUp):
    #     self.abc = SomeClassToTest(self.value)

    def test_runstring_1(self):
        result = run_command("  ")
        assert result == expected
