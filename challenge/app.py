from flask import Flask
import redis

# variable app, set= function Flask, the Python vrble, name, tells Flask everything it needs is in current dir.
app = Flask(__name__)

app = Flask(__name__)
redis_client = FlaskRedis(app)

#increment variable, count, using the redis atomic incr command
count = redis_client.incr('visits')

#the / on a website, eg. google.com/, is the base
@app.route("/")
def welcome():
    return "Welcome!"
# second route
@app.route("/count")
def visits():
    return (f"total visits: {count}")

app.run(host="0.0.0.0:6379")