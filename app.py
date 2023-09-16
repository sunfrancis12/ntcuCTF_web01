from flask import Flask, request,url_for,render_template ,redirect , send_file,make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    
#生命的出路(Path)

@app.route('/money/honey/pocket/dollar/frustrated/happiness/dream')
def path():
    return render_template('way.html')

#數學小學堂

@app.route('/math')
def math1():
    return render_template('math1.html')

@app.route('/answer', methods=['POST'])
def answer():
    ans = request.values.get('answer')
    
    if ans == "correct":
        return render_template('math2.html')
    
    return "ERROR!!!"

#f12啟動

@app.route('/hide')
def hide1():
    return render_template('hide1.html')


#剎那想要抓住網頁

@app.route('/grab')
def grab():
    return render_template('grab.html')

# login flaw

@app.route('/count')
def count():
    return render_template('count.html')

@app.route('/flag1', methods=['POST'])
def flag1():
    data = request.get_json()
    money = data.get('money', '')
    
    if(money >1000):
        return "flag= nihaohaha"
    else:
        return "餘額不足"

#get me admin
    
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

#你是誰?

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
    
# Post me Admin
    
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

# cookie

@app.route('/cookie',methods=['GET','POST'])
def cookie():
    return render_template('cookie.html')

@app.route('/cookie/set',methods=['GET','POST'])
def setcookie():
    
    auth = request.cookies.get('isAdmin')
    if auth :
        if request.method =="POST":
            return redirect("/cookie/admin")
        else:
            return redirect("/cookie/guest")
    
    resp = make_response(redirect("/cookie/guest"))
    resp.set_cookie(key='isAdmin', value='false')
       
    return resp
    
@app.route('/cookie/admin',methods=['GET','POST'])
def cookie_admin():
    auth = request.cookies.get('isAdmin')
    
    if auth =="true":
        return render_template('cookie_admin.html') 
    else:
        return render_template('cookie_failed.html')
    
@app.route('/cookie/guest',methods=['GET','POST'])
def cookie_guest():
    auth = request.cookies.get('isAdmin')
    
    if auth == "false":
        return render_template('cookie_guest.html')
    elif auth =="true":
        return redirect("/cookie/admin") 
    else:
        return "ERROR!"

'''
@app.route('/img', methods=['GET'])
def img():
    if 'filename' in request.args:
        return send_file('images/' + request.args['filename'])
    return render_template('img.html')
'''

if __name__ == '__main__':
    app.run(host="0.0.0.0")