FROM python:3.14

WORKDIR /backend_finance

COPY ./requirements.txt /backend_finance/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend_finance/requirements.txt

COPY /app /backend_finance/app

CMD [ "fastapi", "run" ]