from src.Email.EnviarCorreo import Envio_Correo


def Estructura_Exitoso(estado):
    asunto = "Ejecución Exitosa - Azure Analysis Services"

    body = (
        "<html>"
        "<body>"
        "<p>Estimado usuario,</p>"
        "<p>La ejecución del proceso en <b>Azure Analysis Services</b> se realizó correctamente.<br>"
        "No se detectaron errores durante la operación.</p>"
        f"<p><b>Estado final:</b> {estado}</p>"
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
