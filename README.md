# Mon Application

Bienvenue dans le README de mon application ! Ce guide explique comment installer et lancer le **frontend** et le **backend** de manière simple et rapide.

## Prérequis

- **Node.js** (pour le frontend)
- **Python 3.x** et **pip** (pour le backend)
- **Git** (pour cloner le dépôt)

## Installation et lancement

### 1. Frontend

Le frontend utilise un `package.json` pour gérer les dépendances.

1. Accédez au dossier du frontend :

```bash
cd frontend
```

2. Installez les dépendances

```bash
yarn install
```

3. Lancer le projet

```bash
yarn dev
```

### 1. Backend

1. Accédez au dossier du backend :

```bash
cd backend
```

2. Installez les librairies python

```bash
pip install -r requirements.txt
```

3. Exécuter les migrations de bdd

```bash
python manage.py migrate
```


4. Lancer le script d'initialisation des data

```bash
python manage.py setup_data
```


5. Lancer le serveur

```bash
python manage.py runserver
```


Vous pouvez maintenant vous rendre sur l'adresse: http://localhost:5173
