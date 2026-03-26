# Digit Recognition (MNIST)

Simple handwritten digit classifier trained on the MNIST dataset using TensorFlow/Keras. The repository includes a training notebook and a small script to run inference on an image.

## Contents
- `main.ipynb` — trains a small neural network on MNIST and saves the model
- `digit_recognition.keras` — saved Keras model
- `predict.py` — loads the saved model and predicts a digit from `your_digit.png`
- `your_digit.png` — example input image

## Requirements
- Python 3
- TensorFlow
- NumPy
- Pillow

Install dependencies (example):
```bash
pip install tensorflow numpy pillow
```

## Train the model
Open and run the notebook (optionally — there is a trained model already):
- `main.ipynb`

It trains on MNIST and saves the model to `digit_recognition.keras`.

## Run a prediction
1. Put your 28x28 (or any size) digit image in the repo root as `your_digit.png` (black background, white digit).
2. Run:
```bash
python predict.py
```

The script prints:
- `Detected number: <digit>`
