#!/bin/bash
INTERPRETE="python "
PERCORSO=/PERCORSO/
INSERT=mariadb_to_zabbix_insert.py
UPDATE=mariadb_to_zabbix_update.py
DELETE=mariadb_to_zabbix_delete.py
CHECK=integrity_check.py
cd $PERCORSO
$INTERPRETE$CHECK 3
$INTERPRETE$DELETE
$INTERPRETE$CHECK 1
$INTERPRETE$INSERT
$INTERPRETE$CHECK 2
$INTERPRETE$UPDATE

