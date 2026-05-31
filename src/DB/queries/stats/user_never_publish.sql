SELECT u.ID, u.Nom 
FROM Utilisateur u 
WHERE NOT EXISTS( 
  SELECT r.IdUtilisateur 
  FROM Resume r 
  WHERE r.IdUtilisateur=u.ID);
