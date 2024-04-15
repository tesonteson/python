from sklearn.datasets import load_iris, load_digits
from sklearn.svm import SVC
import numpy as np
from PIL import Image


class IrisPrediction():
    def __init__(self):
        self.data = load_iris()
        x, y = self.data.data, self.data.target
        self.model = SVC().fit(x, y)

    def predict_iris(self, sepal_length, sepal_width, petal_length, petal_width):
        predict_data = np.array([[sepal_length,sepal_width,petal_length,petal_width]])
        pred_result = self.model.predict(predict_data)
        if pred_result == 0:
            return "setosa"
        elif pred_result == 1:
            return "versicolor"
        else:
            return "virginica"


class ImagePrediction():
    def __init__(self):
        self.data = load_digits()
        x, y = self.data.data, self.data.target
        self.model = SVC().fit(x, y)

    def predict_image(self, image_file):
        image = Image.open(image_file.file)
        image = image.convert("L")
        image = image.resize((8, 8), Image.Resampling.LANCZOS)
        image = np.array(image)
        predict_data = (16 - (image * 16 / 255)).astype(int)
        predict_data = predict_data.reshape(1, -1)
        pred_result = self.model.predict(predict_data)[0]
        return pred_result
