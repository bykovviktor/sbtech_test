FROM python:3.8-alpine
RUN mkdir /app
ADD . /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]