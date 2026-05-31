SELECT u.Nom, u.Points, SUM(t.Montant) AS TotalDepense
FROM Utilisateur u
JOIN TransactionPoints t ON t.IdUtilisateur = u.ID
WHERE t.TypeTransaction = 'dépense'
GROUP BY u.ID, u.Nom, u.Points
HAVING SUM(t.Montant) > u.Points;