from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained xG prediction model
model = joblib.load('xg_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])

        # Predict xG
        prediction = model.predict(input_df)[0]

        return jsonify({'predicted_xG': round(float(prediction), 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
