SELECT SUM(Montant) as Total
FROM TransactionPoints
WHERE IdUtilisateur= %(idUser)s AND Montant >0;
