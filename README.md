# BDD_project

Si MySql Server n'est pas déjà installé , exécuter cette ligne de commande

```bash
sudo apt install mysql-server
sudo mysql < src/DB/id.json
sudo mysql < src/DB/init.json

```

# Dependences
customtkinter==5.2.2

1. Création d'un environnement virtuel
```bash
python3 -m venv .venv
```
2. Activation de l'environnement
```bash
source .venv/bin/activate
```
3. Installation des dépendences

```bash
pip install -r requirements.txt
sudo apt install mysql-server
```


