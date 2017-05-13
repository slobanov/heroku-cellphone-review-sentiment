import json

from flask import Flask, render_template, request, abort

import SentimentAnalyzer

app = Flask("SentimentAnalyzerController")
analyzer = SentimentAnalyzer


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/api/predict", methods=["GET"])
def predict():
    if "text" not in request.args:
        app.logger.error("There is no 'text' arg")
        abort(400)

    text = request.args.get("text")

    predictions = analyzer.predict(text)
    return json.dumps(predictions)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9080)
