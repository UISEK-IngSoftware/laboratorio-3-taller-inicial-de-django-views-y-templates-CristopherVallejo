from django.urls import path
from . import views  # Importa las funciones de vistas de la aplicación

urlpatterns = [
    # 1. URL para la lista de Pokemones (Ruta raíz: /)
    path('', views.lista_pokemones, name='lista_pokemones'),
    
    # 2. URL para el detalle de un Pokémon (Ruta: /pokemon/ID/)
    # <int:pokemon_id> captura un número entero y lo pasa a la función detalle_pokemon
    path('pokemon/<int:pokemon_id>/', views.detalle_pokemon, name='detalle_pokemon'),
]