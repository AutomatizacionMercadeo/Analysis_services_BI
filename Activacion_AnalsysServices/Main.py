from datetime import datetime
import os
import time

from src.Email.EstructuraCorreos import Estructura_Exitoso, Estructura_Error
from src.Modules.EjecucionAzure import obtener_estado_analysis_services, pausar_analysis_services, reanudar_analysis_services

# Obtenemos la hora y el minuto actual
hora = datetime.now().hour
minute = datetime.now().minute

print(f"Hora actual: {hora}:{minute}")


# Es la hora de reanudar el servicio (6:00 AM)
if hora == 6 and 0 <= minute <= 5:
    try:
        resultado_reanudar = reanudar_analysis_services()
        print(f"Resultado de reanudar Analysis Services: {resultado_reanudar}")

        # Reintentos hasta 5 minutos (300 segundos), cada 10 segundos
        max_reintentos = 30
        reintento = 0
        while reintento < max_reintentos:
            estado = obtener_estado_analysis_services()
            print(f"Estado actual de Analysis Services en la mañana: {estado}")
            
            if estado.strip('"') == "Succeeded":
                print("Analysis Services reanudado correctamente.")
                Estructura_Exitoso()
                break
            elif estado.strip('"') in ["Resuming", "Provisioning"]:
                print("Esperando a que el estado sea 'Succeeded'...")
                time.sleep(10)
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
if hora == 17 and 30 <= minute <= 40:
    try:
        resultado_pausa = pausar_analysis_services()
        print(f"Resultado de pausar Analysis Services: {resultado_pausa}")

        # Reintentos hasta 5 minutos (300 segundos), cada 10 segundos
        max_reintentos = 30
        reintento = 0
        while reintento < max_reintentos:
            estado = obtener_estado_analysis_services()
            print(f"Estado actual de Analysis Services en la tarde: {estado}")
            
            if estado.strip('"') == "Paused":
                print("Analysis Services pausado correctamente.")
                Estructura_Exitoso()
                break
            elif estado.strip('"') == "Suspending":
                print("Esperando a que el estado sea 'Paused'...")
                time.sleep(10)
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