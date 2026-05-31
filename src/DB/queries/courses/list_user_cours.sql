SELECT c.Mnemonique
FROM CoursUtilisateur c
WHERE c.IdUtilisateur = %(idUser)s
