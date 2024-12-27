FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml ./

RUN pip install --no-cache-dir build setuptools && pip install --no-cache-dir .

COPY . .

# Alkalmazás futtatása
CMD ["python", "app.py"]
