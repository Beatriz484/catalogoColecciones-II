# validations.py

VALID_STATUSES = {"disponible", "reservada", "vendida"}

def validate_price(price):
    """Valida que el precio sea numérico y mayor que cero."""
    try:
        numeric_price = float(price)
    except (ValueError, TypeError):
        raise ValueError("El precio debe ser un valor numérico.")
    
    if numeric_price <= 0:
        raise ValueError("El precio debe ser mayor que cero.")
    return numeric_price

def validate_status(status):
    """Valida que el estado esté entre los permitidos."""
    if not isinstance(status, str):
        raise ValueError("El estado debe ser una cadena de texto.")
    
    clean_status = status.strip().lower()
    if clean_status not in VALID_STATUSES:
        raise ValueError(f"Estado no válido. Debe ser uno de: {list(VALID_STATUSES)}")
    return clean_status

def validate_description(description):
    """Valida que la descripción contenga 'usada' o 'certificada'."""
    if not isinstance(description, str):
        raise ValueError("La descripción debe ser una cadena de texto.")
    
    desc_lower = description.lower()
    if "usada" not in desc_lower and "certificada" not in desc_lower:
        raise ValueError("La descripción debe contener obligatoriamente las palabras 'usada' o 'certificada'.")
    return description.strip()

def validate_not_empty(value, field_name):
    """Valida que un valor obligatorio no esté vacío."""
    if value is None or (isinstance(value, str) and not value.strip()):
        raise ValueError(f"El campo '{field_name}' no puede estar vacío.")
    return str(value).strip() if isinstance(value, str) else value

def validate_catalog(catalog):
    """Valida que el argumento recibido sea una lista."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
