SELECT r.Titre, r.Publication, r.Visibilite, r.Moyenne, r.Version, r.Mnemonique, u.Nom, r.ID, r.IdUtilisateur,r.Visibilite
FROM Resume r, Utilisateur u
WHERE r.Mnemonique = %(Mnemonique)s AND r.IdUtilisateur = u.ID AND (r.Visibilite = 1 OR r.IdUtilisateur = %(idUser)s)
