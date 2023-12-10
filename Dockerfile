FROM python:3.9-slim

WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .
COPY requirements_dev.txt .
COPY requirements_api.txt .


# Installer les dépendances
RUN pip --default-timeout=100 install --no-cache-dir -r requirements.txt
RUN pip --default-timeout=100 install --no-cache-dir -r requirements_dev.txt
RUN pip --default-timeout=100 install --no-cache-dir -r requirements_api.txt

# Copier le reste du code
COPY . /app/

EXPOSE 800

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "800"]
