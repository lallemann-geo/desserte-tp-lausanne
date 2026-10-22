# Desserte en transports publics et population à Lausanne

Combien d’habitants de la commune de Lausanne vivent dans chaque niveau de qualité de desserte en transports publics (A à D, ou aucune) ?

## Résultat principal (population 2025)

| Classe | Habitants | Part |
|---|---|---|
| A (très bonne) | 101 185 | 67,7 % |
| B (bonne) | 39 193 | 26,2 % |
| C (moyenne) | 7 897 | 5,3 % |
| D (faible) | 783 | 0,5 % |
| Aucune | 486 | 0,3 % |

Au total, 94 % des habitants se trouvent en classe A ou B.

## Données (à télécharger, non incluses dans ce dépôt)

- ARE, niveaux de qualité de desserte en transports publics (GeoPackage) : https://data.geo.admin.ch/browser/index.html#/collections/ch.are.gueteklassen_oev. À placer dans `data/OeV_Gueteklassen_ARE.gpkg`.
- OFS, STATPOP, population et ménages par hectare, 2025 (GeoPackage) : https://data.geo.admin.ch/browser/index.html#/collections/ch.bfs.statistik-bevoelkerung_haushalte/items/statistik-bevoelkerung_haushalte_2025?.language=fr-CH&.asset=asset-statistik-bevoelkerung_haushalte_2025_2056-gpkg. À placer dans `data/statistik-bevoelkerung_haushalte_2025_2056.gpkg`.

## Installation et lancement

Testé avec Python 3.14.

1. Créer un environnement : `python -m venv .venv`
2. L’activer (Windows) : `.venv\Scripts\activate`
3. Installer les outils : `python -m pip install -r requirements.txt`
4. Placer les deux fichiers dans le dossier `data`.
5. Lancer : `python 02_population_lausanne.py`

Les résultats sont écrits dans le dossier `resultats` (un tableau CSV et une couche de carte GeoPackage).

## Méthode

1. On isole la commune de Lausanne (numéro OFS 5586).
2. On garde les carrés de 100 m (STATPOP) dont le centre est dans Lausanne.
3. Chaque carré reçoit la classe de la zone de desserte qui contient son centre.
4. On additionne les habitants (colonne `BBTOT`) par classe.

## Limites

- La distance à l’arrêt est mesurée à vol d’oiseau, sans tenir compte des rues ni de la pente.
- Seule une journée ouvrable de 6 h à 20 h est prise en compte (ni soirs, ni week-ends).
- Seuls les habitants sont comptés, pas les emplois ni les visiteurs.
- Un carré est compté en entier selon son centre : la somme des carrés (149 544) dépasse de 2,7 % le total communal (145 596).

## Fichiers

- `01_inspecter.py` : exploration des fichiers de données
- `02_population_lausanne.py` : analyse principale
- `resultats/` : résultats produits par l’analyse

## Pistes d’amélioration (non réalisées)

- Comparer la part des 65 ans et plus selon la classe de desserte
- Tester une autre règle de calcul (répartir chaque carré selon sa surface dans chaque zone)
- Mesurer la pente des carrés avec le modèle de terrain de swisstopo

## Auteur

Lucas Allemann. Données : Office fédéral du développement territorial et Office fédéral de la statistique.