INSERT INTO TransactionPoints (Date, Montant, TypeTransaction, IdUtilisateur);
SELECT r.Publication, 100, 'Résumé', r.IdUtilisateur;
FROM Resume r;

INSERT INTO TransactionPoints (Date, Montant, TypeTransaction, IdUtilisateur);
SELECT '2005-01-24', 50, 'Evalution', e.IdUtilisateur;
FROM Evaluation e;

INSERT INTO TransactionPoints (Date, Montant, TypeTransaction, IdUtilisateur);
SELECT '2005-04-11', -oc.Prix, 'Achat', uo.IdUtilisateur;
FROM UtilisateurObjet uo;
JOIN ObjetCosmetique oc ON uo.IdObjet = oc.ID;