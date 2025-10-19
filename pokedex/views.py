from django.shortcuts import render

# --- DATOS SIMULADOS (Reemplazando los Modelos de Django) ---
POKEMONES = [
    {'id': 1, 'nombre': 'Bulbasaur', 'tipo': 'Planta/Veneno', 'descripcion': 'Pokémon semilla. Fuerte contra agua, débil contra fuego.', 'imagen_nombre': 'bulbasaur.png'},
    {'id': 4, 'nombre': 'Charmander', 'tipo': 'Fuego', 'descripcion': 'Pokémon lagarto. Fuerte contra planta, débil contra agua.', 'imagen_nombre': 'charmander.png'},
    {'id': 7, 'nombre': 'Squirtle', 'tipo': 'Agua', 'descripcion': 'Pokémon tortuguita. Fuerte contra fuego, débil contra eléctrico.', 'imagen_nombre': 'squirtle.png'},
    {'id': 25, 'nombre': 'Pikachu', 'tipo': 'Eléctrico', 'descripcion': 'Pokémon ratón. Fuerte contra agua, débil contra tierra.', 'imagen_nombre': 'pikachu.png'},
]

# --- VISTA 1: Lista de Pokemones ---
def lista_pokemones(request):
    """
    Muestra la lista de Pokemones.
    """
    contexto = {
        'titulo': 'Pokédex - Lista Completa',
        'pokemones': POKEMONES,
    }
    # Renderiza la plantilla 'pokedex/lista.html'
    return render(request, 'pokedex/lista.html', contexto)


# --- VISTA 2: Detalle de un Pokémon ---
def detalle_pokemon(request, pokemon_id):
    """
    Muestra los detalles de un Pokémon específico por su ID.
    """
    # Buscar el Pokémon en la lista por su 'id'
    pokemon_seleccionado = next((p for p in POKEMONES if p['id'] == pokemon_id), None)
    
    # Manejo de error si el Pokémon no existe (simulación de 404)
    if pokemon_seleccionado is None:
        contexto_error = {
            'titulo': 'Pokémon No Encontrado',
            'mensaje': f'El Pokémon con ID #{pokemon_id} no existe en esta Pokédex.',
            'id': pokemon_id
        }
        return render(request, 'pokedex/404.html', contexto_error, status=404)

    contexto = {
        'titulo': f"Detalles de {pokemon_seleccionado['nombre']}",
        'pokemon': pokemon_seleccionado,
    }
    # Renderiza la plantilla 'pokedex/detalle.html'
    return render(request, 'pokedex/detalle.html', contexto)