SELECT u.Nom, u.Niveau, u.Points, Titre.IdObjet, Titre.NomObjet AS NomObjet, Titre.TypeObjet
FROM Utilisateur u 
LEFT JOIN (
  SELECT uo.IdUtilisateur, uo.IdObjet, oc.nom AS NomObjet, oc.TypeObjet
  FROM UtilisateurObjet uo
  JOIN ObjetCosmetique oc on uo.IdObjet = oc.ID
  WHERE EstActif = 1 AND (oc.TypeObjet = 'titre' or oc.TypeObjet='badge')
) AS Titre ON u.ID = Titre.IdUtilisateur
WHERE u.ID = %(idUser)s;
