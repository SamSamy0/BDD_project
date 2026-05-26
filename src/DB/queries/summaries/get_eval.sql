SELECT e.Note, e.Commentaire, u.Nom
FROM Evaluation e, Utilisateur u
WHERE e.ID = %(ID)s AND u.ID = e.IdUtilisateur
