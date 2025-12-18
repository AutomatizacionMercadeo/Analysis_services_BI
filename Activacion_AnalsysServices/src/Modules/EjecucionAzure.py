import subprocess, os
from dotenv import load_dotenv

load_dotenv()

ruta = os.getenv('RUTA_AZURE')
grupo = os.getenv('GROUP_AZURE')
servicio = os.getenv('SERVICES_AZURE')

AZ_CMD = r'"C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd"'

def obtener_estado_analysis_services():
	"""Obtiene el estado del servidor Analysis Services usando Azure CLI."""
	try:
		comando = f'{AZ_CMD} resource show --name {servicio} --resource-group {grupo} --resource-type Microsoft.AnalysisServices/servers --query properties.state'
		resultado = subprocess.run(comando, capture_output=True, text=True, shell=True)
		return resultado.stdout.strip()
	except Exception as e:
		return f"Error al obtener estado: {str(e)}"


def pausar_analysis_services():
	"""Pausa el servidor Analysis Services usando Azure CLI."""
	try:
		comando = f'{AZ_CMD} rest --method post --uri "{ruta}/suspend?api-version=2017-08-01"'
		resultado = subprocess.run(comando, capture_output=True, text=True, shell=True)
		return resultado.stdout.strip()
	except Exception as e:
		return f"Error al pausar: {str(e)}"


def reanudar_analysis_services():
	"""Reanuda el servidor Analysis Services usando Azure CLI."""
	try:
		comando = f'{AZ_CMD} rest --method post --uri "{ruta}/resume?api-version=2017-08-01"'
		resultado = subprocess.run(comando, capture_output=True, text=True, shell=True)
		return resultado.stdout.strip()
	except Exception as e:
		return f"Error al reanudar: {str(e)}"
