# matrix-status-bot

matrix bot that notifies you when a system services fails.

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

Append the following line to your service you want to be notified about:
```
OnFailure=/home/user/matrix-status-bot/bin/python /home/matrix-status-bot/status.py "Service Name"
```
