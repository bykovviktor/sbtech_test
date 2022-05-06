## Install and run:

```
docker-compose build
docker-compose up -d app 
```

### Note: App runs on port 8080 by default. If you want to change it - please edit `docker-compose.yml`

> If you want to run API tests, please use command:
>
> ```
> docker-compose up test
> ```

## If you want to use only app docker image, please go to app dir and run

```
docker build .
```

## Usage

send `GET` request to `127.0.0.1:443/card/<card number>`

example for correct card number: 30080657890123456

**app validates:**
 - card number length ( <16 and >20 )
 - card number consits digits only

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

## Contacts:
 
 Viktor
 
 tg: @vbykov

mail: bykov.v@gmail.com
