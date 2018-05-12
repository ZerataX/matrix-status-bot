# matrix-status-bot

matrix bot that notifies you when a system services fails.

## setup
```
$ virtualenv ENV
$ source bin/activate
$ pip install requirements.txt -r
$ cp settings.yaml.example settings.yaml
```

Edit settings.yaml to your liking

Append to your service you wanted to be notified about:
```
OnFailure=/home/user/matrix-status-bot/bin/python /home/matrix-status-bot/status.py "Service Name"
```
