#import "config.typ": *

#show: template

= Introduction <intro>
Le projet consiste à créer une plateforme universitaire qui permet aux étudiants de publier leurs résumés sur un cours. À cela se rajoute un aspect ludique: les étudiants ont la possibilité d'évaluer les résumés, qui grâce à un système de points de contributions, permet d'évoluer dans un classement et d'acquérir des objets cosmétiques.

Pour cette première phase, en nos qualités d'experts en bases de données, nous avons pour but de modéliser l'application sous forme de modèle Entité-Association et Relationnel, tout en définissant toutes les contraintes et les hypothèses.


Le rapport contient le diagramme Entité-Association modélisant le projet, dont découle le modèle Relationnel. Seront introduites par la suite les contraintes au niveau d'unicité, de domaine et d'intégrité. Enfin, le document se conclut sur l'exposé des nos hypothèses de travail et leurs justifications.

Pour conclure, cette modélisation doit être robuste car elle servira de fondation directe pour l'implémentation de la prochaine phase.

= Modèle Entité-Association
\
\
\
#figure(image("Diagramme/Mode\u{300}le EA.drawio.svg", height : 60% ),
caption: [Diagramme Entité-Association])
#remark[Pour mieux visualiser le diagramme, il est nécessaire de zoomer (format .svg)]

= Modèle Relationnel


#block(breakable:false)[Utilisateur(#underline[Identifiant], Nom, Email, ProfilNiveau,           ProfilNombrePoint, ProfilDateInscription)
]



#block(breakable:false)[Résumé(#underline[Identifiant], Titre, Description, Date de publication, Version, Visibilité, /Note moyenne, Code, IdUtilisateur)]
Résumé.Code référence Cours.Code
Résumé.IdUtilisateur référence Utilisateur.Identifiant

#block(breakable:false)[Evaluation(#underline[Identifiant], Note, Commentaire,IdUtilisateur, IdRésumé)]

Evaluation.IdRésumé référence Résumé.Identifiant

Evaluation.IdUtilisateur référence Utilisateur.Identifiant

#block(breakable:false)[Cours(#underline[Code], Nom, Faculté, Année)]

#block(breakable:false)[CoursUtilisateur(#underline[Code,IdUtilisateur])]

Code référence Cours.Code

IdUtilisateur référence Utilisateur.Identifiant

#block(breakable:false)[HistoriqueClassement(#underline[Classement, Période], Points, IdUtilisateur)]

HistoriqueClassement.IdUtilisateur référence Utilisateur.Identifiant

#block(breakable:false)[TransactionPoints(#underline[Identifiant], Date, Montant, Type, IdUtilisateur)]

TransactionPoints.IdUtilisateur référence Utilisateur.Identifiant

#block(breakable:false)[ObjetCosmétique(#underline[Nom], Type, Prix, Description)]

#block(breakable:false)[UtilisateurObjetCosmétique(#underline[IdUtilisateur, Nom], EstActif)]
UtilisateurObjetCosmétique.IdUtilisateur référence Utilisateur.Identifiant

UtilisateurObjetCosmétique.Nom 
référence ObjetCosmétique.Nom






= Contraintes

== Contraintes d'intégrité

- L'utilisateur qui publie un résumé de cours doit faire partie du cours
- La date d'inscription de l'utilisateur doit être inférieure à la date de publication
- L'utilisateur ne peut pas noter/évaluer ses propres résumés
- L'utilisateur ne peut pas acheter plusieurs fois le même badge ni activer un titre ou un badge plusieurs fois
- L'utilisateur doit avoir suffisamment de points pour acheter un objet cosmétique
- Un utilisateur ne peut porter que des objets qu'il possède
- Un résumé en version non visible ne peut pas recevoir d’évaluations
- Lors de l'activation, un utilisateur a la possibilité d'activer au plus 1 objet cosmétique pour chaque type

== Contraintes d'unicité

- Le mail de chaque utilisateur est unique
- Les noms des objets cosmétiques sont uniques
- L'utilisateur ne peut évaluer un résumé qu'une seule fois

== Contraintes de domaine

- Les notes d'évaluation sont comprises entre 0 et 20
- Les identifiants des utilisateurs, des évaluations, des résumés et des transactions de points contiennent uniquement des chiffres
- Les prix des objets cosmétiques doivent être sous forme d'entiers (représentant leur valeur en terme de points) 
- Le total de points de l'utilisateur ne peut pas être négatif 
- Le prix des objets cosmétiques ne peut pas être négatif 
- Le format de mail doit contenir le symbole "@"
- Les dates d'inscriptions, de publications, et la période d'HistoriqueClassement ne peuvent pas être des dates "futures" qui ne sont pas encore passées
- La visibilité des résumés est soit "Public" ou "Privé"


= Hypothèses et Justifications
+ Une évaluation doit n'avoir qu'un seul auteur
+ Le classement se fait uniquement sur base des points gagnés
+ Un objet cosmétique peut appartenir à plusieurs utilisateurs
+ Lors de l'inscription, l'utilisateur doit être un étudiant
+ Un cours ne contenant aucun élève n'existe pas 
+ Les pseudos ne sont pas uniques car les utilisateurs se distinguent sur base de leurs identifiants


== Entre Utilisateur --- HistoriqueClassement 

#block(breakable:false)[*Cardinalité :* Utilisateur (1,n) - HistoriqueClassement(1,1)] 

#block(breakable :false)[*Justification: *]
- Un utilisateur est classé au cours de plusieurs périodes #sym.arrow (1,n)
- Un HistoriqueClassement ne concerne qu'un utilisateur #sym.arrow (1,1)

== Entre Utilisateur --- TransactionPoints 

#block(breakable:false)[*Cardinalité :* Utilisateur (0,n) - TransactionPoints(1,1)]

#block(breakable :false)[*Justification: *]
- Un utilisateur peut ne jamais dépenser ou gagner des points #sym.arrow (0,n)
- Une transaction ne concerne qu'un utilisateur #sym.arrow (1,1)

== Entre Utilisateur --- Objet Cosmétique (Achat)

#block(breakable:false)[*Cardinalité :* Utilisateur (0,n) - Objet Cosmétique(0,n)]

#block(breakable :false)[*Justification: *]
- Un utilisateur peut acheter plusieurs objets cosmétiques #sym.arrow (0,n)
- Un objet cosmétiques peut appartenir à plusieurs utilisateurs #sym.arrow (0,n)

== Entre Utilisateur --- Objet Cosmétique (Activation)

#block(breakable:false)[*Cardinalité :* Utilisateur (0,n) - Objet Cosmétique(0,n)]

#block(breakable :false)[*Justification: *]
- Un utilisateur peut avoir plusieurs objets cosmétiques actifs (mais au plus un du même type) #sym.arrow (0,n)
- Un objet cosmétique peut être porté par plusieurs utilisateurs #sym.arrow (0,n)à
#pagebreak()
== Entre Utilisateur --- Evaluation 

#block(breakable:false)[*Cardinalité :* Utilisateur (0,n) - Evaluation(1,1)]

#block(breakable :false)[*Justification: *]
- Un utilisateur peut évaluer plusieurs résumés #sym.arrow (0,n)
- Une évaluation est rédigée par un seul et unique utilisateur #sym.arrow (1,1)

== Entre Utilisateur --- Cours 

#block(breakable:false)[*Cardinalité :* Utilisateur (1,n) - Cours(1,n)]

#block(breakable :false)[*Justification: *]
- Un utilisateur participe à minimum 1 cours #sym.arrow (1,n)
- Un cours est suivi par minimum 1 élève #sym.arrow (1,n)

== Entre Utilisateur --- Résumé 

#block(breakable:false)[*Cardinalité :* Utilisateur (0,n) - Résumé (1,1)]

#block(breakable :false)[*Justification: *]
- Un utilisateur peut rédiger 0 ou plusieurs résumés #sym.arrow (0,n)
- Un résumé est rédigé par un et un seul utilisateur #sym.arrow (1,1)

== Entre Résumé --- Cours 

#block(breakable:false)[*Cardinalité :* Résumé (1,1) - Cours(0,n)]

#block(breakable :false)[*Justification: *]
- Un résumé concerne un unique cours #sym.arrow (1,1)
- Il peut y avoir plusieurs résumé pour un cours #sym.arrow (0,n)




#bibliography("./bibliography.bib", full: true)