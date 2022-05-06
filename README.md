**Hi**

It's web application to check card number

Install:

```
docker build -t sbertech .
```
Run:
```
docker run -p <your_local_port>:8080 sbertech 
```

Usage

send GET request to 127.0.0.1:443/card/<card number>

app checks:
-card number length ( <16 and >20 )
-card number consits digits only

you will get a response:
 http code
 message body

http code:
``` 
 500:
  internal server error
  if card number length is incorrect
  if card number has letters or some special symbols.
  bin number was not found in database
 200:
  card number is correct and bin number is in database
```

message body:
```
  error details for error 500
  bank details for valid card (json)
```

for some additional info please contact:
 Viktor
 tg: @vbykov
 mail: bykov.v@gmail.com
