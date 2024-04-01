from clasess.pueblo import Pueblo
from clasess.rutas import Rutas
from clasess.pokemon import Pokemon
from clasess.persona import Persona


ubicaciones = [Rutas("Ruta 1", Pokemon("squirtle", 80, 60, ["pistola agua", "burbuja", "placaje"])), Rutas("Ruta 2", Pokemon("caterpie", 56, 80, ["fortaleza", "electrotela"])), Pueblo("pueblo blanco", Persona("kayn", "45", "pueblo blanco", [Pokemon("squirtle", 60, 60, ["pistola agua", "burbuja", "placaje"]), Pokemon("caterpie", 60, 60, ["placaje", "fortaleza", "electrotela"])], 0, 1, 0)), Rutas("Ruta 3", Pokemon("Beedrill", 70, 100, ["pin misil", "placaje"])), Rutas("Ruta 4", Pokemon("Pidgey", 56, 100, ["placaje", "ataque ala"])), Pueblo("pueblo rojo", Persona("anna", "17", "pueblo rojo", [Pokemon("Beedrill", 76, 100, ["pin misil", "placaje"]), Pokemon("Pidgey", 76, 100, ["placaje", "ataque ala"])], 0, 2, 0)), Rutas("Ruta 5", Pokemon("Pikachu", 90, 100, ["electrotela", "ataque rapido"])), Rutas("Ruta 6", Pokemon("Sandshrew", 100, 100, ["rizo defensa", "arañazo"])), Pueblo("pueblo azul", Persona("diana", "35", "pueblo azul", [Pokemon("Pikachu", 110, 100, ["electrotela", "ataque rapido"]), Pokemon("Sandshrew", 110, 100, ["rizo defensa", "arañazo"])], 0, 3, 0)), Rutas("Ruta 7", Pokemon("charmander", 100, 100, ["arañazo", "ascuas", "lanzallamas"])), Rutas("Ruta 8", Pokemon("vulpix", 100, 100, ["ataque rapido", "ascuas", "lanzallamas"])), Pueblo(
    "pueblo amarillo", Persona("brook", "90", "pueblo amarillo", [Pokemon("charmander", 150, 100, ["arañazo", "ascuas", "lanzallamas"]), Pokemon("vulpix", 150, 100, ["ataque rapido", "ascuas", "lanzallamas"])], 0, 4, 0)), Rutas("Ruta 9", Pokemon("bulbasaur", 100, 100, ["latigo", "hoja afilada", "placaje"])), Rutas("Ruta 10", Pokemon("Zubat", 120, 100, ["ataque rapido", "ataque ala"])), Pueblo("pueblo verde", Persona("miguel", "17", "pueblo rojo", [Pokemon("bulbasaur", 200, 100, ["latigo", "hoja afilada", "placaje"]), Pokemon("Zubat", 200, 100, ["ataque rapido", "ataque ala"])], 0, 5, 0)), Rutas("Ruta 11", Pokemon("squirtle", 150, 60, ["pistola agua", "burbuja", "placaje"])), Rutas("Ruta 12", Pokemon("Pidgey", 160, 100, ["placaje", "ataque ala"])), Pueblo("pueblo marron", Persona("peruan_man", "21", "pueblo verde", [Pokemon("squirtle", 250, 60, ["pistola agua", "burbuja", "placaje"]), Pokemon("Pidgey", 250, 100, ["placaje", "ataque ala"])], 0, 6, 0)), Rutas("Ruta 13", Pokemon("Parasect", 160, 90, ["arañazo", "chirrido"])), Rutas("Ruta 14", Pokemon("Meowth", 200, 90, ["arañazo", "chirrido", "ataque rapido"])), Pueblo("liga", [Persona("voli", "89", "pueblo blanco", [Pokemon("charmander", 250, 80, ["arañazo", "ascuas", "lanzallamas"]), Pokemon("bulbasaur", 250, 80, ["latigo", "hoja afilada", "placaje"])], 0, 7, 0), Persona("diana", "25", "pueblo blanco", [Pokemon("Parasect", 250, 80, ["arañazo", "chirrido"]), Pokemon("caterpie", 250, 80, ["fortaleza", "electrotela"]), Pokemon("vulpix", 250, 80, ["ataque rapido", "ascuas", "lanzallamas"])], 0, 7, 0)])]
