from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

news = [
    "Gold prices increase due to inflation",
    "Crypto market crashes",
    "Stable bonds gaining attention",
    "Tech stocks rally in the market",
]

labels = ["conservative", "aggressive", "conservative", "aggressive"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(news)

model = LogisticRegression()
model.fit(X, labels)

def predict_news(news_text):
    vec = vectorizer.transform([news_text])
    return model.predict(vec)[0]