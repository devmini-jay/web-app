from flask import Flask

app = Flask(__name__) #creates the flass application


@app.route("/") #runs function when root url is visited
def home(): 
    return """
    <h1>Practical Assessment</h1>
    <h2>Devmini Jayasiri</h2>
    <p>Web app in the container is running!! Yippiee!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) #starts app on port 5000.