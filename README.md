#### Project Overview

This project demonstrates a simple TensorFlow-based solution for solving the XOR problem using a Multi-layer Perceptron (MLP). The network comprises a single hidden layer with 2 neurons and an output layer with a single neuron. Both layers use the sigmoid activation function. The model is trained using the Adam optimizer and the Binary Cross-Entropy loss function. Training metrics, time, and final predictions are displayed.

---

#### Dependencies

- Python 3.x
- TensorFlow 2.x

#### Installation

1. Install Python: [Download Python](https://www.python.org/downloads/)
2. Install TensorFlow:
    ```bash
    pip install tensorflow
    ```

---

#### How to Run

1. Clone the repository or download the code.
2. Run the Python script `MLP.py`.

---

#### Code Description

1. **Data Preparation**
    - XOR input-output pairs are defined.
  
2. **Model Architecture**
    - A single hidden layer with 2 neurons and an output layer with 1 neuron are added to the model.
    
3. **Model Compilation**
    - The model is compiled using Binary Cross-Entropy as the loss function and Adam as the optimizer.
  
4. **Training**
    - Model is trained for 1500 epochs, and the training time is measured.

5. **Evaluation and Prediction**
    - The trained model is evaluated on the input data.
    - Predictions are made on the same data and rounded to produce output close to 0 or 1.

---

#### Output Metrics

- **Loss**: The Binary Cross-Entropy loss after training.
- **Accuracy**: The binary accuracy of the model.
- **Training Time**: Time taken for model training, rounded to 2 decimal places.
- **Predictions**: The model's predictions on the input data, rounded to the nearest integer (0 or 1).

---

