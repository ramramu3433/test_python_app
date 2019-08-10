from flask import Flask
app = Flask(__name__)


@app.route("/")
def  test():
     return  "hello-world"

@app.route("/hello",methods=["GET"])
def  hello():
     return  "get method only"

if __name__ == "__main__":
  app.run(debug=True)
