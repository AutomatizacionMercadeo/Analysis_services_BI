from datetime import datetime
import os
import time

from src.Email.EstructuraCorreos import Estructura_Exitoso, Estructura_Error
from src.Modules.EjecucionAzure import (
    obtener_estado_analysis_services,
    pausar_analysis_services,
    reanudar_analysis_services,
    az_login_service_principal,
)

# Obtenemos la hora y el minuto actual
hora = datetime.now().hour
minute = datetime.now().minute

print(f"Hora actual: {hora}:{minute}")


# Es la hora de reanudar el servicio (6:00 AM)
if hora == 6 and 0 <= minute <= 5:
    try:
        # Login en Azure antes de intentar reanudar
        login_result = az_login_service_principal()
        if login_result is not True:
            print(f"Error en az login: {login_result}")
            Estructura_Error(f"Error en az login: {login_result}")
            raise SystemExit(1)

        resultado_reanudar = reanudar_analysis_services()
        print(f"Resultado de reanudar Analysis Services: {resultado_reanudar}")

        # Reintentos hasta 5 minutos (300 segundos), cada 10 segundos
        max_reintentos = 10
        reintento = 0
        while reintento < max_reintentos:
            estado = obtener_estado_analysis_services()
            print(f"Estado actual de Analysis Services en la mañana: {estado}")
            
            if estado.strip('"') == "Succeeded":
                print("Analysis Services reanudado correctamente.")
                Estructura_Exitoso(estado.strip('"'))
                break
            elif estado.strip('"') in ["Resuming", "Provisioning"]:
                print("Esperando a que el estado sea 'Succeeded'...")
                time.sleep(30)
                reintento += 1
            else:
                print(f"Estado inesperado: {estado}")
                break
        else:
            print("No se logró reanudar el servicio en 5 minutos.")
            Estructura_Error(f"No se logró reanudar el servicio en 5 minutos. Último estado: {estado}")
    
    except Exception as e:
        print(f"Error al reanudar Analysis Services: {e}")
        Estructura_Error(e)


# Es la hora de pausar el servicio (6:00 PM)
if hora == 11 and 0 <= minute <= 30:
    try:
        # Login en Azure antes de intentar pausar
        login_result = az_login_service_principal()
        if login_result is not True:
            print(f"Error en az login: {login_result}")
            Estructura_Error(f"Error en az login: {login_result}")
            raise SystemExit(1)

        resultado_pausa = pausar_analysis_services()
        print(f"Resultado de pausar Analysis Services: {resultado_pausa}")

        # Reintentos hasta 5 minutos (300 segundos), cada 10 segundos
        max_reintentos = 10
        reintento = 0
        while reintento < max_reintentos:
            estado = obtener_estado_analysis_services()
            print(f"Estado actual de Analysis Services en la tarde: {estado}")
            
            if estado.strip('"') == "Paused":
                print("Analysis Services pausado correctamente.")
                Estructura_Exitoso(estado.strip('"'))
                break
            elif estado.strip('"') == "Suspending":
                print("Esperando a que el estado sea 'Paused'...")
                time.sleep(30)
                reintento += 1
            else:
                print(f"Estado inesperado: {estado}")
                break
        else:
            print("No se logró pausar el servicio en 5 minutos.")
            Estructura_Error(f"No se logró pausar el servicio en 5 minutos. Último estado: {estado}")
    
    except Exception as e:
        print(f"Error al pausar Analysis Services: {e}")
        Estructura_Error(e)
