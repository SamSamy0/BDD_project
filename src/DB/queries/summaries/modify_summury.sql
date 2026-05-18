²SELECT r.ID r.Titre,r.Description, r.Version, r.Mnemonique
FROM Resume r
WHERE r.ID = %(idSumm)s and  r.Titre = %(title)s and  r.Description = %s
    and  r.Version = %(version)s and  r.Mnemonique = %(mnemo)s
    and r.Version = r.Version +1