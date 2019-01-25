from flask import Flask,redirect
app=Flask(__name__)

@app.route("/about_me")
def about_me():
    return "name : phamMinhHoang <br> work : dai_hoc_Bach_khoa <br> age :21 <br>hobbies : listen_music , reading , play guitar"

@app.route("/school")
def school():
    return redirect("http://techkids.vn")

if __name__=="__main__":
    app.run(debug=True)