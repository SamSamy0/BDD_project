SELECT sum(hc.Gains), hc.IdUtilisateur
From HistoriqueClassement hc
GROUP BY hc.IdUtilisateur
ORDER BY hc.Gains DESC
