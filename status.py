from matrix_client.api import MatrixHttpApi
import os
import sys
import yaml

settings = None
try:
    with open('settings.yaml', 'r') as stream:
        settings = yaml.load(stream)
except IOError as e:
    sys.exit("no settings.yaml found!")

# CONSTANTS
DOMAIN = settings['DOMAIN']
SERVICES = settings['SERVICES']
ROOMS = settings['ROOMS']
TOKEN = settings['TOKEN']


def online( service ):
    stat = os.system('systemctl is-active --quiet {}'.format(service))
    if not stat:
        return True
    return False


matrix = MatrixHttpApi(DOMAIN, token=TOKEN)
status = False
for service in SERVICES:
    if not online(service):
        status = True
        message = "Service: '{}' is offline".format(service)
        print(message)
        for room in ROOMS:
                matrix.join_room(room)
                response = matrix.send_message(room, message)
if not status:
    print("everything is fine")
