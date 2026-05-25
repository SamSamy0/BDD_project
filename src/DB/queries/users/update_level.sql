UPDATE Utilisateur SET Niveau=%(new_lvl)s WHERE ID=%(idUser) AND Niveau < %(new_lvl)s;
