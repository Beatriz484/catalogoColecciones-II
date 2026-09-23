# catalog.py

from validations import (
    validate_price,
    validate_status,
    validate_description,
    validate_not_empty,
    validate_catalog
)

def add_piece(piece_id, name, category, price, status, description):
    """Agrega y retorna un diccionario con los datos validados de la pieza."""
    validate_not_empty(piece_id, "id")
    validate_not_empty(name, "name")
    validate_not_empty(category, "category")
    
    validated_price = validate_price(price)
    validated_status = validate_status(status)
    validated_desc = validate_description(description)
    
    return {
        "id": str(piece_id).strip(),
        "name": str(name).strip(),
        "category": str(category).strip(),
        "price": validated_price,
        "status": validated_status,
        "description": validated_desc
    }

def list_pieces(catalog):
    """Retorna una lista con los nombres de todas las piezas."""
    try:
        validate_catalog(catalog)
    except TypeError:
        return []
    
    if not catalog:
        return []
        
    return [piece["name"] for piece in catalog]

def find_piece_by_id(catalog, piece_id):
    """Busca y retorna el diccionario de la pieza o None si no existe."""
    try:
        validate_catalog(catalog)
    except TypeError:
        return None
        
    for piece in catalog:
        if piece.get("id") == str(piece_id):
            return piece
    return None

def remove_piece(catalog, piece_id):
    """Elimina una pieza por su ID. Lanza excepción si no se encuentra."""
    validate_catalog(catalog)
    piece = find_piece_by_id(catalog, piece_id)
    if not piece:
        raise ValueError(f"La pieza con ID '{piece_id}' no fue encontrada en el catálogo.")
    
    catalog.remove(piece)
    return True

def get_catalog_summary(catalog):
    """Retorna un diccionario con la cantidad de piezas por categoría."""
    validate_catalog(catalog)
    summary = {}
    for piece in catalog:
        cat = piece.get("category", "Desconocida")
        summary[cat] = summary.get(cat, 0) + 1
    return summary

def get_pieces_by_category(catalog, category):
    """Retorna una lista con los nombres de las piezas de una categoría."""
    validate_catalog(catalog)
    matching = []
    for piece in catalog:
        if piece.get("category", "").lower() == str(category).lower():
            matching.append(piece["name"])
    return matching

def piece_exists(catalog, piece_id):
    """Retorna True si la pieza existe, o False en caso contrario."""
    try:
        validate_catalog(catalog)
    except TypeError:
        return False
    return find_piece_by_id(catalog, piece_id) is not None

def filter_by_status(catalog, status):
    """Filtra y retorna las piezas que coincidan con un estado permitido."""
    validated_status = validate_status(status)
    validate_catalog(catalog)
    return [piece for piece in catalog if piece.get("status") == validated_status]

def filter_by_min_price(catalog, min_price):
    """Filtra piezas cuyo precio sea mayor al valor indicado."""
    validate_catalog(catalog)
    try:
        min_p = float(min_price)
    except (ValueError, TypeError):
        raise ValueError("El precio mínimo debe ser un valor numérico.")
        
    return [piece for piece in catalog if piece.get("price", 0) > min_p]

def get_average_price(catalog):
    """Calcula y retorna el precio promedio de las piezas del catálogo."""
    validate_catalog(catalog)
    if not catalog:
        return 0.0
    
    total = sum(piece.get("price", 0) for piece in catalog)
    return total / len(catalog)