## Parser

Парсер был написан в рамках тестового задания.

Заходит в три категории из каталога, собирает все товары в данной категории (учитывая пагинацию). В карточке товара забирает "Название", "цена", "Описание".

Данные сохраняет в csv файл

### Tech Stack
- python 3.9
- Scrapy

### Installation

1. Клонируйте репозиторий

```
git clone git@github.com:verafadeeva/test_parser.git
```
2. Установите виртуальное окружение
```
python3.9 -m venv .venv
```
3. Активируйте виртуальное окружение
```
source .venv/bin/activate
```
4. Установите зависимости
```
pip install -r requirements.txt
```
5. В корне проекта выполните
```
scrapy crawl paints
```
После работы парсера данные будут сохранены в файл items.csv

### Authors

Вера Фадеева (lunatik.yar@gmail.com)
