from matrix_client.client import MatrixClient
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


client = MatrixClient(settings['DOMAIN'])

username = raw_input("enter username:\n")
password = raw_input("enter password:\n")

# Existing user
token = client.login_with_password(username=username, password=password)
print("\n")
print(token)
