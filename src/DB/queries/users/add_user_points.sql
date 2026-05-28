-- Increment user's points
UPDATE Utilisateur SET Points = Points + %(cost)s WHERE ID =  %(idUser)s
