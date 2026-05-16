SELECT u.ID, u.Points, u.Niveau
FROM Utilisateur u
WHERE u.Nom = %(username)s and u.Email = %(email)s;
