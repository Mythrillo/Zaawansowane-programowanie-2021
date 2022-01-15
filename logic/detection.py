import json
from io import BytesIO
from PIL import Image

from flask import send_file
from flask import Response

import werkzeug
import cv2
import numpy as np


def detect_people(image: werkzeug.datastructures.FileStorage) -> Response:
    with open("models/classes.json") as f:
        classes = json.load(f)
    image_str = image.read()
    image = cv2.imdecode(np.fromstring(image_str, np.uint8), cv2.IMREAD_COLOR)
    cvNet = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb', 'models/graph.pbtxt')
    rows = image.shape[0]
    cols = image.shape[1]
    cvNet.setInput(cv2.dnn.blobFromImage(image, size=(500, 500), swapRB=True, crop=False))
    count = 0
    cvOut = cvNet.forward()
    for i in np.arange(0, cvOut.shape[2]):
        confidence = cvOut[0, 0, i, 2]
        if confidence > 0.5:
            class_name = classes[str(int(cvOut[0, 0, i, 1]))]
            if class_name != "person":
                continue
            count += 1
            left = cvOut[0, 0, i][3] * cols
            top = cvOut[0, 0, i][4] * rows
            right = cvOut[0, 0, i][5] * cols
            bottom = cvOut[0, 0, i][6] * rows
            cv2.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 0), thickness=2)
            cv2.putText(image, f"confidence: {confidence:.2f}", (int(left), int(top) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(image, f"Detected: {count} people.", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    return serve_pil_image(image)


def serve_pil_image(image: Image.Image) -> Response:
    image_io = BytesIO()
    image.save(image_io, "JPEG", quality=70)
    image_io.seek(0)
    return send_file(image_io, mimetype="image/jpeg")
