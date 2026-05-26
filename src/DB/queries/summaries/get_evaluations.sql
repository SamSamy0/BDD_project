SELECT e.ID, e.Note, u.Nom
FROM Evaluation e, Utilisateur u
WHERE e.IdUtilisateur = u.ID AND e.IdResume = %(IdResume)s
