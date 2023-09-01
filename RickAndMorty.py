import requests
import os


# Hacer una solicitud a la API

response = requests.get("https://rickandmortyapi.com/api/episode")
data = response.json()  # Esto convierte la respuesta JSON en un diccionario de Python

response1 = requests.get("https://rickandmortyapi.com/api/character")
data1 = response1.json()



def limpiar_pantalla():
    return os.system('cls' if os.name == 'nt' else 'clear')



# Hacer una solicitud a la API para obtener el episodio con ID 19

while True:
    
    episode_id = input("Ingrese el id que quiera :D : ")
    print("\ningrese 1 para ver la informacion de Rick Sanchez\nIngrese 2 para ver la infomacionde de Morty Smith\nIngrese 3 para ver la informacion de Summer Smith\n")
    character_id = input("> ")
    
    episode_response = requests.get(f"https://rickandmortyapi.com/api/episode/{episode_id}")
    episode_data = episode_response.json()
    
    character_response1 = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
    character_data1 = character_response1.json()
    
    episode1_response = requests.get("https://rickandmortyapi.com/api/episode/51")
    episode1_data = episode1_response.json()
    
    episode2_response = requests.get("https://rickandmortyapi.com/api/episode/50")
    episode2_data = episode2_response.json()

    episode3_response = requests.get("https://rickandmortyapi.com/api/episode/49")
    episode3_data = episode3_response.json()
 
    if episode_id == "8":
        
        print()
        print("\nDatos del episodio con ID 8:\n")
        print("ID:", episode_data["id"])
        print()
        print("Nombre:", episode_data["name"])
        print("Fecha de emision:", episode_data["air_date"])
        print("Episodio:", episode_data["episode"])
        print()
        
        for url, character_url in enumerate(episode_data["characters"], start=1):
            
            print(f"{url}. {character_url}")

        
        num_episodes = len(episode_data["episode"])


        print()
        print(f"cantidad de espiodios del sujeto {episode_id}:", num_episodes)
        print("")
        limpiar_pantalla()
    

    elif episode_id == "19":

        print(f"\nDatos del episodio con ID {episode_id}\n")
        print("ID:", episode_data["id"])
        print()
        print("Name:", episode_data["name"])
        print("Air date:", episode_data["air_date"])
        print("Episode:", episode_data["episode"])
        print()

        print("URLs de los personajes")
        print("\nEsto son la cantidad de personajes que aparecen en el episodio\n")
        
        for url, character_url in enumerate(episode_data["characters"], start=1):
            
            print(f"{url}. {character_url}")

        num_episodes = len(episode_data["episode"])


        print()
        print(f"cantidad de espiodios del sujeto {episode_id}:", num_episodes)
        print()
        print("Created", episode_data["created"])
        input("")

        limpiar_pantalla()

    else:

        # Imprimir los datos del episodio con formato legible
        print(f"\nDatos del episodio con ID {episode_id}\n")
        print("Identificador:", episode_data["id"])
        print()
        print("Nombre:", episode_data["name"])
        print("Fecha de emision:", episode_data["air_date"])
        print("Episodio:", episode_data["episode"])
        print("\nEsto son la cantidad de personajes que aparecen en el episodio\n")

        for url, character_url in enumerate(episode_data["characters"], start=1):
            
            print(f"{url}. {character_url}")

        print()
        
        print("Enlace:", episode_data["url"])
        print()
        print("Nombre: ", character_data1["name"])
        print()
        
        for episodios, numero_episodios in enumerate(character_data1["episode"], start=1):
            print(f"{episodios}. {numero_episodios}")

        print()
        print("Fecha De Creacion", episode_data["created"])
        print()
        print("\nDatos del episodio 51\n")
        print("Identificador:", episode1_data["id"])
        print()
        print("Nombre:", episode1_data["name"])
        print("Fecha de emision:", episode1_data["air_date"])
        print("Episodio:", episode1_data["episode"])
        
        print("\nEsto son la cantidad de personajes que aparecen en el episodio\n")
        for episodios_finales, numero_episodios_finales in enumerate(episode1_data["characters"], start=1):
            print(f"{episodios_finales}. {numero_episodios_finales}")
        
        print()
        print("Fecha De Creacion", episode2_data["created"])
        print()
        print(f"\nDatos del episodio 50\n")
        print("Identificador:", episode2_data["id"])
        print()
        print("Nombre:", episode2_data["name"])
        print("Fecha de emision:", episode2_data["air_date"])
        print("Episodio:", episode2_data["episode"])
        print("\nEsto son la cantidad de personajes que aparecen en el episodio\n")
        for episodios_finales, numero_episodios_finales in enumerate(episode2_data["characters"], start=1):
            print(f"{episodios_finales}. {numero_episodios_finales}")

        print()
        print("Fecha De Creacion", episode3_data["created"])
        print()
        
        print(f"\nDatos del episodio 49\n")
        print("Identificador:", episode3_data["id"])
        
        print()
        print("Nombre:", episode3_data["name"])
        print("Fecha de emision:", episode3_data["air_date"])
        print("Episodio:", episode3_data["episode"])
        print("\nEsto son la cantidad de personajes que aparecen en el episodio\n")
        for episodios_finales, numero_episodios_finales in enumerate(episode3_data["characters"], start=1):
            print(f"{episodios_finales}. {numero_episodios_finales}")

        
        input("")
        limpiar_pantalla()


    