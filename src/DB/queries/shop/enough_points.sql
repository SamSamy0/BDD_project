SELECT u.ID
FROM Utilisateur u
WHERE u.ID = %(ID)s and u.Points >= %(points)s
