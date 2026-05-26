SELECT o.Nom, o.ID, o.TypeObjet, uo.EstActif
FROM ObjetCosmetique o
JOIN UtilisateurObjet uo ON uo.IdObjet = o.ID
WHERE uo.IdUtilisateur = %(idUser)s;
