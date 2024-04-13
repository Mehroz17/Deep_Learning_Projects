from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import  cv2
from PIL import Image
from keras import models

m = models.load_model("model/happy_sad_image.pkl")


app = Flask(__name__)

@app.route('/')
def home():
    return  render_template("indexhappy.html")


@app.route("/predict",methods = ["POST"])
def predict():
    option = request.form.get("options")

    img_file = request.files["image-input"]
    answer = image_preprocessing(img_file)
    if(answer < 0.5):
        option = "option1"
    else:
        option = "option2"
    return  render_template("indexhappy.html",selected_option = option)


def image_preprocessing(img_link):
    img_path = img_link
    img = Image.open(img_path)
    resize = tf.image.resize(img,(256,256))
    answer = m.predict(np.expand_dims(resize/255,0))
    return answer


if __name__ == "__main__":
    app.run()