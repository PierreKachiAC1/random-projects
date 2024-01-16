from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import numpy as np
import pandas as pd
import tensorflow as tf
import numpy as np

app = Flask(__name__)

MAX_FEATURES = 200000  
vectorizer = TextVectorization(
    max_tokens=MAX_FEATURES,
    output_sequence_length=1800,
    output_mode='int'
)

# Load the toxicity model
toxicity_model = load_model('toxicity.h5')  
df = pd.read_csv('train.csv')
X = df['comment_text']

vectorizer.adapt(X.values)

@app.route('/predict', methods=['POST'])
def predict():
    
    data = request.get_json()
    text = data["text"]
    try:
        vectorized_text = vectorizer(np.array([text]))
        prediction = toxicity_model.predict(vectorized_text)
        result_string = ', '.join(map(str, prediction[0]))
        return jsonify({'result': result_string})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
