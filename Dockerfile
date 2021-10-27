FROM python:3.9

WORKDIR /create_event

COPY ./requirements.txt /create_event/requirements.txt

EXPOSE 8000:8000

RUN pip install --no-cache-dir --upgrade -r /create_event/requirements.txt

COPY ./sql_app /create_event/sql_app

CMD ["uvicorn", "sql_app.main:app", "--host", "0.0.0.0", "--port", "80"]
