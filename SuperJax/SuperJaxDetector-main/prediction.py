import cv2
import tensorflow as tf


CATEGORIES = ["SuperJax", "SerInferior"]

img = "bg373.png"

def prepare(filepath):
    IMG_SIZE = 100  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  # read in the image, convert to grayscale
    try:
    	new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize image to match model's expected sizing
    except Exception as e:
    	print(e)
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)  # return the image with shaping that TF wants.

model = tf.keras.models.load_model("64x3-CNN.model")

prediction = model.predict([prepare(img)])  # REMEMBER YOU'RE PASSING A LIST OF THINGS YOU WISH TO PREDICT


print("==============================================================")
print(f"A imagem {img} é:")
print(CATEGORIES[int(prediction[0][0])])