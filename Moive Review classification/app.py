import numpy as np
from flask import Flask , request , render_template
from keras import models
from keras.preprocessing.text import Tokenizer

print("Hello")

app = Flask(__name__)

m = models.load_model("models/model2.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods = ["POST"])
def predict():
    text = request.form['review']
    print("The value we got is ",text)

    max = 10000
    tok = Tokenizer(num_words=max)
    tok.fit_on_texts([text])
    s = tok.texts_to_sequences([text])
    x = vectorization_sequences(s, dimension=max)
    p = m.predict(x)
    u = np.round(p)
    o = ""
    if (u == 0):
        print(u)
        o = "The Review is Negative"
    else:
        print(u)
        o ="The Review is Positive"
    return  render_template("index.html",prediction_text = "{}".format(o))


# it the part of converting the data into desired form

def vectorization_sequences(sequence, dimension=10000):
  results  = np.zeros((len(sequence),dimension))
  for i , sequence in enumerate(sequence):
    results[i,sequence] = 1.
  return results

if __name__ == "__main__":
    app.run()