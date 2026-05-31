-- Select all user's courses
SELECT c.Mnemonique, co.Nom, co.Fac, co.Credits, co.Annee
FROM CoursUtilisateur c
JOIN Cours co ON co.Mnemonique = c.Mnemonique
WHERE c.IdUtilisateur = %(idUser)s
