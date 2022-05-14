from array import array
import numpy as np
from flask import Flask, jsonify, request
import pandas as pd
import joblib


# Declare a Flask app
app = Flask(__name__)

# Main function here
# ------------------
@app.route('/predict', methods=['POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        clf = joblib.load("clf.pkl")
        
        # Get values through input bars
        # height = request.form.get("height")
        # weight = request.form.get("weight")
        query = request.get_json()

        data = query['data']

        print(np.nan_to_num(data))

        
        
        # Put inputs to dataframe
        X = pd.json_normalize(np.nan_to_num(data)).replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)

        # Get prediction
        prediction = clf.predict(X)[0]
        
    else:
        prediction = ""
        
    # return render_template("website.html", output = prediction)
    print(prediction)
    return jsonify(prediction)



# Running the app
if __name__ == '__main__':
    app.run()