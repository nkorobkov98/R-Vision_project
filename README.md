# R-Vision Project

## 1. Как поднять проект

1. Скопируйте файл .env.example и создайте файл .env в корневом каталоге проекта.
2. Выполните те же действия в каталоге backend, создав файл .env.
3. Соберите контейнеры с помощью команды:

   
   docker-compose build
   

4. Поднимите контейнеры с помощью команды:

   
   docker-compose up
   

## 2. Описание работы

### Эндпоинт API

Проект предоставляет API эндпоинт по адресу:

http://127.0.0.1:8000/api/upload-xml


Этот эндпоинт предназначен для получения OVAL файла. Вы можете отправить файл с помощью команды curl:

curl -X POST http://127.0.0.1:8000/api/upload-xml/ \
  -F "xml_file=@rhel-8.oval.xml"


### Административная панель

После успешного парсинга данных вы сможете зайти в административную панель по адресу:

http://127.0.0.1:8000/admin


Для входа используйте учетные данные суперпользователя:

- Имя пользователя: admin
- Электронная почта: admin@example.com
- Пароль: mypassword

### Просмотр и экспорт данных

В административной панели вы сможете просмотреть все спаршенные данные. Также работает поиск по полям CVE и RHBA.

Вы можете выделить определенные патчи или все данные и экспортировать их в формат CSV, JSON и т.д., с нужными столбцами из базы данных.
