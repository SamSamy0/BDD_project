CREATE DATABASE IF NOT EXISTS projectH303;
USE projectH303;

CREATE TABLE Utilisateur(
  ID  INT NOT NULL AUTO_INCREMENT,
  Nom VARCHAR(255) NOT NULL,
  Email VARCHAR(255) NOT NULL,
  Inscription DATE NOT NULL,
  Niveau INT NOT NULL,
  Points INT NOT NULL,
  PRIMARY KEY (ID)
);

CREATE TABLE Cours(
  Mnemonique VARCHAR(255) NOT NULL ,
  Nom VARCHAR(255) NOT NULL,
  Fac VARCHAR(255) NOT NULL,
  Credits INT NOT NULL,
  Annee INT,
  PRIMARY KEY (Mnemonique)
);

CREATE TABLE ObjetCosmetique (
  Nom VARCHAR(255) NOT NULL ,
  TypeObjet VARCHAR(255) NOT NULL,
  Prix INT NOT NULL,
  Description VARCHAR(255) NOT NULL,
  PRIMARY KEY (Nom)
);

CREATE TABLE Resume(
  ID  INT NOT NULL AUTO_INCREMENT,
  Titre VARCHAR(255) NOT NULL,
  Description VARCHAR(255),
  Publication DATE NOT NULL,
  Version INT NOT NULL,
  Visibilite BOOLEAN NOT NULL,
  Moyenne INT,
  Mnemonique VARCHAR(255) NOT NULL,
  IdUtilisateur INT NOT NULL,
  PRIMARY KEY (ID),
  FOREIGN KEY (Mnemonique) REFERENCES Cours(Mnemonique),
  FOREIGN KEY (IdUtilisateur) REFERENCES Utilisateur(ID)
);

CREATE TABLE Evaluation (
  ID INT NOT NULL  AUTO_INCREMENT,
  Note INT NOT NULL,
  Commentaire VARCHAR(100),
  IdUtilisateur INT NOT NULL,
  IdResume INT NOT NULL,
  PRIMARY KEY(ID),
  FOREIGN KEY(IdUtilisateur) REFERENCES Utilisateur(ID),
  FOREIGN KEY(IdResume) REFERENCES Resume(ID)
);

CREATE TABLE CoursUtilisateur (
  Mnemonique VARCHAR(255) NOT NULL,
  IdUtilisateur INT NOT NULL,
  CONSTRAINT ck_coursUser PRIMARY KEY (Mnemonique, IdUtilisateur),
  FOREIGN KEY(IdUtilisateur) REFERENCES Utilisateur(ID)
);

/*Normalization*/
CREATE TABLE HistoriqueClassement (
  Classement INT NOT NULL,
  Periode VARCHAR (255) NOT NULL,
  Gains INT NOT NULL,
  IdUtilisateur INT NOT NULL,
  CONSTRAINT ck_historique PRIMARY KEY(Classement, Periode),
  FOREIGN KEY (IdUtilisateur) REFERENCES Utilisateur(ID)
);

CREATE TABLE TransactionPoints (
  ID INT NOT NULL  AUTO_INCREMENT,
  Date DATE,
  Montant INT NOT NULL,
  TypeTransaction VARCHAR(255) NOT NULL,
  IdUtilisateur INT NOT NULL,
  PRIMARY KEY (ID),
  FOREIGN KEY (IdUtilisateur) REFERENCES Utilisateur(ID)
);

CREATE TABLE UtilisateurObjet (
  IdUtilisateur INT NOT NULL,
  Nom VARCHAR(255) NOT NULL,
  EstActif BOOLEAN,
  CONSTRAINT ck_objetUser PRIMARY KEY (IdUtilisateur, Nom),
  FOREIGN KEY (IdUtilisateur) REFERENCES Utilisateur(ID),
  FOREIGN KEY (Nom) REFERENCES ObjetCosmetique(Nom)

);



