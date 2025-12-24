from datetime import datetime, timedelta
import holidays

# Diccionario con los días de la semana en español
dias_semana = {
    0: "lunes",
    1: "martes",
    2: "miércoles",
    3: "jueves",
    4: "viernes",
    5: "sábado",
    6: "domingo"
}

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def obtener_dias(dias):
    # Normaliza todos los días de la lista de forma más eficiente
    return [normalize(dias_semana[dia]) for dia in dias]


def ValidarDiasFestivos():
    # Definir el país para las festividades (en este caso, Colombia)
    festivos = holidays.Colombia(years=2025)

    # Obtener la fecha actual y validar si es festivo
    hoy = datetime.now()
    dia = hoy.weekday()
    
    nombre_dia = normalize(dias_semana[dia])

    es_festivo = hoy.date() in festivos

    # Retornar la información solicitada
    return nombre_dia, es_festivo


if __name__ == "__main__":
    resultado = ValidarDiasFestivos()
    print(resultado)