SELECT u.Name, u.Niveau, u.Points, uo.Nom
FROM Utilisateur u JOIN UtilisateurObjet uo on u.ID = uo.IDUser
WHERE u.Id = %s AND uo.EstActif = True
