"""
Test module
"""
from flask import Flask, render_template
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
TEMPLATE_DIR = "./"
ENV = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = ENV.get_template("index.html")
@app.route("/")
def test():
   """
   Test
   """
   return render_template(template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=True)
