# without render_template
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/BMI/<int:weight>/<int:height>")
def BMI(weight,height):
  bmi=weight/((height/100)*(height/100))  
  if bmi < 16:
    return "Severely underweight"
  elif 16 <= bmi <= 18.5:
    return "Underweight"
  elif 18.5 <= bmi < 25:
    return " Normal"
  elif 25 <= bmi < 30:
    return "Overweight"
  elif bmi > 30:
    return "Obese"

if __name__ == '__main__':
  app.run(debug=True)
