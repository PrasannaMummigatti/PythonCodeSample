from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

 @app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    return render_template('index.html', message=forward_message);
