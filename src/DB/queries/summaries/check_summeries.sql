SELECT r.Titre, r.Publication, r.Visibilite, r.Moyenne, r.Version, r.Mnemonique
FROM Resume r
WHERE r.Mnemonique = %(mnemo)s
