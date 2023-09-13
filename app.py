from flask import Flask, request,url_for,render_template ,redirect , send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/math1')
def math1():
    return render_template('math1.html')

@app.route('/math2')
def math2():
    return render_template('math2.html')

@app.route('/hide1')
def hide1():
    return render_template('hide1.html')

@app.route('/form')
def formPage():
    return render_template('form.html')

@app.route('/count')
def count():
    return render_template('count.html')

@app.route('/img', methods=['GET'])
def img():
    if 'filename' in request.args:
        return send_file('images/' + request.args['filename'])
    return render_template('img.html')

@app.route('/flag1', methods=['POST'])
def flag1():
    data = request.get_json()
    money = data.get('money', '')
    
    if(money >1000):
        return "flag= nihaohaha"
    else:
        return "餘額不足"

@app.route('/account/<name>', methods=['GET'])
def account(name):
    return 'Welcome {} ~ !!!'.format(name)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    user = request.form['user']
    if user == "sun":
        print("post : user => ", user)
        return "Hello sun"
    else:
        return "login failed :("
    
@app.route('/get',methods=['GET'])
def get():
    return render_template('get_login.html')

@app.route('/get/login',methods=['GET'])
def get_login():
    user = request.values.get('username')
    password = request.values.get('pass')
    
    if user=="guest" and password == "guest":
        return render_template("get_guest.html")
    elif user=="admin" and password == "admin":
        return render_template("get_admin.html")
    
    return "ERROR"

@app.route('/who',methods=['GET'])
def who():
    return render_template('who.html')
    
@app.route('/who/flag',methods=['GET'])
def who_flag():
    data = request.user_agent.string
    if data == 'ntcuhacker':
        return render_template('who_correct.html') 
    else: 
        return render_template('who_wrong.html')
    
@app.route('/post',methods=['GET'])
def post():
    return render_template('post_login.html')

@app.route('/post/login',methods=['GET','POST'])
def post_login():
    user = request.values.get('username')
    password = request.values.get('pass')
    
    if user=="guest" and password == "guest":
        return render_template("post_guest.html")
    elif user=="admin" and password == "admin":
        return render_template("post_admin.html")
    
    return "ERROR"

if __name__ == '__main__':
    app.run()