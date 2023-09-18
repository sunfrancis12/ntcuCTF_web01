# This is a [Flask](https://flask.palletsprojects.com/en/2.3.x/) based framework
Author: [台中教育大學 白帽社](https://hackmd.io/@ntcuhack/index) -sunfrancis12
## How to download:
git clone it from github
```bash
git clone https://github.com/sunfrancis12/ntcuCTF_web01.git
cd ntcuCTF_web01
```
## Setting up enviorments
install `Flask` to run the code
```bash
pip install flask
```
## Runing the service
starting the flask 
```bash
flask run
```
### run it with `python` 
with `python` 
```bash
python app.py
```
with `python3` 
```bash
python3 app.py
```
## Alternative way to run
### running it with [gunicorn](https://gunicorn.org/):

install gunicorn
```bash
pip install gunicorn
```
excute it
```bash
sudo gunicorn -w 2 -b 0.0.0.0:8000 app:app --daemon
```
`-b` the port it use

`-w` the cpu thread it use

`--daemon` excute in the background
### running it with gunicorn & [gevent](https://www.gevent.org/) :
install gevent
```bash
pip install gevent
```
```bash
sudo gunicorn -w 2 -b 0.0.0.0:8000 app:app --worker-class="gevent" --daemon
```
`--worker-class="gevent"` using gevent
## gunicorn debug
serach for all gunicorn running in the background
```
ps -ef | grep gunicorn
```
you can stop them with
```
sudo -9 kill {PID}
```
OR
clear all gunicorn event
```
sudo pkill gunicorn
```
