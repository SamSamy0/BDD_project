-- Add object to users
INSERT INTO UtilisateurObjet (IdUtilisateur, Nom, EstActif)
VALUES (%(idAuthor)s, %(name)s, False)
