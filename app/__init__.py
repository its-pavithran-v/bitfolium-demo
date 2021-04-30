import psycopg2
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
    server = "postgres://mmojyviutqpftt:9708f3980b74c50a5d4d3ae9713254561626628fde9b23e19e92bfda0ba63b23@ec2-34-233-0-64.compute-1.amazonaws.com:5432/d6pleq228gs43m"
    connection = psycopg2.connect(server,sslmode = "require")
    cursor = connection.cursor()
    query = "SELECT id,url,lastlogin FROM students ORDER BY id ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    return flask.render_template("/test.html",info = results)
