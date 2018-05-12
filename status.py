from matrix_client.api import MatrixHttpApi
import os
import sys
import yaml

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
settings = None
try:
        with open((os.path.join(__location__, 'settings.yaml')), 'r') as stream:
                settings = yaml.load(stream)
except IOError as e:
        sys.exit("no settings.yaml found!")

# CONSTANTS
DOMAIN = settings['DOMAIN']
ROOMS = settings['ROOMS']
TOKEN = settings['TOKEN']

matrix = MatrixHttpApi(DOMAIN, token=TOKEN)
service = sys.argv[1]
message = "Service '{}' just failed".format(service)
print(message)
for room in ROOMS:
        matrix.join_room(room)
        response = matrix.send_message(room, message)
