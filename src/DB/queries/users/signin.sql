SELECT u.ID, u.Points, u.Niveau, u.Nom
FROM Utilisateur u
WHERE u.Nom = %(username)s and u.Email = %(email)s;
