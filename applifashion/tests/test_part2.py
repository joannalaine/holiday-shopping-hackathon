import pytest

from applifashion.tests.tests import task_1, task_2, task_3

PAGE = "tlcHackathonDev.html"


@pytest.mark.part2
def test_1(driver, chrome_eyes):
    task_1(driver, PAGE, chrome_eyes)


@pytest.mark.part2
def test_2(driver, chrome_eyes):
    task_2(driver, PAGE, chrome_eyes)


@pytest.mark.part2
def test_3(driver, chrome_eyes):
    task_3(driver, PAGE, chrome_eyes)
