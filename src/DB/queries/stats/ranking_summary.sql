SELECT r.Mnemonique, r.Titre, r.ID, AVG(e.Note) AS note_moyenne
FROM Evaluation e
JOIN Resume r ON r.ID = e.IdResume
GROUP BY r.Mnemonique, r.Titre, r.ID
HAVING note_moyenne = (

    SELECT MAX(table_temp.note_moyenne)
    FROM (

        SELECT r2.Mnemonique, r2.ID, AVG(e2.Note) AS note_moyenne
        FROM Evaluation e2
        JOIN Resume r2 ON r2.ID = e2.IdResume
        GROUP BY r2.Mnemonique, r2.ID
    ) AS table_temp
    WHERE table_temp.Mnemonique = r.Mnemonique
);