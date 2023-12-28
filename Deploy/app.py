from flask import Flask, request, jsonify
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load your trained model
model = load_model("Brest_CNN.h5")

@app.route('/predict', methods=['POST'])
def predict():
    try:

        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
            return jsonify({'error': 'Invalid file format'})
        
        img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (50, 50))  
        img = np.expand_dims(img, axis=0)  

        prediction = model.predict(img)
        predicted_class = np.argmax(prediction)

        class_labels = ['IDC (-)', 'IDC (+)']
        result = class_labels[predicted_class]

        return jsonify({'prediction': str(predicted_class)})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
