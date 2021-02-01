from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return '''My name is Chineme Ezegbunam. This is my CA2 work.
 My GitHub URL is https://github.com/chinemeezegbunam/myISM209CA2.git'''

if __name__ == "__main__":
 app.run(port=5005)