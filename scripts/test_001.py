import pytest,allure,os

# allure generate report/ -o report/outputs
class Test_allur01:
    @allure.step(title="第一个测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_001(self):
        allure.attach("这是一个描述","试一下")
        assert 1

    @allure.issue("http://www.163.com/ll")
    @allure.step(title="第二个测试")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_001(self):
        allure.attach("这是一个描述", "试一下")
        assert 1