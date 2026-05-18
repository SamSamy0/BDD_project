SELECT u.Nom, u.Niveau, u.Points, uo.IdObjet AS IdObjet, oc.Nom AS NomObjet
FROM Utilisateur u 
LEFT JOIN UtilisateurObjet uo ON u.ID = uo.IdUtilisateur JOIN ObjetCosmetique oc ON oc.ID = uo.IdObjet
AND uo.EstActif = 1 AND oc.TypeObjet = 'Titre'
WHERE u.ID = 5;
