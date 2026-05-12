CREATE DATABASE IF NOT EXISTS projectH303;
USE projectH303;

CREATE TABLE Utilisateur(
  ID  INT NOT NULL AUTO_INCREMENT,
  Name VARCHAR(15) NOT NULL,
  Email VARCHAR(255) NOT NULL,
  Inscription DATE NOT NULL,
  Niveau INT NOT NULL,
  Points INT NOT NULL,
  PRIMARY KEY (ID)
);

CREATE TABLE Cours(
  Mnemonique VARCHAR(10) NOT NULL ,
  Nom VARCHAR(15) NOT NULL,
  Fac VARCHAR(15) NOT NULL,
  Annee INT NOT NULL,
  PRIMARY KEY (Mnemonique)
);

CREATE TABLE ObjetCosmetique (
  Nom VARCHAR(15) NOT NULL ,
  TypeObjet VARCHAR(10) NOT NULL,
  Prix INT NOT NULL,
  Description VARCHAR(100) NOT NULL,
  PRIMARY KEY (Nom)
);

CREATE TABLE Resume(
  ID  INT NOT NULL AUTO_INCREMENT,
  Title VARCHAR(15) NOT NULL,
  Description VARCHAR(255),
  Publication DATE NOT NULL,
  Version INT NOT NULL,
  Visibilite BOOLEAN NOT NULL,
  Moyenne INT,
  Mnemonique VARCHAR(10) NOT NULL,
  IdUser INT NOT NULL,
  PRIMARY KEY (ID),
  FOREIGN KEY (Mnemonique) REFERENCES Cours(Mnemonique),
  FOREIGN KEY (IdUser) REFERENCES Utilisateur(ID)
);

CREATE TABLE Evaluation (
  ID INT NOT NULL  AUTO_INCREMENT,
  Note INT NOT NULL,
  Commentaire VARCHAR(100),
  IDUser INT NOT NULL,
  IDResume INT NOT NULL,
  PRIMARY KEY(ID),
  FOREIGN KEY(IDUser) REFERENCES Utilisateur(ID),
  FOREIGN KEY(IDResume) REFERENCES Resume(ID)
);

CREATE TABLE CoursUtilisateur (
  Mnemonique VARCHAR(10) NOT NULL,
  IDUser INT NOT NULL,
  CONSTRAINT ck_coursUser PRIMARY KEY (Mnemonique, IDUser),
  FOREIGN KEY(IDUser) REFERENCES Utilisateur(ID)
);

CREATE TABLE HistoriqueClassement (
  Classement INT NOT NULL,
  Periode VARCHAR (15) NOT NULL,
  Points INT NOT NULL,
  IDUser INT NOT NULL,
  CONSTRAINT ck_historique PRIMARY KEY(Classement, Periode),
  FOREIGN KEY (IDUser) REFERENCES Utilisateur(ID)
);

CREATE TABLE TransactionPoints (
  ID INT NOT NULL  AUTO_INCREMENT,
  Jour DATE,
  Montant INT NOT NULL,
  TypeTransaction VARCHAR(10) NOT NULL,
  IdUser INT NOT NULL,
  PRIMARY KEY (ID),
  FOREIGN KEY (IDUser) REFERENCES Utilisateur(Id)
);

CREATE TABLE UtilisateurObjet (
  IDUser INT NOT NULL,
  Nom VARCHAR(15) NOT NULL,
  EstActif BOOLEAN,
  CONSTRAINT ck_objetUser PRIMARY KEY (IDUsers, Nom),
  FOREIGN KEY (IDUser) REFERENCES Utilisateur(ID),
  FOREIGN KEY (Nom) REFERENCES ObjetCosmetique(Nom)

);



