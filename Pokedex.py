class Pokemon:  # Clase para representar un Pokémon
    def __init__(self, nombre, tipo, color, altura, peso, habilidad, numero_pokedex):
        self.nombre = nombre
        self.tipo = tipo
        self.color = color
        self.altura = altura
        self.peso = peso
        self.habilidad = habilidad
        self.numero_pokedex = numero_pokedex

    def descripcion(self):
        return f"N°{self.numero_pokedex}: {self.nombre}, Tipo: {self.tipo}, Color: {self.color}, Altura: {self.altura}m, Peso: {self.peso}kg, Habilidad: {self.habilidad}"

pokedex = []  # Lista para almacenar los Pokémon

def agregar_pokemon():
    nombre = input("Introduce el nombre del Pokémon: ")
    tipo = input("Introduce el tipo del Pokémon: ")
    color = input("Introduce el color del Pokémon: ")
    altura = float(input("Introduce la altura del Pokémon (en metros): "))
    peso = float(input("Introduce el peso del Pokémon (en kg): "))
    habilidad = input("Introduce la habilidad del Pokémon: ")
    numero_pokedex = int(input("Introduce el número en la Pokédex: "))

    for p in pokedex:
        if p.numero_pokedex == numero_pokedex:
            print("Este Pokémon ya está registrado en la Pokédex.")
            return
    
    pokedex.append(Pokemon(nombre, tipo, color, altura, peso, habilidad, numero_pokedex))
    print("¡El Pokémon ha sido agregado a la Pokédex!")

def modificar_pokemon():
    numero_pokedex = int(input("Introduce el número en la Pokédex del Pokémon a modificar: "))
    
    for p in pokedex:
        if p.numero_pokedex == numero_pokedex:
            p.nombre = input("Introduce el nuevo nombre del Pokémon: ")
            p.tipo = input("Introduce el nuevo tipo del Pokémon: ")
            p.color = input("Introduce el nuevo color del Pokémon: ")
            p.altura = float(input("Introduce la nueva altura del Pokémon (en metros): "))
            p.peso = float(input("Introduce el nuevo peso del Pokémon (en kg): "))
            p.habilidad = input("Introduce la nueva habilidad del Pokémon: ")
            print("El Pokémon ha sido modificado correctamente.")
            return
    
    print("No se ha encontrado el Pokémon en la Pokédex.")

def eliminar_pokemon():
    numero_pokedex = int(input("Introduce el número en la Pokédex del Pokémon a eliminar: "))

    for p in pokedex:
        if p.numero_pokedex == numero_pokedex:
            pokedex.remove(p)
            print("El Pokémon ha sido eliminado de la Pokédex.")
            return
    
    print("No se ha encontrado el Pokémon en la Pokédex.")

def mostrar_pokedex():
    if not pokedex:
        print("La Pokédex está vacía.")
    else:
        for p in pokedex:
            print(p.descripcion())

def main():
    while True:
        print("\n¿Qué quieres hacer? (Introduce el número de la acción deseada.)")
        print("1. Agregar un Pokémon")
        print("2. Modificar un Pokémon")
        print("3. Eliminar un Pokémon")
        print("4. Mostrar la Pokédex")
        print("5. Salir")

        entrada = int(input())

        if entrada == 1:
            agregar_pokemon()
        elif entrada == 2:
            modificar_pokemon()
        elif entrada == 3:
            eliminar_pokemon()
        elif entrada == 4:
            mostrar_pokedex()
        elif entrada == 5:
            break
        else:
            print("Entrada incorrecta, inténtalo de nuevo.")

if __name__ == "__main__":
    main()
