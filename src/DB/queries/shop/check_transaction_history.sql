SELECT t.ID, t.Date, t.Montant, t.TypeTransaction
FROM TransactionPoints t
WHERE t.IdUtilisateur = %(idUser)s
