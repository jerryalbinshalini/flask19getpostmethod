# ....flask template
# from flask import *
# app=Flask(__name__)
# @app.route('/')
# def temmessage():
#     return "<html><body><h2>Welcome to all</h2></body></html>"
# if __name__=='__main__':
#     app.run(debug=True)
# ......rendering external html file
# from flask import *
# app=Flask(__name__)
# @app.route('/')
# def renmessage():
#     return render_template('render.html')
# if __name__ == '__main__':
#     app.run(debug=True)
# ....Delimeters.....
from flask import *
app=Flask(__name__)
@app.route('/del/<name>')
def renmessage(name):
    return render_template('render.html',username=name)
if __name__ == '__main__':
    app.run(debug=True)