from flask import Flask , render_template , request
app = Flask(__name__)

@app.route('/new_bike' ,methods=["GET","POST"])
def new_bike():
    if request.method=="GET":
        return render_template("ex1.html")
    elif request.method=="POST":
        form=request.form
        m=form["model"]
        df=form["daily_fee"]
        i=form["image"]
        y=form["year"]
        print(m,df,i,y)
        return " :) "

if __name__ == '__main__':
  app.run(debug=True)