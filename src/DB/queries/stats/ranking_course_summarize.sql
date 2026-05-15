SELECT r.Mnemonique, COUNT(r.Mnemonique)
FROM Resume r
GROUP BY Mnemonique
HAVING COUNT(Mnemonique) = (
    SELECT MAX(myCount)
    FROM (
        SELECT Mnemonique, COUNT(Mnemonique) as myCount
        FROM Resume
        GROUP BY Mnemonique
    ) as temp
);
