How to download:
```bash
git clone https://github.com/sunfrancis12/ntcuCTF_web01.git
cd ntcuCTF_web01
```
remember to install `Flask` to run the code
```bash
pip install flask
```
starting the flask service
```bash
flask run
```
OR run it with `python` 
python 
```bash
python app.py
```
python3
```bash
python3 app.py
```

running it with [gunicorn](https://gunicorn.org/):
```bash
sudo gunicorn -w 2 -b 0.0.0.0:8000 app:app --daemon
```
`-b` the port it use

`-w` the cpu thread it use

`--daemon` excute in the background

running it with gunicorn & [gevent](https://www.gevent.org/) :
```bash
sudo gunicorn -w 2 -b 0.0.0.0:8000 app:app --worker-class="gevent" --daemon
```
`--worker-class="gevent"` using gevent
