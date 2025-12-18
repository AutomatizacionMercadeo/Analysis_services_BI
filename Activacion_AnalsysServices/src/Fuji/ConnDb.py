import oracledb
from src.Fuji.get_data import get_datos_id

def conn_db(id_unico):
    
    data = get_datos_id(id_unico)

    if data is None:
        return None, None, None
    else:
        # Extraer las variables del objeto data para la conexión a la base de datos
        pwd = data['tenant_id'] 
        user_Redi = data['user_sig']
        pass_Redi = data['pass_sig']
        
        return user_Redi, pass_Redi, pwd


def conn_db_SFTP(id_unico):
    
    data = get_datos_id(id_unico)

    if data is None:
        return None, None, None, None
    else:
        # Extraer las variables del objeto data para la conexión a la base de datos
        Host_SFTP = data['client_id'] 
        user_SFTP = data['tenant_id']
        pass_SFTP = data['secret_id']
        port_SFTP = data['server_smtp']
        
        return Host_SFTP, user_SFTP, pass_SFTP, port_SFTP


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

