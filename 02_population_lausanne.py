import geopandas as gpd

FICHIER_POP = "data/statistik-bevoelkerung_haushalte_2025_2056.gpkg"
COUCHE_COMMUNES = "statistik-bevoelkerung_haushalte_2025_gmde_2056"
COUCHE_HECTARES = "statistik-bevoelkerung_haushalte_2025_ha_2056"

# 1. Le contour de Lausanne
communes = gpd.read_file(FICHIER_POP, layer=COUCHE_COMMUNES)
lausanne = communes[communes["GDENR"] == 5586]
contour = lausanne.geometry.iloc[0]

# 2. Les hectares qui touchent Lausanne
hectares = gpd.read_file(FICHIER_POP, layer=COUCHE_HECTARES, mask=contour)

# 3. On garde ceux dont le centre est dans Lausanne
centres = hectares.geometry.centroid
hectares_lausanne = hectares[centres.within(contour)]

# 4. Verification
print("Hectares gardes :", len(hectares_lausanne))
print("Habitants (somme des hectares) :", hectares_lausanne["BBTOT"].sum())
print("Habitants (commune) :", lausanne["BBTOT"].iloc[0])

# 5. Les zones de desserte (celles qui touchent Lausanne)
desserte = gpd.read_file("data/OeV_Gueteklassen_ARE.gpkg", mask=contour)

# 6. Chaque hectare prend la classe de la zone qui contient son centre
points = hectares_lausanne.copy()
points["geometry"] = points.geometry.centroid
croise = gpd.sjoin(points, desserte[["KLASSE", "geometry"]], how="left", predicate="within")

# 7. Un hectare hors de toute zone n'a pas de classe
croise["KLASSE"] = croise["KLASSE"].fillna("Aucune")

# 8. Verification : aucun hectare ne doit etre compte deux fois
print("Hectares apres croisement :", len(croise))

# 9. Habitants par classe
resultat = croise.groupby("KLASSE")["BBTOT"].sum()
print(resultat)
print("Total :", resultat.sum())
print((resultat / resultat.sum() * 100).round(1))