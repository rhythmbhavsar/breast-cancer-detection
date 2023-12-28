# Breast Cancer Detection using Histopathology Images

![image](https://github.com/rhythmbhavsar/breast-cancer-detection/assets/98228696/25b5154e-06dc-4707-86bd-2c5696c5257c)


## Overview

This project focuses on training a Convolutional Neural Network (CNN) model to detect breast cancer using histopathology images. It includes the dataset used, model training, and deployment via Flask.

### Dataset

The dataset used for this project is sourced from [Kaggle - Breast Histopathology Images](https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images). It contains histopathology images labeled as IDC (Invasive Ductal Carcinoma) positive and negative cases.

**Download Dataset:**
- [Breast Histopathology Images Dataset](https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images/download?datasetVersionNumber=1)

### Model Training

The Python notebook `Breast_Cancer_Detection.ipynb` illustrates the steps for:
- Loading and exploring the dataset
- Preprocessing the images
- Building and training the CNN model
- Evaluating the model's performance

### Flask Deployment

The Flask web application enables users to interact with the trained model for breast cancer detection. The application takes an input image and provides predictions on whether the image contains IDC positive or negative cells.

### Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/rhythmbhavsar/breast-cancer-detection.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Access the web app via a browser at `http://localhost:5000`.

### Additional Information

#### Breast Cancer Awareness
![image](https://github.com/rhythmbhavsar/breast-cancer-detection/assets/98228696/b8e15c30-3034-4684-87f5-0543e7ae7b62)

Breast cancer is a serious health concern affecting many women worldwide. Early detection and diagnosis significantly improve survival rates. It's essential to raise awareness about breast cancer screening and the importance of regular check-ups.

