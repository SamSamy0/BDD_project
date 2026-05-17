SELECT u.Nom
FROM Utilisateur u, Resume r
WHERE u.ID = r.IdUtilisateur
GROUP BY u.ID
HAVING COUNT(DISTINCT r.Mnemonique) > 1;

