import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time, sys

from src.Fuji.ConnDb import conn_db_correo


# Esta es la funcion para enviar correos exitosos
def Envio_Correo(asunto, cuerpo):

    server_SMTP, port_SMTP, user_SMTP, pass_SMTP = conn_db_correo(id_unico='1')

    # Destinatario principal
    destinatario = 'juan.ortiz@gruporeditos.com, jose.chaverra@gruporeditos.com, cristian.avendano@gruporeditos.com'
    lista_destinatarios = destinatario.split(', ') 

    # Crear el objeto del mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = user_SMTP
    mensaje['To'] = ', '.join(lista_destinatarios)
    mensaje['Subject'] = asunto

    # Adjuntar el cuerpo del correo como texto HTML
    mensaje.attach(MIMEText(cuerpo, 'html'))

    # Establecer la conexión SMTP y enviar el correo
    MAX_INTENTOS = 5
    ESPERA_SEGUNDOS = 30

    for intento in range(1, MAX_INTENTOS + 1):
        try:
            with smtplib.SMTP(server_SMTP, port_SMTP) as servidor:
                servidor.ehlo()
                servidor.starttls()
                servidor.ehlo()
                servidor.login(user_SMTP, pass_SMTP)
                servidor.sendmail(user_SMTP, lista_destinatarios, mensaje.as_string())
                print('Correo enviado exitosamente.')
                break  # Si se envía correctamente, salimos del bucle

        except smtplib.SMTPException as e:
            print(f"Error al enviar el correo (Intento {intento}/{MAX_INTENTOS}): {e}")
            if intento < MAX_INTENTOS:
                print(f"Reintentando en {ESPERA_SEGUNDOS} segundos...")
                time.sleep(ESPERA_SEGUNDOS)
            else:
                print("No se pudo enviar el correo después de varios intentos.")
                sys.exit(1)