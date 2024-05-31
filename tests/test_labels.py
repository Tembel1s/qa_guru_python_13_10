import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag("web", "smoke")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("В списке имеется задача с названием 'новая Issue'")
    allure.dynamic.link("https://github.com", name="Testing")
    allure.dynamic.description("Хотелось бы чтобы тест прошел")
    allure.dynamic.suite('Issues testing')
    pass


@allure.tag("web", "smoke")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("В списке имеется задача с названием 'новая Issue'")
@allure.link("https://github.com", name="Testing")
@allure.description("Хотелось бы чтобы тест прошел")
@allure.suite('Issues testing')
def test_decorator_labels():
    pass
