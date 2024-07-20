from flask import *
app=Flask(__name__)
# # .....post method......
# @app.route('/login',methods=['POST'])
# def login():
#     uname=request.form['uname']
#     password=request.form['pass']
#     if uname=='arun' and password=='abcd':
#         return 'welcome'
# # ..........get method.......
@app.route('/login',methods=['GET'])
def login():
    uname=request.args.get('uname')
    password=request.args.get('pass')
    if uname=='arun' and password=='abcd':
        return 'welcome'

if __name__=='__main__':
    app.run(debug=True)