import psycopg2
import flask,requests,json 
import jinja2
from authlib.flask.client import OAuth
from flask import request,redirect,url_for,jsonify,render_template

app = flask.Flask(__name__)

server = "postgres://mmojyviutqpftt:9708f3980b74c50a5d4d3ae9713254561626628fde9b23e19e92bfda0ba63b23@ec2-34-233-0-64.compute-1.amazonaws.com:5432/d6pleq228gs43m"
connection = psycopg2.connect(server,sslmode = "require")
cursor = connection.cursor()

@app.route("/", methods=["POST","GET"])
def test():

    if request.method == "GET":
        query = "SELECT students.alias,subscriptions.location, subscriptions.profession, subscriptions.subscriptiontype, subscriptions.enddate, students.url, students.id FROM public.students INNER JOIN public.subscriptions ON students.id=subscriptions.id"
        cursor.execute(query)
        results = cursor.fetchall()
        return flask.render_template("/test.html",info = results)

        
@app.route("/ajaxfile", methods=["POST","GET"])
def ajaxfile():
    
    if request.method == "POST":
        user_id = request.form['user_id']
        query = "SELECT students.alias,subscriptions.location, subscriptions.profession, subscriptions.subscriptiontype, subscriptions.enddate, students.url FROM public.students INNER JOIN public.subscriptions ON students.id=%s AND subscriptions.id=%s"
        tuple1 = (user_id,user_id)
        cursor.execute(query,tuple1)
        results = cursor.fetchall()
    return jsonify({'htmlresponse': render_template('response.html',results=results,user_id=user_id)})

@app.route("/ajaxfile1", methods=["POST","GET"])
def ajaxfile1():
    if request.method == "POST":
        user_id = request.form['user_id']
        name = request.form["name"]
        location = request.form["location"]
        profession = request.form["profession"]
        account_type = request.form["account_type"]
        subscription_enddate = request.form["subscription_enddate"]
        url = request.form["url"]        
        query1 = "UPDATE students SET alias=%s , url=%s WHERE id=%s"
        tuple1 = (name,url,user_id)
        cursor.execute(query1,tuple1)
        query2 = "UPDATE subscriptions SET location=%s, profession=%s, subscriptiontype=%s, enddate=%s WHERE id=%s"
        tuple2 = (location,profession,account_type,subscription_enddate,user_id)
        cursor.execute(query2,tuple2)
        connection.commit()
    return "success"
