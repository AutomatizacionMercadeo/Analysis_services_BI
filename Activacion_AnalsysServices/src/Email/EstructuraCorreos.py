from src.Email.EnviarCorreo import Envio_Correo


def _mensaje_servicio(servicio_estado):
    if not servicio_estado:
        return ""

    estado = str(servicio_estado).lower()
    if estado in ("pausado", "se pauso", "pausar"):
        return "<p><b>Nota:</b> Se pausó el servicio.</p>"
    if estado in ("levantado", "activo", "reanudado", "se reanudo", "se reanudó"):
        return "<p><b>Nota:</b> El servicio ya está levantado.</p>"
    # Valor por defecto si no coincide
    return f"<p><b>Nota:</b> Estado del servicio: {servicio_estado}</p>"


def Estructura_Exitoso(estado, servicio_estado=None):
    asunto = "Ejecución Exitosa - Azure Analysis Services"

    nota_servicio = _mensaje_servicio(servicio_estado)

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


def Estructura_Error(error, servicio_estado=None):
    asunto = "Error en Ejecución - Azure Analysis Services"

    nota_servicio = _mensaje_servicio(servicio_estado)

    body = (
        "<html>"
        "<body>"
        "<p>Estimado usuario,</p>"
        "<p>Se ha producido un <b>error</b> durante la ejecución del proceso en <b>Azure Analysis Services</b>.</p>"
        f"<p><b>Detalle del error:</b><br>{error}</p>"
        f"{nota_servicio}"
        "<p>Por favor, revise los detalles y contacte al equipo de soporte si es necesario.</p>"
        "<p>Saludos,<br>Equipo de Automatización</p>"
        "</body>"
        "</html>"
    )

    Envio_Correo(asunto, body)
