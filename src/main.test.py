import pytest
from src.main import main


class TestClass:

	obj = {
		"a": {
			"b": {
				"c": "d"
			}
		}
	}
	
	def test_c(self):
		expected_result = "('d',)"
		result = main.get_value(TestClass.obj, "c")
		out, err = self.capfd.readouterr()
		assert '{}'.format(expected_result) in out
		
	def test_b(self):
		expected_result = "({'c':'d'},)"
		result = main.get_value(TestClass.obj, "b")
		out, err = self.capfd.readouterr()
		assert '{}'.format(expected_result) in out
		
	@pytest.fixture(autouse=True)
	def capfd(self, capfd):
		self.capfd = capfd