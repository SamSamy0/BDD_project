SELECT AVG(compteur) AS Moyenne
FROM (
    SELECT r.IdUtilisateur, COUNT(r.Mnemonique) AS compteur
    FROM Resume r
    GROUP BY r.IdUtilisateur
) AS table_temporaire;

