# API тесты Stellar Burgers

Автотесты для проверки API сервиса Stellar Burgers на pytest + requests с отчётом Allure.

## Что сделано

- Тесты покрывают регистрацию, логин, изменение данных пользователя, создание и получение заказов  
- Использованы фикстуры для создания и автоматической очистки тестовых пользователей  
- Проверяются и статус-коды, и содержимое ответа (success, message, ключевые поля)  
- Тексты ошибок вынесены в константы для единообразия  
- Каждый эндпоинт оформлен в отдельном классе тестов  
- В Allure добавлены title, suite и шаги для читаемого отчёта  

## Запуск

```bash
pip install -r requirements.txt
pytest -v
```
С отчетом Allure

```bash
pytest --alluredir=target/allure-results
allure generate target/allure-results -o target/allure-report --clean
allure open target/allure-report
```