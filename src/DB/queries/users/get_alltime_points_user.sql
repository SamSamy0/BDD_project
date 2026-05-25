SELECT SUM(Points) as Total
FROM TransactionPoints
WHERE ID= %(idUser)s AND TypeTransaction='gains'
