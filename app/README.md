# Hello!

It's a test task for a technical interview from Viktor Bykov.

You are in application directory.

___
## Before install and run:
```Please check first `docker` is installed```
___
## Install and run:

```
docker build -t image_name .
docker run -d -p 8080:8080 image_name
```
___
## Usage

send `GET` request to `127.0.0.1:443/card/<card number>`

example for correct card number: 30080657890123456

**app validates:**
 - card number length ( 16 >= length >= 20 )
 - card number contains digits only

**Response:**
 - http code
 - message body

http codes:
``` 
 500:
  - internal server error
  - if card number length is incorrect
  - if card number has letters or some special symbols.
  - bin number was not found in database
 200:
  - card number is correct and bin number is in database
```

message body:
```
  error details for error 500
  bank details for valid card (json)
```
___
## Contacts:
 
 Viktor
 
 tg: @vbykov

mail: bykov.v@gmail.com



___

Task details:

```
Определение банка по номеру карты

Часть 1

Разработать на языке Python сервер, определяющий банк по номеру банковской карты.
Приложение должно удовлетворять следующим критериям.

    Приложение при запуске считывает из csv-файла на диске базу данных BIN-номеров (файл с базой можно взять на GitHub: https://github.com/iannuttall/binlist-data)
    После успешной загрузки приложение «превращается» в HTTP-сервер (открывает на прослушивание TCP-порт, готовится принимать запросы на него).
    При поступлении GET-запроса "GET /cards/<номер карты>" сервер
        проверяет корректность номера карты (номер должен быть длиной от 16 до 20 символов включительно и состоять из цифр);
        в случае некорректного номера отвечает пользователю HTTP-кодом 500 и завершает обработку запроса;
        в случае корректного номера
            выделяет BIN-номер (первые 6 цифр номера карты);
            производит поиск по базе данных BIN-номеров;
            отвечает пользователю HTTP-кодом 200, содержимое ответа – найденная информация о банке (в любой форме: текст, JSON, XML, HTML; все поля или их часть).

Развитие приложения в любом направлении (от повышения удобства эксплуатации до внедрения новых функций) не является обязательным, но приветствуется.

Часть 2

Разработать на unittest автоматические тесты для сервера из первой части.

Часть 3

Упаковать сервер из первой части в docker-контейнер. Запустить и протестировать получившееся контейнеризированное приложение автотестами из части 2.
```
