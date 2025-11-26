# logica.py
"""
Módulo de lógica de negocio para el Sistema de Gestión de Notas de Laboratorio
Contiene todas las funciones para manipular la estructura de datos
"""

# Almacenamiento interno: Lista de diccionarios
notas_laboratorio = []

# Contador global para IDs únicos
contador_id = 1


def agregar_nota(titulo, descripcion):
    """
    Agrega una nueva nota al sistema
    
    Args:
        titulo (str): Título de la nota
        descripcion (str): Descripción detallada de la nota
    
    Returns:
        dict: La nota creada con su ID asignado
    """
    global contador_id
    
    nueva_nota = {
        "id": contador_id,
        "titulo": titulo,
        "descripcion": descripcion
    }
    
    notas_laboratorio.append(nueva_nota)
    contador_id += 1
    
    return nueva_nota


def obtener_todas_notas():
    """
    Retorna todas las notas almacenadas
    
    Returns:
        list: Lista de diccionarios con todas las notas
    """
    return notas_laboratorio


def buscar_notas(termino_busqueda):
    """
    Función pura para filtrar/buscar notas por término
    
    Args:
        termino_busqueda (str): Término a buscar en título o descripción
    
    Returns:
        list: Lista filtrada de notas que coinciden con el término
    """
    if not termino_busqueda:
        return notas_laboratorio
    
    termino_lower = termino_busqueda.lower()
    
    notas_filtradas = [
        nota for nota in notas_laboratorio
        if termino_lower in nota["titulo"].lower() or 
           termino_lower in nota["descripcion"].lower()
    ]
    
    return notas_filtradas


def eliminar_nota(nota_id):
    """
    Elimina una nota por su ID
    
    Args:
        nota_id (int): ID de la nota a eliminar
    
    Returns:
        bool: True si se eliminó, False si no se encontró
    """
    global notas_laboratorio
    
    for i, nota in enumerate(notas_laboratorio):
        if nota["id"] == nota_id:
            notas_laboratorio.pop(i)
            return True
    
    return False


def obtener_nota_por_id(nota_id):
    """
    Obtiene una nota específica por su ID
    
    Args:
        nota_id (int): ID de la nota
    
    Returns:
        dict or None: La nota encontrada o None
    """
    for nota in notas_laboratorio:
        if nota["id"] == nota_id:
            return nota
    
    return None


def contar_notas():
    """
    Retorna el número total de notas
    
    Returns:
        int: Cantidad de notas almacenadas
    """
    return len(notas_laboratorio)