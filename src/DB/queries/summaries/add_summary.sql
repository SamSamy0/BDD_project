INSERT INTO Resume (Titre, Description, Publication, Version, Visibilite, Moyenne, Mnemonique, IdUtilisateur)
SELECT %(title)s, %(desc)s, %(date)s, %(version)s, %(visible)s, NULL, %(mnemo)s, %(idAuthor)s
FROM CoursUtilisateur
WHERE Mnemonique = %(mnemo)s AND IdUtilisateur = %(idAuthor)s;

