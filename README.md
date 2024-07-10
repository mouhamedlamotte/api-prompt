## Get ready ! 

d'abord il faut forker le projet en appuyant sur le bouton fork de de GitHub.

## Cloner le depot github

ouvrez votre terminal et faites la commande suivante :

```bash 
git clone https://github.com/<username>/api-prompt.git
```

## CREER UN ENVIRONNEMENT VIRTUEL

```bash
cd api-prompt
python3 -m venv .venv
```

## ACTIVER L'ENVIRONNEMENT VIRTUEL

WINDOWS
```bash
.\.venv\Scripts\activate
```
LINUX OR MAC
```bash
source .venv/bin/activate
```

## INSTALLER LES DEPENDANCES

```bash
pip install -r requirements.txt
```

## COPIER env.exemple EN .env

```bash
cp env.exemple .env
```
apres aavoir copier env.exemple en .env , renseigner les informations

## INITIALISER LA BASE DE DONNEES

```bash
flask init-db
```

## LANCER LE SERVEUR
AVEC FLASK 

```bash
flask run
```

AVEC WSGI PYTHON

```bash
python3 wsgi.py
```

AVEC GUNICORN

```bash
gunicorn -b :5000 wsgi:app
```

LE SERVEUR SERA LANCER SUR [http://127.0.0.1:5000](http://127.0.0.1:5000)


# TESTER L'API


BY [@mouhamedlamotte](https://github.com/mouhamedlamotte)
