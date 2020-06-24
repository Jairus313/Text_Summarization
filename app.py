from flask import Flask, render_template, url_for, request, redirect
from summariser import Summariser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def result():
    if request.method == "POST":
        text = request.form["text"]
        if text == "":
            return render_template("home.html")

        else:
            paragraph = Summariser.clean_text(text)
            freq_table = Summariser.create_frequency_table(paragraph)
            sentence = Summariser.sentence_tokenize(paragraph)
            sentence_scores = Summariser.score_sentences(sentence, freq_table)
            threshold = Summariser.find_average_score(sentence_scores)
            summary = Summariser.generate_summary(sentence, sentence_scores, 0.75 * threshold)
            
            return render_template("result.html",text=summary)

if __name__ == "__main__":
    app.run(debug=True)