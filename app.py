
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
import joblib

def spam_ham_classifier(input_text):
    model = joblib.load('spam ham')
    prediction = model.predict([input_text])
    return prediction[0]

# Example usage:
input_text = "ENTER YOUR TEXT HERE"  # Replace with your input text
prediction = spam_ham_classifier(input_text)
print(prediction)

                                
