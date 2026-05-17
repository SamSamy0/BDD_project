SELECT u.Nom, u.Niveau, u.Points, uo.IdObjet AS IdObjet
FROM Utilisateur u 
LEFT JOIN UtilisateurObjet uo ON u.ID = uo.IdUtilisateur AND uo.EstActif = 1
WHERE u.ID = %(idUser)s;
