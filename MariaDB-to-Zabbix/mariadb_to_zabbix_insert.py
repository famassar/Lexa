import configparser
import json
import requests
import mysql.connector
import logging
from datetime import datetime

class Host:
    def __init__(self, host_name, visible_name, description, disabled, interface_type, interface_ip_address, interface_dns, interface_use_ip, interface_port, interface_default, inserted, updated, deleted, type, type_full, name, alias, os, os_full, os_short, serialno_a, serialno_b, tag, asset_tag, macaddress_a, macaddress_b, hardware, hardware_full, software, software_full, software_app_a, software_app_b, software_app_c, software_app_d, software_app_e, contact, location, location_lat, location_lon, notes, chassis, model, hw_arch, vendor, contract_number, installer_name, deployment_status, url_a, url_b, url_c, host_networks, host_netmask, host_router, oob_ip, oob_netmask, oob_router, date_hw_purchase, date_hw_install, date_hw_expiry, date_hw_decomm, site_address_a, site_address_b, site_address_c, site_city, site_state, site_country, site_zip, site_rack, site_notes, poc_1_name, poc_1_email, poc_1_phone_a, poc_1_phone_b, poc_1_cell, poc_1_screen, poc_1_notes, poc_2_name, poc_2_email, poc_2_phone_a, poc_2_phone_b, poc_2_cell, poc_2_screen, poc_2_notes):
        self.host_name=host_name
        self.visible_name=visible_name
        self.description=description
        self.disabled=disabled
        self.interface_type=interface_type
        self.interface_ip_address=interface_ip_address
        self.interface_dns=interface_dns
        self.interface_use_ip=interface_use_ip
        self.interface_port=interface_port
        self.interface_default=interface_default
        self.inserted=inserted
        self.updated=updated
        self.deleted=deleted
        self.type=type
        self.type_full=type_full
        self.name=name
        self.alias=alias
        self.os=os
        self.os_full=os_full
        self.os_short=os_short
        self.serialno_a=serialno_a
        self.serialno_b=serialno_b
        self.tag=tag
        self.asset_tag=asset_tag
        self.macaddress_a=macaddress_a
        self.macaddress_b=macaddress_b
        self.hardware=hardware
        self.hardware_full=hardware_full
        self.software=software
        self.software_full=software_full
        self.software_app_a=software_app_a
        self.software_app_b=software_app_b
        self.software_app_c=software_app_c
        self.software_app_d=software_app_d
        self.software_app_e=software_app_e
        self.contact=contact
        self.location=location
        self.location_lat=location_lat
        self.location_lon=location_lon
        self.notes=notes
        self.chassis=chassis
        self.model=model
        self.hw_arch=hw_arch
        self.vendor=vendor
        self.contract_number=contract_number
        self.installer_name=installer_name
        self.deployment_status=deployment_status
        self.url_a=url_a
        self.url_b=url_b
        self.url_c=url_c
        self.host_networks=host_networks
        self.host_netmask=host_netmask
        self.host_router=host_router
        self.oob_ip=oob_ip
        self.oob_netmask=oob_netmask
        self.oob_router=oob_router
        self.date_hw_purchase=date_hw_purchase
        self.date_hw_install=date_hw_install
        self.date_hw_expiry=date_hw_expiry
        self.date_hw_decomm=date_hw_decomm
        self.site_address_a=site_address_a
        self.site_address_b=site_address_b
        self.site_address_c=site_address_c
        self.site_city=site_city
        self.site_state=site_state
        self.site_country=site_country
        self.site_zip=site_zip
        self.site_rack=site_rack
        self.site_notes=site_notes
        self.poc_1_name=poc_1_name
        self.poc_1_email=poc_1_email
        self.poc_1_phone_a=poc_1_phone_a
        self.poc_1_phone_b=poc_1_phone_b
        self.poc_1_cell=poc_1_cell
        self.poc_1_screen=poc_1_screen
        self.poc_1_notes=poc_1_notes
        self.poc_2_name=poc_2_name
        self.poc_2_email=poc_2_email
        self.poc_2_phone_a=poc_2_phone_a
        self.poc_2_phone_b=poc_2_phone_b
        self.poc_2_cell=poc_2_cell
        self.poc_2_screen=poc_2_screen
        self.poc_2_notes=poc_2_notes

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Database'], config['Zabbix'], config['Lexa']

def configure_logger(lexa_config):
    script_log=lexa_config['INSERT_LOG']
    logging.basicConfig(filename=script_log, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def log_message(message):
    logging.info(message)    

def update_host_info_in_database(db_config, zabbix_config, host):
    
        # Ottieni hostid da Zabbix
        hostid = get_zabbix_hostid(zabbix_config, host)
        interfaceid = get_zabbix_interfaceid(zabbix_config, hostid)
            # Aggiorna campi nel database con le informazioni di Zabbix
        update_query = "UPDATE alldata SET hostid = '" + hostid + "',interface_id = '" + interfaceid + "' WHERE host_name = '" + host + "'"
            
        connection = mysql.connector.connect(
            host=db_config['DB_HOST'],
            user=db_config['DB_USER'],
            password=db_config['DB_PASSWORD'],
            database=db_config['DB_NAME'],
            port=db_config['DB_PORT']
        )

        cursor = connection.cursor()
        cursor.execute(update_query)
        connection.commit()
        cursor.close()

        update_query = "UPDATE lexa.alldata SET inserted=1 WHERE host_name = '"+ host + "'"
        cursor = connection.cursor()
        cursor.execute(update_query, (host))
        connection.commit()
        cursor.close()

        connection.close()
    
        log_message(f"Host {host}: Zabbix hostid updated in the database.")

def get_zabbix_hostid(zabbix_config, host_name):

    bearer = f"{zabbix_config['ZABBIX_TOKEN']}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + bearer
        }

    api_url = f"{zabbix_config['ZABBIX_URL']}/api_jsonrpc.php"

    # Creazione della richiesta JSON per ottenere hostid da Zabbix
    payload = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "filter": {"host": [host_name]},
            "output": ["hostid"]
        },
        "id": 1
    }
    # Invio della richiesta HTTP
    response = requests.post(api_url, headers=headers, json=payload)
    
    # Gestione della risposta
    if response.status_code == 200:
        result = response.json().get('result')
        
        if result:
            return result[0]['hostid']
        else:
            log_message(f"Host {host_name}: Zabbix hostid not found.")
    else:
        log_message(f"Failed to get hostid for {host_name}: {response.text}")

    return None

def get_zabbix_interfaceid(zabbix_config, hostid):

    bearer = f"{zabbix_config['ZABBIX_TOKEN']}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + bearer
        }

    api_url = f"{zabbix_config['ZABBIX_URL']}/api_jsonrpc.php"

    # Creazione della richiesta JSON per ottenere hostid da Zabbix
    payload = {
           "jsonrpc": "2.0",
           "method": "hostinterface.get",
           "params": {
               "output": "interfaceid",
               "hostids": [hostid]
           },
           "id": 1
       }
    # Invio della richiesta HTTP
    response = requests.post(api_url, headers=headers, json=payload)
    
    # Gestione della risposta
    if response.status_code == 200:
        result = response.json().get('result')
        
        if result:
            return result[0]['interfaceid']
        else:
            log_message(f"Host {interfaceid}: Zabbix hostid not found.")
    else:
        log_message(f"Failed to get hostid for {interfaceid}: {response.text}")

    return None

def get_hosts_from_database(db_config):
    connection = mysql.connector.connect(
        host=db_config['DB_HOST'],
        user=db_config['DB_USER'],
        password=db_config['DB_PASSWORD'],
        database=db_config['DB_NAME'],
        port=db_config['DB_PORT']
    )
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT host_name, visible_name, description, disabled, interface_type, interface_ip_address, interface_dns, interface_use_ip, interface_port, interface_default, inserted, updated, deleted, `type`, type_full, name, alias, os, os_full, os_short, serialno_a, serialno_b, tag, asset_tag, macaddress_a, macaddress_b, hardware, hardware_full, software, software_full, software_app_a, software_app_b, software_app_c, software_app_d, software_app_e, contact, location, location_lat, location_lon, notes, chassis, model, hw_arch, vendor, contract_number, installer_name, deployment_status, url_a, url_b, url_c, host_networks, host_netmask, host_router, oob_ip, oob_netmask, oob_router, date_hw_purchase, date_hw_install, date_hw_expiry, date_hw_decomm, site_address_a, site_address_b, site_address_c, site_city, site_state, site_country, site_zip, site_rack, site_notes, poc_1_name, poc_1_email, poc_1_phone_a, poc_1_phone_b, poc_1_cell, poc_1_screen, poc_1_notes, poc_2_name, poc_2_email, poc_2_phone_a, poc_2_phone_b, poc_2_cell, poc_2_screen, poc_2_notes FROM lexa.alldata WHERE inserted=0;")
    hosts = [Host(**row) for row in cursor.fetchall()]
    cursor.close()
    connection.close()

    return hosts

def create_hosts_in_zabbix(zabbix_config, hosts, db_config):

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
                    "method": "host.create",
                    "params": {
                    "host": host.host_name,
				    "name": host.visible_name,
				    "description": host.description,
				    "status": host.disabled,
                    "interfaces": [
                                {
                                    "type": host.interface_type,
                                    "main": 1,
                                    "useip": host.interface_use_ip,
                                    "ip": host.interface_ip_address,
                                    "dns": host.interface_dns,
                                    "port": host.interface_port,
									"details": {
                                        "version": "2",
                                        "bulk": "1",
                                        "community": "{$SNMP_COMMUNITY}"
                                    }
                                }
                    ],
                    "groups": [
                        {
                            "groupid": defgroup
                        }
                    ],
         			"tags": [
         				{
         					"tag": "Lexa",
         					"value": ""
         				}
                    ],
				    "inventory_mode": 0,
				    "inventory": {
						"type": host.type,
						"type_full": host.type_full,
						"name": host.name,
						"alias": host.alias,
						"os": host.os,
						"os_full": host.os_full,
						"os_short": host.os_short,
						"serialno_a": host.serialno_a,
						"serialno_b": host.serialno_b,
						"tag": host.tag,
						"asset_tag": host.asset_tag,
						"macaddress_a": host.macaddress_a,
						"macaddress_b": host.macaddress_b,
						"hardware": host.hardware,
						"hardware_full": host.hardware_full,
						"software": host.software,
						"software_full": host.software_full,
						"software_app_a": host.software_app_a,
						"software_app_b": host.software_app_b,
						"software_app_c": host.software_app_c,
						"software_app_d": host.software_app_d,
						"software_app_e": host.software_app_e,
						"contact": host.contact,
						"location": host.location,
						"location_lat": host.location_lat,
						"location_lon": host.location_lon,
						"notes": host.notes,
						"chassis": host.chassis,
						"model": host.model,
						"hw_arch": host.hw_arch,
						"vendor": host.vendor,
						"contract_number": host.contract_number,
						"installer_name": host.installer_name,
						"deployment_status": host.deployment_status,
						"url_a": host.url_a,
						"url_b": host.url_b,
						"url_c": host.url_c,
						"host_networks": host.host_networks,
						"host_netmask": host.host_netmask,
						"host_router": host.host_router,
						"oob_ip": host.oob_ip,
						"oob_netmask": host.oob_netmask,
						"oob_router": host.oob_router,
						"date_hw_purchase": host.date_hw_purchase,
						"date_hw_install": host.date_hw_install,
						"date_hw_expiry": host.date_hw_expiry,
						"date_hw_decomm": host.date_hw_decomm,
						"site_address_a": host.site_address_a,
						"site_address_b": host.site_address_b,
						"site_address_c": host.site_address_c,
						"site_city": host.site_city,
						"site_state": host.site_state,
						"site_country": host.site_country,
						"site_zip": host.site_zip,
						"site_rack": host.site_rack,
						"site_notes": host.site_notes,
						"poc_1_name": host.poc_1_name,
						"poc_1_email": host.poc_1_email,
						"poc_1_phone_a": host.poc_1_phone_a,
						"poc_1_phone_b": host.poc_1_phone_b,
						"poc_1_cell": host.poc_1_cell,
						"poc_1_screen": host.poc_1_screen,
						"poc_1_notes": host.poc_1_notes,
						"poc_2_name": host.poc_2_name,
						"poc_2_email": host.poc_2_email,
						"poc_2_phone_a": host.poc_2_phone_a,
						"poc_2_phone_b": host.poc_2_phone_b,
						"poc_2_cell": host.poc_2_cell,
						"poc_2_screen": host.poc_2_screen,
						"poc_2_notes": host.poc_2_notes
				}
    },
	  "id": 1
}
        # Invio della richiesta HTTP
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
                
        # Gestione della risposta
        log_message(f"Host {host.host_name} creation response: {response.text}")

        if response.status_code == 200:
            log_message(f"Host {host.host_name} created successfully")
            # Aggiorna le informazioni di Zabbix nel database
            update_host_info_in_database(db_config, zabbix_config, host.host_name)
        else:
            log_message(f"Failed to create host {host.host_name}: {response.text}")

def main():
    db_config, zabbix_config, lexa_config = load_config()
    configure_logger(lexa_config)

    hosts = get_hosts_from_database(db_config)
    create_hosts_in_zabbix(zabbix_config, hosts, db_config)

if __name__ == "__main__":
    main()
