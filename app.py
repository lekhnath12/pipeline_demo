from flask import Flask, render_template
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
template_dir = "./"
ENV = Environment(loader=FileSystemLoader(template_dir))
template = ENV.get_template("index.html")
@app.route("/")
def mothersday():
    return render_template(template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=True)
