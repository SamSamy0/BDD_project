SELECT hc.Classement, hc.Periode, hc.Gains, hc.IdUtilisateur
From HistoriqueClassement hc
WHERE hc.Periode = %s
ORDER BY hc.Gains DESC

/*TODO: Réfléchir à l'attribut Classement, pour savoir si on le garde ou pas,
lors des demandes de classement antérieur*/