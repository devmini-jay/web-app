from flask import Flask

app = Flask(__name__)  # creates the flask application


@app.route("/")  # runs function when root url is visited
def home():
    return """
    <html>
    <head>
        <title>Practical Assessment</title>
        <style>
            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                background: linear-gradient(135deg, #ffd6e8, #ffb3d1);
                font-family: "Segoe UI", Verdana, sans-serif;
                color: #6b2c47;
            }
            .card {
                background: #fff5f9;
                padding: 40px 60px;
                border-radius: 20px;
                box-shadow: 0 8px 24px rgba(214, 51, 132, 0.25);
                text-align: center;
                border: 2px solid #ffc2dd;
            }
            h1 {
                margin: 0 0 8px;
                color: #d63384;
            }
            h2 {
                margin: 0 0 20px;
                font-weight: 400;
                color: #a64d79;
            }
            p {
                background: #ffe3f0;
                padding: 12px 20px;
                border-radius: 12px;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Practical Assessment</h1>
            <h2>Devmini Jayasiri</h2>
            <p>Web app in the container is running!! Yippiee! 🎀</p>
            <p>Updated automatically through the CI/CD pipeline! Yayyy!</p>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # starts app on port 5000.