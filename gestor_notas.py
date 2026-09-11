def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print(" 1. Añadir una nota")
    print(" 2. Ver todas las notas")
    print(" 3. Buscar una nota por palabra clave")
    print(" 4. Eliminar una nota")
    print(" 5. Salir")


def ver_notas(notas):
    print("\n--- TUS NOTAS ---")
    
    if len(notas) == 0:
        print("No tienes notas guardadas.")
        return
    
    total_notas = len(notas)
    suma_caracteres = 0

    for nota in notas:
        suma_caracteres += len(nota['contenido'])
    
    media_contenido = suma_caracteres / total_notas
    
    for i, nota in enumerate(notas, start=1):
        print(f"{i}. Título: {nota['titulo']}")
        print(f"    Contenido: {nota['contenido']}")

    print("\nESTADÍSTICAS DEL GESTOR:")
    print(f"Total de notas: {total_notas}")
    print(f"Longitud media del contenido: {media_contenido:.2f} caracteres")


def añadir_nota(notas):
    print("\n--- NUEVA NOTA ---")
    titulo = input("Introduce el título de la nota: ").strip()
    
    nota_existente = None
    for n in notas:
        if n['titulo'].lower() == titulo.lower():
            nota_existente = n
            break            
            
    if nota_existente:
        print("Ya existe una nota con ese título.")
        sobreescribir = input("¿Quieres sobrescribirla? (s/n): ").lower().strip()
        if sobreescribir != 's':
            print("Operación cancelada.")
            return
        
    contenido = input("Introduce el contenido de la nota: ")
        
    confirmar = input(f"¿Guardar la nota '{titulo}'? (s/n): ").lower().strip()
    
    if confirmar == 's':
        if nota_existente:
            nota_existente['contenido'] = contenido
            print("Nota actualizada correctamente.") 
        else:
            nueva_nota = {"titulo": titulo, "contenido": contenido}
            notas.append(nueva_nota)
            print("Nota guardada correctamente.")
    else:
        print("Nota descartada.")


def buscar_nota(notas):
    print("\n--- BUSCAR NOTA ---")
    
    if not notas:
        print("No hay notas guardadas para realizar una búsqueda.")
        return

    palabra_clave = input("Introduce la palabra que quieres buscar: ").lower().strip()
    encontrada = False

    print(f"\nResultados para '{palabra_clave}':")

    for nota in notas:
        if palabra_clave in nota['titulo'].lower() or palabra_clave in nota['contenido'].lower():
            print(f"- Título: {nota['titulo']}")
            print(f"  Contenido: {nota['contenido']}")
            encontrada = True
    
    if not encontrada:
        print("No se han encontrado notas que coincidan con esa palabra.")


def eliminar_nota(notas):
    print("\n--- ELIMINAR NOTA ---")
    
    if not notas:
        print("No hay notas para eliminar.")
        return

    for i, nota in enumerate(notas, start=1):
        print(f"{i}. {nota['titulo']}")

    try:
        indice_usuario = int(input("\nIntroduce el número de la nota a eliminar: "))
        indice_real = indice_usuario - 1

        if 0 <= indice_real < len(notas):
            nota_a_borrar = notas[indice_real]
            confirmar = input(f"¿Seguro que quieres borrar '{nota_a_borrar['titulo']}'? (s/n): ").lower().strip()
            
            if confirmar == 's':
                notas.pop(indice_real)
                print("Nota eliminada con éxito.")
            else:
                print("Operación cancelada.")
        else:
            print("Error: El número introducido no corresponde a ninguna nota.")
            
    except ValueError:
        print("Error: Debes introducir un número válido.")       
            

def main():
    notas = []
    continuar = True
    
    print("¡Bienvenido al Gestor de Notas!")
    
    while continuar:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()
    
        if opcion == "1":
            añadir_nota(notas)
        elif opcion == "2":    
            ver_notas(notas)
        elif opcion == "3":
            buscar_nota(notas)
        elif opcion == "4":
            eliminar_nota(notas)
        elif opcion == "5":    
            print("Saliendo de la aplicación...")
            continuar = False
        else:
            print("Opción no válida. Introduce un número del 1 al 5.")


if __name__ == "__main__":
    main()
    