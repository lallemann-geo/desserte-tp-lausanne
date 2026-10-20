from pathlib import Path
import geopandas as gpd
import pandas as pd

dossier_data = Path("data")

for fichier in sorted(dossier_data.rglob("*")):
    if not fichier.is_file():
        continue

    print("=" * 60)
    print(fichier)

    extension = fichier.suffix.lower()

    if extension in [".gpkg", ".shp", ".geojson"]:
        carte = gpd.read_file(fichier)
        print("Nombre de lignes :", len(carte))
        print("Systeme de coordonnees :", carte.crs)
        print("Colonnes :", list(carte.columns))
        print(carte.head(3))

    elif extension == ".csv":
        tableau = pd.read_csv(fichier, nrows=3, sep=None, engine="python")
        print("Colonnes :", list(tableau.columns))
        print(tableau)