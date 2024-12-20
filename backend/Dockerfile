# Alap image, amely tartalmaz Python 3-at
FROM python:3.10-slim

# Munkakönyvtár létrehozása az alkalmazás számára
WORKDIR /app

# Másold a követelményeket a konténerbe
COPY requirements.txt /app/

# A szükséges Python csomagok telepítése
RUN pip install --no-cache-dir -r requirements.txt

# Az alkalmazás fájlok másolása
COPY . /app/

# A Flask alkalmazás elindításához szükséges környezeti változók beállítása
ENV FLASK_APP=backend.py
ENV FLASK_RUN_HOST=0.0.0.0

# Az alkalmazás alapértelmezett portja
EXPOSE 5000

# A Flask alkalmazás futtatása
CMD ["flask", "run"]
