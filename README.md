# EIS_PROJECT
[![License MIT](https://img.shields.io/badge/licence-MIT-green)](https://opensource.org/license/mit/)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
# Разработчик проекта: Татьяна Лоскутова
<details> 
  <summary>Описание</summary>
  
1.	Реализовать модели данных «Дом», «Квартира», «Счётчик воды», «Тариф»,
учитывая связи между ними.
В доме может быть много квартир. В квартире может быть несколько счётчиков.
У квартиры должна быть площадь (будет нужно для расчёта платы за содержание
общего имущества).
Для счётчика нужно хранить показания за несколько прошедших месяцев.
Тариф — это цена услуги или ресурса (например, цена за единицу объёма воды),
используется для расчёта платы за коммунальные услуги.
2.	Реализовать API для ввода и вывода данных по дому (например, адрес дома, список
квартир и т. п., должны выводиться данные из нескольких моделей).
3.	Реализовать функцию расчёта квартплаты для всех квартир в доме за какой-либо
месяц. Результаты записывать в БД. Функция должна сохранять прогресс расчёта.
Квартплата включает в себя:
● Водоснабжение. Рассчитывается по расходу воды за месяц
(тариф_за_единицу_объёма × расход). Расход — это разница между показаниями
счётчика за текущий и за предыдущий месяц.
● Содержание общего имущества. Рассчитывается на основе площади квартиры
(тариф_за_единицу_площади × площадь_квартиры).
4.	Реализовать API, которое запускает процесс расчёта квартплаты
в фоновом режиме (например в celery).
На усмотрение кандидата. Рекомендуется использовать django, celery, postgresql.
</details>


# Подготовка и запуск проекта
Склонировать репозиторий на локальную машину:
```
git clone git@github.com:TatianaLoskutova/EIS_Project.git
```

Запускаем проект: \
Для запуска проекта, необходимо выполнить в миграции: ``` python manage.py migrate  ```\
Затем запустить: ``` python manage.py runserver  ```

Сервер слушает по адресу ``` http://127.0.0.1:8000 ```

## Справка по API
В самом начале необходимо создать в администритивной панели Тарифы через superusera ```http://127.0.0.1:8000/admin/``` \
Создание суперюзера:
```python manage.py createsuperuser```
- Тариф для воды (name=water)
- Тариф для общего имущества (name=property)

**SWAGGER API** по адресу ``` http://127.0.0.1:8000/api/docs/ ```
Перед расчетом кварплаты дома желательно запустить CELERY ``` celery -A config worker -P solo -E -l info ``` \
И FLOWER ``` celery -A config worker -P solo -E -l info ```

<details>
    <summary>Расчет кварплаты</summary>

#### Расчет кварплаты по дому за определнный месяц
``` http POST /api/houses/<int:house_id>/month/<int:month>/ ``` \
Расчет идет в фоновом режиме, результат сохраняется в БД Postgres
</details>

<details>
    <summary>Houses</summary>

#### Создание нового дома
``` http POST /api/houses/ ```
#### Получить список домов
``` http GET /api/houses/ ```
#### Получить дом по pk
``` http GET /api/houses/<int:pk>/ ```
</details>

<details>
    <summary>Аpartment</summary>

#### Создание новой квартиры
``` http POST /api/apartments/ ```
#### Получить список квартир
``` http GET /api/apartments/ ```
#### Получить квартиру по pk
``` http GET /api/apartments/<int:pk>/ ```
</details>

<details>
    <summary>Watermeter</summary>

#### Создание показаний счетчика
``` http POST /api/watermeters/ ```

#### Получить список счетчиков
``` http GET /api/watermeters/ ```

#### Получить счетчик по pk
``` http GET /api/watermeters/<int:pk>/ ```
</details>

