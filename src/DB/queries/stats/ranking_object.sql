SELECT o.Nom, COUNT(uo.IdUtilisateur) AS compteur
FROM UtilisateurObjet uo
JOIN ObjetCosmetique o ON uo.IdObjet = o.ID
GROUP BY o.Nom
ORDER BY compteur DESC
LIMIT 5;

