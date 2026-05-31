SELECT r.Titre, r.Publication, r.Visibilite, r.Moyenne, r.Version, r.Mnemonique, u.Nom, r.ID, r.IdUtilisateur
FROM Resume r, Utilisateur u
WHERE r.Mnemonique = %(Mnemonique)s AND r.IdUtilisateur = u.ID
