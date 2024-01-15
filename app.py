from flask import Flask,request,render_template
import google.generativeai as palm

palm.configure(api_key="AIzaSyDa31qY_HjCWZd7Gf4tGObk9iaJ0vKjwTk")
model = {"model":"models/chat-bison-001"}

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def index():
    if request.method == "POST":
        q = request.form.get("q")
        print(q)
        r = palm.chat(
            **model,
            messages = q
            )
        return(render_template("index.html", result=r.last))
    else:
        return(render_template("index.html", result="Waiting for question......"))

if __name__ == "__main__":
    app.run()
