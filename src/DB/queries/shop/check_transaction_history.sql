SELECT t.ID, t.Jour, t.Montant, t.TypeTransaction
FROM TransactionPoints t
WHERE t.IdUser = %s
