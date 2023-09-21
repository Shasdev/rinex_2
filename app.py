import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import streamlit as st
import joblib
model=joblib.load('spam ham')
st.title('SPAM HAM CLASSIFIER')
ip=st.text_input('ENTER YOUR TEXT')
op=model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
                                
