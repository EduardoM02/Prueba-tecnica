from decimal import Decimal, InvalidOperation


def validar_importe(importe):
    try:
        importe = Decimal(str(importe))

        if not importe.is_finite():
            return "El importe no es un número finito"

        if importe <= 0:
            return "El importe debe ser positivo"

        if importe.as_tuple().exponent < -2:
            return "El importe excede los 2 decimales permitidos"

        return None

    except (InvalidOperation, ValueError, TypeError):
        return "El importe debe ser numérico"


def validar_clabe(clabe):
    if not isinstance(clabe, str):
        return "La CLABE debe ser texto"

    if not clabe.isdigit():
        return "La CLABE contiene caracteres no numéricos"

    if len(clabe) != 18:
        return f"La CLABE tiene {len(clabe)} dígitos (debe tener 18)"

    return None


def validar_beneficiario(beneficiario):
    if not isinstance(beneficiario, str) or not beneficiario.strip():
        return "El beneficiario está vacío"

    return None
