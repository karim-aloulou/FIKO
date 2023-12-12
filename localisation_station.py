import geocoder
import webbrowser

def find_nearest_gas_station():
    # Obtenir la localisation actuelle
    g = geocoder.ip('me')
    current_location = g.latlng

    if current_location:
        latitude, longitude = current_location
        # Créer l'URL pour l'itinéraire vers la station-service la plus proche
        maps_url = f"https://www.google.com/maps/dir/?api=1&destination=gas+station&travelmode=driving&dir_action=navigate"

        # Ouvrir l'URL dans le navigateur par défaut
        webbrowser.open(maps_url)
    else:
        print("Localisation actuelle introuvable.")

# Exécuter la fonction
find_nearest_gas_station()
