# content of test_class_demo.py
class TestClassDemoInstance:
    """test are not chained, they are independent"""

    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 0
