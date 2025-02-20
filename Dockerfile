FROM python:3.12-alpine

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install poetry

COPY . .

RUN poetry config virtualenvs.create false
RUN poetry install

ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0", "bla.main:api" ]
