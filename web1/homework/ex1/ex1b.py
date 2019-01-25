from flask import Flask,render_template
app = Flask(__name__)

@app.route("/BMI/<int:weight>/<int:height>")
def BMI(weight,height):
    bmi=weight/((height/100)*(height/100)) 
    return render_template("ex1.html",bmi=bmi)
  

if __name__ == '__main__':
  app.run(debug=True)