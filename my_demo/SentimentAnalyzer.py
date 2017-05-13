import pickle
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer

stemmer = SnowballStemmer("russian")
analyzer = CountVectorizer().build_analyzer()


def stemmed_words(doc):
    return (stemmer.stem(w) for w in analyzer(doc))


class SentimentAnalyzer:
    def __init__(self):
        self.model = SentimentAnalyzer._load_model("models/cnt_log.pkl")

    @staticmethod
    def _load_model(model_name):
        with open(model_name, "rb") as f:
            model = pickle.load(f)
        return model

    def predict(self, text):
        label = int(self.model.predict([text])[0])
        return {
            "label": label,
            "prob": float(self.model.predict_proba([text])[0][label])
        }