USE projectH303;
INSERT INTO TransactionPoints (Date, Montant, TypeTransaction, IdUtilisateur)
SELECT r.Publication, 100, 'Résumé', r.IdUtilisateur
FROM Resume r;

INSERT INTO TransactionPoints (Date, Montant, TypeTransaction, IdUtilisateur)
SELECT '2005-01-24', 50, 'Evaluation', e.IdUtilisateur
FROM Evaluation e;

INSERT INTO TransactionPoints (Date, Montant, TypeTransaction, IdUtilisateur)
SELECT '2005-04-11', -oc.Prix, 'dépense', uo.IdUtilisateur
FROM UtilisateurObjet uo
JOIN ObjetCosmetique oc ON uo.IdObjet = oc.ID;

INSERT INTO TransactionPoints (Date, Montant, TypeTransaction, IdUtilisateur)
SELECT NOW(), u.Points - IF(t.TotalTransactions IS NULL, 0, t.TotalTransactions),'ajustement',u.ID
FROM Utilisateur u
LEFT JOIN ( SELECT IdUtilisateur, SUM(Montant) as TotalTransactions 
  FROM TransactionPoints 
  GROUP BY IdUtilisateur) t 
ON u.ID = t.IdUtilisateur
WHERE u.Points - IF(t.TotalTransactions IS NULL, 0, t.TotalTransactions) != 0;

