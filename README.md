# matrix-status-bot

matrix bot that notifies you of stopped system services.

## setup
```
$ virtualenv <directory>
$ cd <directory>
$ source bin/activate
$ pip install requirements.txt -r
$ cp settings.yaml.example settings.yaml
```

Edit settings.yaml to your liking.
You can get the access token by executing:
```
$ python get_token.py
```

Add a cronjob to execute the script periodically, e.g. for every 5 minutes:
```
*/5 * * * * <directory>/bin/python <directory>/status.py
```
