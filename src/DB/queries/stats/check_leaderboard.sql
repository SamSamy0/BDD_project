SELECT
    RANK() OVER (ORDER BY Points DESC) as Rang,
    Nom,
    Points
FROM Utilisateur
ORDER BY Points DESC
