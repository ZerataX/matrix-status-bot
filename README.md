# matrix-status-bot

matrix bot that notifies you of stopped system services.

## setup
```
$ virtualenv ENV
$ source bin/activate
$ pip install requirements.txt -r
$ cp settings.yaml.example settings.yaml
```

Edit settings.yaml

```
$ python status.py
```

Add a crontab to execute periodically, e.g. for every 5 minutse:
```
*/5 * * * * /home/user/matrix-status-bot/bin/python /home/user/matrix-status-bot/status.py
```
