FROM python:3.14

WORKDIR /backend_finance

ENV PYTHONPATH=/backend_finance:/backend_finance/app

COPY ./requirements.txt /backend_finance/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend_finance/requirements.txt

COPY ./app /backend_finance/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]