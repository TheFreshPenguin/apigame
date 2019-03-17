import flask
from flask import request, jsonify

from apibot import Apibot
#from munch import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

a = Apibot(5,5)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>API Game</h1>
<p>This API should be called using get and post requests.
Please read the rules markdown file first.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/move', methods=['POST'])
def api_all():
    #req = munchify(request.get_json(force=True))
    req = request.get_json(force=True)
    if req.get("where"):
        where = req.get("where")
        if where.get("direction"):
            direction = where.get("direction")
            if direction == "up":
                a.x += 1
    return(str(a.x))

app.run()
