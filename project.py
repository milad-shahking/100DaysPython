import cv2
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np

# بارگیری مدل از پیش آموزش دیده
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# خواندن تصویر
image = cv2.imread("animal.jpg")
image = cv2.resize(image, (224, 224))  # تغییر اندازه برای مدل
image = np.expand_dims(image, axis=0)
image = preprocess_input(image)

# پیش‌بینی کلاس حیوان
predictions = model.predict(image)
label = decode_predictions(predictions, top=1)[0][0][1]

print(f"حیوان شناسایی‌شده: {label}")
