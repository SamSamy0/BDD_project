-- Add object to users
INSERT INTO UtilisateurObjet (IdUtilisateur, IdObjet, EstActif)
VALUES (%(idUser)s, %(objId)s, False);
