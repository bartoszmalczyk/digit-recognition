from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf 

img = Image.open('your_digit.png').convert('L') 
img = img.resize((28,28))

img_array = np.array(img)
img_array = img_array.astype('float32') / 255.0
img_array = img_array.reshape(1, 784)

model = tf.keras.models.load_model('digit_recognition.keras')

prediction = model.predict(img_array)
output = np.argmax(prediction)

print(f"Detected number: {output}")