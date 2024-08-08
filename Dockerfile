FROM python:3.12-alpine

COPY pyproject.toml ./
COPY requirements.txt ./
COPY app ./app/
COPY tests ./tests/

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app/__init__.py"]
