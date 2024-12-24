# Python alapú kép
FROM python:3.11-slim

# Munkakönyvtár beállítása
WORKDIR /app

# Követelmények másolása
COPY requirements.txt requirements.txt

# Python csomagok telepítése
RUN pip install --no-cache-dir -r requirements.txt

# Alkalmazás fájlok másolása
COPY . .

# Port nyitása
EXPOSE 5000

# Alkalmazás futtatása
CMD ["python", "backend.py"]
