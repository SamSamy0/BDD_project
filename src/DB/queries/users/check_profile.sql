SELECT u.Nom, u.Niveau, u.Points, uo.Nom
FROM Utilisateur u JOIN UtilisateurObjet uo on u.ID = uo.IdUtilisateur
WHERE u.ID = %s AND uo.EstActif = True
