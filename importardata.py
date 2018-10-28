#!/usr/bin/python
import mysql.connector
import csv
import argparse
import mysql.connector as mariadb
import uuid


# input parameter handling
DEFAULT_INSTANCE = '57'
INSTANCES = ['51', '55', '56', '57']
PORTS = ['5173', '5539', '5620', '5704','3306']
ENGINES = ['InnoDB', 'MyISAM']
DEFAULT_ENGINE = 'InnoDB'
HOST = '127.0.0.1'
USER = 'root'
port = '3306'
PASSWORD = ''
DATABASE = 'web_uniclick_br'
TABLE_DEFINITION = (
    # 'CREATE TABLE `nodes` ('
    # '    `id` bigint PRIMARY KEY,'
    # '    `lat` decimal(9,7),'
    # '    `lon` decimal(10,7),'
    # '    `version` int,'
    # '    `timestamp` timestamp,'
    # '    `changeset` bigint,'
    # '    `uid` bigint,'
    # '    `user` varchar(255)'
    # ')'

    # 'CREATE TABLE `nodes` ('
	# '`FUENTE` VARCHAR(250) NULL,'
	# '`CODIGO_BASE` VARCHAR(250) NULL, '
	# '`TIPO_DOCUMENTO` VARCHAR(250) NULL, '
	# '`NUMERO_DOCUMENTO` VARCHAR(250) NULL, '
	# '`PATERNO` VARCHAR(250) NULL, '
	# '`MATERNO` VARCHAR(250) NULL, '
	# '`NOMBRE1` VARCHAR(250) NULL, '
	# '`NOMBRE2` VARCHAR(250) NULL, '
	# '`TIPO` VARCHAR(250) NULL, '
	# '`MODALIDAD_ACTIVACION` VARCHAR(250) NULL, '
	# '`TIPO_TARJETA` VARCHAR(250) NULL, '
	# '`LINEA` VARCHAR(250) NULL, '
	# '`VIGENCIA` VARCHAR(250) NULL '
    # ')'
)
CSV_FILE = 'archivobase/Base_Web_Captacion_201804.csv'

parser = argparse.ArgumentParser(description='Creates and imports the nodes table.')
parser.add_argument('--engine', choices=ENGINES, default=DEFAULT_ENGINE,
                    help='Chosen engine (default: ' + DEFAULT_ENGINE + ')')
parser.add_argument('--instance', choices=INSTANCES, default=DEFAULT_INSTANCE,
                    help='Instance version (default: ' + DEFAULT_INSTANCE + ')')
options = parser.parse_args()
# port = PORTS[INSTANCES.index(options.instance)]

# database connection
# mariadb_connection = mariadb.connect(user='root', password='',host='127.0.0.1',database='web_uniclick_br')   output1tab.csv
# cursor = mariadb_connection.cursor()

db = mariadb.connect(user='root', password='',host='127.0.0.1',database='web_uniclick_br')
cursor = db.cursor()


direccion_csv_file="SELECT direccion from zdata WHERE idz=(SELECT MAX(idz)  FROM zdata)"
cursor.execute(direccion_csv_file)
direccion=cursor.fetchall()


#CSV_FILE = 'archivobase/output1tab.csv'
#CSV_FILE = 'D:/xampp/htdocs/bancoripleyweb/app/storage/app/archivoscsv/2018/04/24/10/output1tabv2.csv'
#CSV_FILE = 'D:\xampp\htdocs\bancoripleyweb\app/storage/app/archivoscsv/2018/04/24/11/output1tabv2.csv'
CSV_FILE = direccion[0][0]




# Obtener el nombre de tabla de base de datos
# create_table = TABLE_DEFINITION + ' ENGINE=' + options.engine
obtener_nombreTabla="SELECT nombreTabla from zdata WHERE idz=(SELECT MAX(idz)  FROM zdata)"
cursor.execute(obtener_nombreTabla)
nametable=cursor.fetchall()

# data import descomentar

load_data = "LOAD DATA INFILE '" + CSV_FILE + "' INTO TABLE "+nametable[0][0]
cursor.execute(load_data)

load_data = "DELETE FROM "+nametable[0][0]+" LIMIT 1"
cursor.execute(load_data)

# finishing
if (options.engine == 'MyISAM'):
    cursor.execute('FLUSH TABLES')
else:
    db.commit()

cursor.close()
db.close()
