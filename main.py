import numpy as np
import pickle
import pandas as pd
import time
import sys
from preprocessData import ModelInference

class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

def print_both(*args, **kwargs):
    """
    Print to both console and file
    """
    print(*args, **kwargs)
    with open("output_log.txt", "a") as f:
        print(*args, file=f, **kwargs)

# Redirect stdout to a file
sys.stdout = Logger("output_log.txt")

class NIDSClassifier:
    def __init__(self, model_path):
        # Load the sgboost model from the pkl file during initialization
        with open(model_path, 'rb') as f:
            self.sgboost_classifier = pickle.load(f)
        self.model_instance = ModelInference()

    def classify_data(self, input_data):
        input_of_model_array = np.array(input_data)
        # Reshape the array to match the shape expected by the model
        input_of_model_array = input_of_model_array.reshape(1, -1)
        # Use the sgboost model to make predictions
        predictions = self.sgboost_classifier.predict(input_of_model_array)
        return predictions

    def prediction(self, output):
        x = output[0]
        if x != 1:
            return 'No Current Threats..Benign State'
        else:
            return 'Be careful!!!! DDOS attack expected'

    def __call__(self, input_file):
        start_time = time.time()
        input_data = self.model_instance.preprocess_input(input_file)

        flag = False
        for input_d in input_data:
            predictions = self.classify_data(input_d)
            if predictions[0] == 1:
                print(self.prediction(predictions))
                flag = True
                break
        end_time = time.time()
        
        running_time = end_time - start_time
        print("Running time:", running_time, "seconds")
        if not flag:
            print(self.prediction(predictions))

if __name__ == '__main__':
    nids_classifier = NIDSClassifier('xgboost_model.pkl')
    output = nids_classifier("flows/outputFlows.csv")
    print(output)

# Reset stdout to the original value
sys.stdout = sys.__stdout__
