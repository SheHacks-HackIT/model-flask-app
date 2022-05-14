# model-flask-app
The server that is responsible for training our model and predicting a result to send it over a request.
Part of the KidErra project by SheHacks -- Hack !T.

The model is trained and saved in clf.pkl. You can find its source code in model/stressClassifier.py
The app is developed with Flask and sends back the prediction for the data coming as input to the /predict route.

