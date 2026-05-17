-- Select all user's courses
SELECT c.Mnemonique
FROM CoursUtilisateur c
WHERE c.IdUtilisateur = %s
