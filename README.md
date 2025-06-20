# Дипломный проект QA.GURU (API-тестирование)

Данный репозиторий содержит проект - API тестирование для https://reqres.in/api - часть дипломной работы, выполненной в рамках обучения на курсах QA.GURU. Проект разработан с целью продемонстрировать полученные навыки и знания в области тестирования программного обеспечения.

## Используемые инструменты
<div>
<img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" title="python" alt="python" width="40" height="40"/>&nbsp
<img src="https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png" title="pytest" alt="pytest" width="40" height="40"/>&nbsp
<img src="https://img.icons8.com/?size=100&id=3tC9EQumUAuq&format=png&color=000000" title="github" alt="github" width="40" height="40"/>&nbsp
<img src="https://user-images.githubusercontent.com/25181517/179090274-733373ef-3b59-4f28-9ecb-244bea700932.png" title="jenkins" alt="jenkins" width="40" height="40"/>&nbsp
<img src="resources/AllureTestOps.png" width="40" height="40"  alt="Allure TestOps"/> 
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pycharm/pycharm-original.svg" title="pycharm" alt="pycharm" width="40" height="40"/>&nbsp
<img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" title="telegram" alt="telegram" width="40" height="40"/>&nbsp
</div>

## Список автоматизированных тест-кейсов:
1. Проверка успешной регистрации нового пользователя
2. Проверка ошибки при неуспешной регистрации пользователя
3. Проверка успешной авторизации
4. Проверка неуспешной авторизации
5. Проверка получения данных о существующем пользователе
6. Проверка редактирования данных существующего пользователя
7. Проверка удаления существующего пользователя
8. Проверка создания нового пользователя
9. Проверка получения данных о существующем товаре
10. Проверка ошибки при запросе данных о несуществующем товаре

## Запуск тестов и получение отчета

### **Локально**

<details><summary>1. Склонировать репозиторий</summary>

```
git clone https://github.com/SychkovArkadiyQA/QA_GURU_Python_19_api_diplom
```
</details>

<details><summary>2. Установить зависимости и запустить тесты</summary>

```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install
pytest .
```
</details>

<details><summary>3. Получить отчет о прохождении тестов в allure</summary>

```
allure serve tests/allure-results/
```
</details>

<details><summary>4. После выполнения команды откроется браузер с отчетом</summary>
    
<img src="resources/allure_local.png">

</details>

### **Удалённо**

Удаленный запуск автотестов осуществляется при помощи Jenkins. Для этого необходимо выполнить следующие действия:

1. Открыть проект на Jenkins

<details><summary>2. Нажать на Build now</summary>

![img_1.png](img_1.png)
</details>

<details><summary>3. Дождаться окончания выполнения автотестов и нажать на иконку allure для просмотра отчета</summary>

![img_2.png](img_2.png)

</details>

## Отчет в Allure report

<details><summary>Основной отчет</summary>

![img_3.png](img_3.png)

</details>
<details><summary>Тесты</summary>

![img_4.png](img_4.png)

</details>

## <img src="resources/AllureTestOps.png" width="30" height="30"  alt="Allure TestOps"/> Отчет в <a href = "https://allure.autotests.cloud/project/4367/dashboards">Allure TestOps</a>

<details><summary>Основной отчет</summary>

<img src="resources/testOps_base_report.png">

</details>

<details><summary>Тесты</summary>

<img src="resources/testOps_tests.png">

</details>

