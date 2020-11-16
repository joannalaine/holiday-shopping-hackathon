import pytest

from applifashion.tests.test_tasks import task_1, task_2, task_3


@pytest.mark.parametrize(
    'page',
    [
        pytest.param("tlcHackathonMasterV1.html", marks=pytest.mark.part1),
        pytest.param("tlcHackathonDev.html", marks=pytest.mark.part2)
    ]
)
class TestSingleBrowser:
    def test_1(self, driver, page, chrome_eyes):
        task_1(driver, page, chrome_eyes)

    def test_2(self, driver, page, chrome_eyes):
        task_2(driver, page, chrome_eyes)

    def test_3(self, driver, page, chrome_eyes):
        task_3(driver, page, chrome_eyes)


@pytest.mark.parametrize(
    'page',
    [
        pytest.param("tlcHackathonMasterV2.html", marks=pytest.mark.part3)
    ]
)
class TestMultipleBrowsers:
    def test_1(self, driver, page, cross_browser_eyes):
        task_1(driver, page, cross_browser_eyes)

    def test_2(self, driver, page, cross_browser_eyes):
        task_2(driver, page, cross_browser_eyes)

    def test_3(self, driver, page, cross_browser_eyes):
        task_3(driver, page, cross_browser_eyes)
