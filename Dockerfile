# Image de base légère Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les dépendances en premier (optimisation du cache Docker)
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app/ .

# Exposer le port 3000
EXPOSE 3000

# Commande de démarrage
CMD ["python", "app.py"]