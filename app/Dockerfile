FROM python:3.9-slim

# Installation des dépendances système pour psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# On copie et on installe les dépendances AVANT le reste
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie le code
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
