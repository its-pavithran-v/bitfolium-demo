import flask,requests,json 
import jinja2
from authlib.flask.client import OAuth

app = flask.Flask(__name__)

@app.route("/")
def home_view():
    return "<p>hello</p>"


@app.route("/abc")
def abc():
    return jsonify(
                message="good test",
                category="success",
                data=data,
                status=200
            )

@app.route("/test")
def test():
    data = "Pavithran"
    return flask.render_template("/test.html",info = data)
