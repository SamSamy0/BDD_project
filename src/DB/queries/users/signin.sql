SELECT u.ID
FROM Utilisateur u
WHERE u.Nom = %(username)s and u.Email = %(email)s;
