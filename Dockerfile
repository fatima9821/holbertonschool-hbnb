# Utiliser l'image de base alpine avec Python 3.8
FROM python:3.8-alpine

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier les fichiers requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application dans le conteneur
COPY . .

# Définir la variable d'environnement pour le port
ENV PORT=5000

# Exposer le port sur lequel l'application s'exécute
EXPOSE $PORT

# Définir le volume pour la persistance des données
VOLUME ["/app/data"]

# Commande pour lancer l'application avec Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
