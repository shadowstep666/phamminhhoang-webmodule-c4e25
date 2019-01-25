from flask import Flask,render_template
app = Flask(__name__)

@app.route("/user/<user_name>")
def user(user_name):
    name_list={
        "hoang":{
            "name":"pham minh hoang",
            "gender":"male",
            "age" : "21",
            "hobbies":"play guitar , listen music , reading",
        },
        "dat":{
            "name":"tran quoc dat",
            "gender":"male",
            "age" : "19",
            "hobbies":"play game",
        },
        "linh":{
            "name":"nguyen phuong linh",
            "gender":"female",
            "age" : "25",
            "hobbies":"shopping",
       }
    }
    if user_name in name_list:
        return render_template("ex2.html",user_name=name_list[user_name])
    else :
        return " user not found "
  

if __name__ == "__main__":
  app.run(debug=True)