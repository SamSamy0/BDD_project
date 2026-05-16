SELECT r.ID r.Titre,r.Description, r.Publication,r.Version, r.Visibilite, r.Moyenne, r.Mnemonique
FROM Resume r
WHERE r.ID = %s