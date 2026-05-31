UPDATE Resume
    SET Titre = %(title)s,
        Description = %(desc)s,
        Version = Version + 1
    WHERE ID = %(idSumm)s AND IdUtilisateur = %(idAuthor)s;
