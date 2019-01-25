from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "hello, t am again"

@app.route("/c4e25")
def c4e25():
    return "this is c4e25 , happy coding !!!"
  
@app.route("/hi/quan")
def hi_me():
    return "hello"

@app.route("/hi/<name>")
def hi(name):
    return "hi "+ name +", have a nice day !!!"

# @app.route("/add/<a>/<b>")
# def add(a,b):  
    # return   str(int(a) +int(b))

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return str(a+b)

@app.route("/simple-html")
def simple_html():
    return "<h3>hello</h3>"

@app.route("/html")
def html():
    return render_template("sample.html")#food.html hien dang la mot file tinh


food_list=[
    "bun dau",
    "bun cha ",
    "com",
    "pho",
]

@app.route("/menu")
def menu():
    return render_template("menu.html",food_list=food_list)


# @app.route("/food")
# def food():
#     return render_template("food.html",title=food_list[1])

@app.route("/food/<int:index>")#detail
def food(index):
    return render_template("food.html",title=food_list[index])

detail={
    'title':'bun cha '
    'image':''
}

@app.route("/food_detail")
def food_detail():
    return render_template("food_detail.html",detail=detail)
if __name__ == '__main__':
  app.run(debug=True)