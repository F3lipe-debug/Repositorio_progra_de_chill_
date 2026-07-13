def leer_opcion():
    
    try:
        opcion = int(input("Ingrese opción: "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Debe seleccionar una opción válida")
            return None
    except ValueError:
        print("Debe seleccionar una opción válida")
        return None


def cupos_genero(genero, peliculas, cartelera):
    
    total_cupos = 0
    genero_lower = genero.lower()
    
    for codigo, info_pelicula in peliculas.items():
        if info_pelicula[1].lower() == genero_lower:
            total_cupos += cartelera[codigo][1]
    
    print(f"El total de cupos disponibles es: {total_cupos}")


def busqueda_precio(p_min, p_max, peliculas, cartelera):
    
    peliculas_encontradas = []
    
    for codigo, precio_cupos in cartelera.items():
        precio = precio_cupos[0]
        cupos = precio_cupos[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            titulo = peliculas[codigo][0]
            peliculas_encontradas.append(f"{titulo}--{codigo}")
    
    if peliculas_encontradas:
        peliculas_encontradas.sort()
        print(f"Las películas encontradas son: {peliculas_encontradas}")
    else:
        print("No hay películas en ese rango de precios.")


def buscar_codigo(codigo, peliculas):
    
    codigo_upper = codigo.upper()
    return codigo_upper in peliculas


def actualizar_precio(codigo, nuevo_precio, peliculas, cartelera):
    
    codigo_upper = codigo.upper()
    
    if buscar_codigo(codigo, peliculas):
        cartelera[codigo_upper][0] = nuevo_precio
        return True
    else:
        return False


def validar_codigo(codigo, peliculas):
    
    if not codigo or codigo.isspace():
        return False
    if buscar_codigo(codigo, peliculas):
        return False
    return True


def validar_titulo(titulo):
    
    if not titulo or titulo.isspace():
        return False
    return True


def validar_genero(genero):
    
    if not genero or genero.isspace():
        return False
    return True


def validar_duracion(duracion):
    
    try:
        duracion_int = int(duracion)
        return duracion_int > 0
    except ValueError:
        return False


def validar_clasificacion(clasificacion):
    
    return clasificacion in ['A', 'B', 'C']


def validar_idioma(idioma):
    
    if not idioma or idioma.isspace():
        return False
    return True


def validar_es_3d(es_3d):
    
    return es_3d.lower() in ['s', 'n']


def validar_precio(precio):
    
    try:
        precio_int = int(precio)
        return precio_int > 0
    except ValueError:
        return False


def validar_cupos(cupos):
    
    try:
        cupos_int = int(cupos)
        return cupos_int >= 0
    except ValueError:
        return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    
    codigo_upper = codigo.upper()
    
    peliculas[codigo_upper] = [titulo, genero, int(duracion), clasificacion, idioma, es_3d == 's']
    cartelera[codigo_upper] = [int(precio), int(cupos)]
    
    return True


def eliminar_pelicula(codigo, peliculas, cartelera):
    
    codigo_upper = codigo.upper()
    
    if buscar_codigo(codigo, peliculas):
        del peliculas[codigo_upper]
        del cartelera[codigo_upper]
        return True
    else:
        return False


def main():
    
    peliculas = {
        'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
        'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
        'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
        'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
        'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
        'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    }
    
    cartelera = {
        'P101': [5990, 40],
        'P102': [7990, 0],
        'P103': [4990, 25],
        'P104': [6990, 12],
        'P105': [8990, 8],
        'P106': [7490, 3],
    }
    
    while True:
        print()
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")
        
        opcion = leer_opcion()
        
        if opcion is None:
            continue
        
        if opcion == 1:
            genero = input("Ingrese género a consultar: ")
            cupos_genero(genero, peliculas, cartelera)
        
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, peliculas, cartelera)
        
        elif opcion == 3:
            repetir = True
            while repetir:
                codigo = input("Ingrese código de película: ")
                nuevo_precio_str = input("Ingrese nuevo precio: ")
                
                try:
                    nuevo_precio = int(nuevo_precio_str)
                    if nuevo_precio <= 0:
                        print("El precio debe ser mayor que cero")
                        continue
                    
                    if actualizar_precio(codigo, nuevo_precio, peliculas, cartelera):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                except ValueError:
                    print("El precio debe ser un número entero")
                    continue
                
                respuesta = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                if respuesta != 's':
                    repetir = False
        
        elif opcion == 4:
            codigo = input("Ingrese código de película: ")
            
            if not validar_codigo(codigo, peliculas):
                print("El código no es válido o ya existe")
                continue
            
            titulo = input("Ingrese título: ")
            if not validar_titulo(titulo):
                print("El título no es válido")
                continue
            
            genero = input("Ingrese género: ")
            if not validar_genero(genero):
                print("El género no es válido")
                continue
            
            duracion = input("Ingrese duración (minutos): ")
            if not validar_duracion(duracion):
                print("La duración no es válida")
                continue
            
            clasificacion = input("Ingrese clasificación: ").upper()
            if not validar_clasificacion(clasificacion):
                print("La clasificación no es válida")
                continue
            
            idioma = input("Ingrese idioma: ")
            if not validar_idioma(idioma):
                print("El idioma no es válido")
                continue
            
            es_3d = input("¿Es 3D? (s/n): ").lower()
            if not validar_es_3d(es_3d):
                print("Debe ingresar 's' o 'n'")
                continue
            
            precio = input("Ingrese precio: ")
            if not validar_precio(precio):
                print("El precio no es válido")
                continue
            
            cupos = input("Ingrese cupos: ")
            if not validar_cupos(cupos):
                print("Los cupos no son válidos")
                continue
            
            agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera)
            print("Película agregada")
        
        elif opcion == 5:
            codigo = input("Ingrese código de película: ")
            
            if eliminar_pelicula(codigo, peliculas, cartelera):
                print("Película eliminada")
            else:
                print("El código no existe")
        
        elif opcion == 6:
            print("Programa finalizado.")
            break


if __name__ == "__main__":
    main()
