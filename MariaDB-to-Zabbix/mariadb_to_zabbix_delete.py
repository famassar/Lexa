import configparser
import json
import requests
import mysql.connector
import logging
from datetime import datetime

class Host:
    def __init__(self, hostid, host_name):
        self.hostid=hostid
        self.host_name=host_name

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Database'], config['Zabbix'], config['Lexa']

def configure_logger(lexa_config):
    script_log=lexa_config['DELETE_LOG']
    logging.basicConfig(filename=script_log, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def log_message(message):
    logging.info(message)    

def get_hosts_from_database(db_config):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT hostid, host_name FROM lexa.alldata WHERE deleted=1;")
    hosts = [Host(**row) for row in cursor.fetchall()]
    cursor.close()
    connection.close()

    return hosts

def delete_host_in_database(db_config, hostname):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )
    cursor = connection.cursor()

    # Esempio di UPDATE per aggiornare il campo visible_name
    update_query = "DELETE FROM lexa.alldata WHERE host_name = '"+ hostname + "'"
        
    cursor.execute(update_query, (hostname))

    connection.commit()

    cursor.close()
    connection.close()

def delete_hosts_in_zabbix(zabbix_config, hosts, db_config):

    bearer = f"{zabbix_config['ZABBIX_TOKEN']}"
    defgroup = f"{zabbix_config['DEFAULT_GROUP']}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + bearer
        }

    for host in hosts:
        
        api_url = f"{zabbix_config['ZABBIX_URL']}/api_jsonrpc.php"

        # Creazione della richiesta JSON per la creazione dell'host su Zabbix
        payload ={
                "jsonrpc": "2.0",
                "method": "host.delete",
                "params": [
                    host.hostid
                ],
                "id": 1
                }
        
        # Invio della richiesta HTTP
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        
        # Gestione della risposta
        log_message(f"Host {host.host_name} deleting response: {response.text}")

        if response.status_code == 200:
            log_message(f"Host {host.host_name} deleted successfully")
            # Esempio di aggiornamento del campo visible_name dopo la creazione su Zabbix
            delete_host_in_database(db_config, host.host_name)
        else:
            log_message(f"Failed to delete host {host.host_name}: {response.text}")

def main():
    db_config, zabbix_config, lexa_config = load_config()
    configure_logger(lexa_config)

    hosts = get_hosts_from_database(db_config)
    delete_hosts_in_zabbix(zabbix_config, hosts, db_config)

if __name__ == "__main__":
    main()
