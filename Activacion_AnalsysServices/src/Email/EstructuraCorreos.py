from src.Email.EnviarCorreo import Envio_Correo


def _mensaje_servicio(servicio_estado):
    if not servicio_estado:
        return ""

    estado = str(servicio_estado)
    if estado in ("Paused"):
        return "<p><b>Nota:</b> Se pausó el servicio.</p>"
    if estado in ("Succeeded"):
        return "<p><b>Nota:</b> El servicio ya está levantado.</p>"
    # Valor por defecto si no coincide
    return f"<p><b>Nota:</b> Estado del servicio: {servicio_estado}</p>"


def Estructura_Exitoso(estado):
    asunto = "Ejecución Exitosa - Azure Analysis Services"

    nota_servicio = _mensaje_servicio(estado)

    body = (
        "<html>"
        "<body>"
        "<p>Estimado usuario,</p>"
        "<p>La ejecución del proceso en <b>Azure Analysis Services</b> se realizó correctamente.<br>"
        "No se detectaron errores durante la operación.</p>"
        f"<p><b>Estado final:</b> {estado}</p>"
        f"{nota_servicio}"
        "<p>Saludos,<br>Equipo de Automatización</p>"
        "</body>"
        "</html>"
    )

    Envio_Correo(asunto, body)


def Estructura_Error(error):
    asunto = "Error en Ejecución - Azure Analysis Services"

    body = (
        "<html>"
        "<body>"
        "<p>Estimado usuario,</p>"
        "<p>Se ha producido un <b>error</b> durante la ejecución del proceso en <b>Azure Analysis Services</b>.</p>"
        f"<p><b>Detalle del error:</b><br>{error}</p>"
        "<p>Por favor, revise los detalles y contacte al equipo de soporte si es necesario.</p>"
        "<p>Saludos,<br>Equipo de Automatización</p>"
        "</body>"
        "</html>"
    )

    Envio_Correo(asunto, body)


def Estructura_festivo(estado):
    asunto = "Día Festivo - Azure Analysis Services"

    nota_servicio = _mensaje_servicio(estado)

    body = (
        "<html>"
        "<body>"
        "<p>Estimado usuario,</p>"
        "<p>Hoy es <b>día festivo</b> en Colombia.<br>"
        "No se realiza ninguna acción sobre Azure Analysis Services por este motivo.</p>"
        f"<p><b>Estado final:</b> {estado}</p>"
        f"{nota_servicio}"
        "<p>Saludos,<br>Equipo de Automatización</p>"
        "</body>"
        "</html>"
    )

    Envio_Correo(asunto, body)