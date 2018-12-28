# Arlo: code for downloading videos from arlo cloud.

## Setup:

### Note: you must create a arlo.ini file under resources with the following:
```
[ARLO]
arlo.username=
arlo.password=
arlo.videospath=videos/
```

```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python arlo.py
```
