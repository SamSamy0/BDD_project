SELECT AVG(compteur)
FROM (
    --Nombre de publication par utilisateur 
    SELECT r.IdUtilisateur, COUNT(r.Mnemonique) AS compteur
    FROM Resume r
    GROUP BY r.IdUtilisateur
) AS table_temporaire;

