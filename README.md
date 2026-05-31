# BDD_project

Cette application client-serveur permet aux étudiants de partager des résumés de cours, de s'évaluer mutuellement et de gagner des points pour débloquer des objets cosmétiques dans une boutique intégrée. Elle dispose d'une interface graphique moderne basée sur customtkinter et repose sur une base de données MySQL.


# Prérequis
1. Python 3

2. Serveur MySQL (mysql-server)


# Installation et configuration

Si MySql Server n'est pas déjà installé , exécuter cette ligne de commande

```bash
sudo apt update
sudo apt install mysql-server
```

```bash
sudo mysql < src/DB/init.sql
sudo mysql < src/DB/id.sql
sudo mysql < src/DB/init_transactions.sql

```

Installer Tkinter

```bash
sudo apt install python3-tk
```

# Dependences

customtkinter==5.2.2

# Environnement Virtuel et Dépendances Python

 ```bash
 # 1. Installation de pip et venv
 sudo apt install python3-pip python3.14-venv

 # 2. Création de l'environnement virtuel
python3 -m venv .venv

 # 3. Activation de l'environnement
source .venv/bin/activate

 # 4. Installation des dépendances
pip install -r requirements.txt
 ```


# Importation des données initiales

```bash
cd src
./initData.sh
```

# Lancement de l'application

L'application fonctionne avec une architecture Client/Serveur (communication par Sockets et JSON). Vous devez d'abord lancer le serveur, puis le client.

### Démarrer le Serveur
```bash
./src/run_server.sh
```
Le serveur écoute par défaut sur l'IP 127.0.0.1 au port 8080.

### Démarrer le Client
Dans un nouveau terminal (en vous assurant d'avoir préalablement activé l'environnement virtuel avec source .venv/bin/activate) :
```bash
./src/run_client.sh
```

