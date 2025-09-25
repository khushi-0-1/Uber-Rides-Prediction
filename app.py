import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # get inputs from form (4 values)
        int_features = [int(x) for x in request.form.values()]

        # convert to 2D numpy array
        final_features = np.array([int_features])   # shape (1, 4)

        # make prediction
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        return render_template(
            'index.html',
            prediction_text=f"Number of Weekly Rides Should be {math.floor(output)}"
        )

    except Exception as e:
        # debugging ke liye error browser par print karo
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run()
