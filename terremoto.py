#---------------------------------------------------------------------------------------
"""Programa em Python para listar os terremotos acima de 6 graus nos ultimos 30 dias."""
# Fonte dos dados: https://earthquake.usgs.gov/ - USGS
# Autor: Marcelo Pinheiro - [Twitter](http://twitter.com/mpinheir)
#---------------------------------------------------------------------------------------
import urllib.request
import json

URLTOACESS = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"
with urllib.request.urlopen(URLTOACESS) as url:
    DATA = json.loads(url.read().decode())
    NUMERO_DE_TERREMOTOS = DATA['metadata']['count']
    print("Terremotos acima de 6 graus nos ultimos 30 dias:")
    print("================================================")
    for i in range(0, NUMERO_DE_TERREMOTOS-1):
        Magnitude = DATA['features'][i]['properties']['mag']
        if Magnitude > 6:
            Epicentro = DATA['features'][i]['properties']['place']
            print(Epicentro, '--> Magnitude:', Magnitude)
