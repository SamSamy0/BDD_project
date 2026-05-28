SELECT u.Nom
FROM Utilisateur u
WHERE u.Points < (
    SELECT SUM(t.Montant)
    FROM TransactionPoints t
    WHERE t.IdUtilisateur = u.ID
);
