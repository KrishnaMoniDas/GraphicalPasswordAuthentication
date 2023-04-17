from flask import Flask, render_template

app = Flask(__name__)

MEMBERS = [
  {
    'id':1,
    'name':'Krishna Moni Das'
  },
  {
    'id':2,
    'name':'Milonjyoti Borah'
  },
  {
    'id':3,
    'name':'Abir Banerjee'
  },
  {
    'id':4,
    'name':'Amarjeet Boruah'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html',Website_dev='Krishna Moni Das',members=MEMBERS)

@app.route("/login")
def login_page():
  return render_template('login.html')


@app.route("/signup")
def signup_page():
  return render_template('signup.html')
  


if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)