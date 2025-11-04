import mysql.connector
import json
import configparser
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--osname", help="Operating System Name")
parser.add_argument("-v", "--osver", help="Operating System Version")
parser.add_argument("-s", "--subnet", help="Subnet")
parser.add_argument("-u", "--user", help="Username")

args = parser.parse_args()

p_so_name = args.osname
p_so_ver = args.osver
p_subnet = args.subnet
p_user = args.user

# Lettura della configurazione dal file .ini
config = configparser.ConfigParser()
config.read('/opt/lexa/glpi-to-rundeck/config.ini')

# Configurazione della connessione al database
db_config = {
    'user': config['database']['user'],
    'password': config['database']['password'],
    'host': config['database']['host'],
    'database': config['database']['database']
}

# Connessione al database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Query per estrarre i dati dalla tabella
query = "SELECT hostname,ip FROM lexa_rundeck WHERE os_name LIKE '%" + p_so_name + "%' AND os_name LIKE '%" + p_so_ver + "%' AND subnet LIKE '" + p_subnet + "%' AND status NOT LIKE 'Spento'"
# Esecuzione della query
cursor.execute(query)

# Estrazione dei risultati
nodes = []
for (nodename, ip) in cursor:
    node = {
        "nodename": nodename,
        "hostname": ip,
        "username": p_user
    }
    nodes.append(node)

# Chiusura della connessione
cursor.close()
conn.close()

# Nome del file output
output_file = "/var/lib/data/" + p_so_name + "_" + p_so_ver + "_" + p_subnet + ".json"

# Scrittura del file JSON
with open(output_file, 'w') as f:
    json.dump(nodes, f, indent=4)

print(f"File di configurazione dei nodi generato: {output_file}")
