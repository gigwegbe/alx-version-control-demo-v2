import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Job API(s)</h1><p>This site is a prototype Job APIs.</p>"


app.run()
