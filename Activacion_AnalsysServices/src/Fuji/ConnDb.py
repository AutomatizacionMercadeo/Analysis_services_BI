import oracledb
from src.Fuji.get_data import get_datos_id

def conn_azure(id_unico):
    
    data = get_datos_id(id_unico)

    if data is None:
        return None, None, None
    else:
        # Extraer las variables del objeto data para la conexión a la base de datos
        client = data['user_sig'] 
        tenant = data['pass_sig']
        client_secret = data['url']
        
        return client, tenant, client_secret


def conn_db_correo(id_unico):
    
    data = get_datos_id(id_unico)

    if data is None:
        return None, None, None, None
    else:
        server_Redi = data['server_smtp']
        port_Redi = data['port_smtp']
        user_Redi = data['user_smtp']
        passSmtp_Redi = data['pass_smtp']

        return server_Redi, port_Redi, user_Redi, passSmtp_Redi

