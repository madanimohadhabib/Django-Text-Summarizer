# Étape 1 : Choisir une image de base
FROM python:3.9-slim

# Étape 2 : Définir les variables d'environnement
ENV PYTHONUNBUFFERED 1

# Étape 3 : Créer un répertoire de travail dans le conteneur
WORKDIR /app

# Étape 4 : Copier les fichiers de votre projet dans le conteneur
COPY . /app/

# Étape 5 : Installer les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Étape 6 : Exposer le port 8000
EXPOSE 8000

# Étape 7 : Exécuter le serveur Django (en mode développement)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


