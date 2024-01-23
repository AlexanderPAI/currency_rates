# Технические задание

Cоздать "голый" Django проект, который по переходу на страницу /get-current-usd/ будет отображать в json-формате
актуальный курс доллара к рублю (запрос по апи, найти самостоятельно) и показывать 10 последних запросов 
(паузу между запросами курсов должна быть не менее 10 секунд).

# Соискатель:
Петров Александр Иванович

Ссылка на резюме: https://hh.ru/resume/3c099319ff0c68c07f0039ed1f7a524841447a

## Основной стек:

- Django 2.2.28
- Django REST Framework 3.9.4
- gunicorn 21.2.0
- psycopg2-binary 2.9.9
- requests 2.31.0

### Примечания:
1. Django версии 2.2.28 использована сознательно, так как в требованиях к вакансии было указано наличие у соискателя 
опыта разработки на Django 2.x. Соответственно, версия DRF также использована с учетом совместимости версий Django 2.x (в последних версиях DRF - Django 2.x не поддерживается).
2. Автоматически генерируемая страница API DRF по URL, указанному в ТЗ, также используется сознательно, так как использование готового инструмента упрощает и ускоряет разработку.
3. В репозитории приложения используется контейниризация с использованием docker-compose и nginx, но проект при небольших манипуляциях также может быть запущен без Docker'a (см. инструкции по запуску ниже).

## Краткое описание алгоритма работы
1. Пользователь переходит в браузере по URL http://127.0.0.1/get-current-usd, либо направляет `GET`-запрос без каких-либо параметров на данный эндпоинт через любой инстумент запросов (cUrl, Postman, Insomnia и пр.)
2. Приложение направляет `GET`-запрос на открытый API https://openexchangerates.org.
3. Приложение получает актуальный курс доллара США к Российскому рублю.
4. Приложение преобразует полученную информацию в соответствии с ТЗ и возвращает на страницу курс доллара США к Российскому рублю и последние 10 запросов курсов валют в формате `json`.

### Ответ предоставляется в виде:
```json
{
    "request_date": "2024-01-23T17:01:47.440378",
    "currency_code": "USD",
    "target_currency_code": "RUB",
    "rate": 88.573959,
    "recent_requests": [
        {
            "request_date": "2024-01-23T17:01:47.440378",
            "currency_code": "USD",
            "target_currency_code": "RUB",
            "rate": 88.573959
        },
        {
            "request_date": "2024-01-23T17:01:36.453160",
            "currency_code": "USD",
            "target_currency_code": "RUB",
            "rate": 88.573959
        },
```

Описание полей:

`request_date` - дата и время запроса

`currency_code` - базовая валюта (по умолчанию - USD)

`target_currency_code` - целевая валюта (по умолчанию - RUB)

`rate` - курс USD/RUB

`recent_requests` - список последних 10 запросов.

# Запуск приложения
## С использованием docker-compose
В этом случае запущенный проект будет доступен по URL `http:127.0.0.1/get-current-usd/`

**1.** Клорировать репозиторий:
```bash
git clone git@github.com:AlexanderPAI/currency_rates.git
```
**2.** Разместить в каталоге файл переменных окружения `currency_rates/.env`
Для удобства проверки можно просто [скачать](https://disk.yandex.ru/d/duglH_CdZAUAWQ) тестовый `.env` и расместить по указанному пути.

**3.** Из каталога приложения запустить docker-compose:
```bash
cd currency_rates
docker-compose up --build
```
**Примечание**: на машине должен быть установлен Docker; на машинах с ОС Windows должны быть запущены WSL и Docker Desktop.

## Без docker-compose

В этом случае запущенный проект будет доступен по URL `http://127.0.0.1:8000/get-current-usd/` (обязательно с указанием порта)

**1.** Клорировать репозиторий:
```bash
git clone git@github.com:AlexanderPAI/currency_rates.git
```

**2.** Поднять и активировать виртуальное окружение:
```bash
python -m venv venv

# Windows (PowerShell)
venv\Scripts\activate

# Linux
source venv\bit\activate
```

**3.** Обновить менеджер пакетов `pip` и установить зависимости:
```bash
# В активированном виртуальном окружении
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**4.** Разместить в каталоге файл переменных окружения `currency_rates/.env`
Для удобства проверки можно просто [скачать](https://disk.yandex.ru/d/duglH_CdZAUAWQ) тестовый `.env` и расместить по указанному пути.

**5.** [Рекомендуется, но не обязательно] Для упрощения тестирования, чтобы не поднимать базу данных PostgreSQL в соответствии с данными, указанными в `.env`-файле, в настройках проекта Django `currency_rates/settings.py` можно заменить БД на SQLite3:
```python
# Раскомментировать строки:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Закомментировать строки:
# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('POSTGRES_USER'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT')
#     }
# }
```
В ином случае необходимо вручную поднять БД PostgreSQL, исходя из данных в `.env`-файле, а также в `.env`-файле заменить`DB_HOST=db` на `DB_HOST=localhost`.

**6.** Создать и выполнить миграции:
```bash
python currency_rates/manage.py makemigrations
python currency_rates/manage.py migrate --run-syncdb
```

**7.** Запустить Dev-сервер:
```bash
python currency_rates/manage.py runserver
```
