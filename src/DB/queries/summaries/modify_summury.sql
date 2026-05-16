SELECT r.ID r.Titre,r.Description, r.Version, r.Mnemonique
FROM Resume r
WHERE r.ID = %s and  r.Titre = %s and  r.Description = %s
    and  r.Version = %s and  r.Mnemonique = %s
    and r.Version = r.Version +1