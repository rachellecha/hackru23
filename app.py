import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the model from a pickle file
with open('model_final.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    data_precip = [0.1574193548, 0.1389285714, 0.134516129, 0.1266666667, 0.2109677419, 0.2, 0.1680645161, 0.2432258065, 0.05333333333, 0.2248387097, 0.05933333333, 0.2074193548]
    precip1 = 0.00


    month = request.form['month']
    day = request.form['day']
    hour = request.form['hour']
    minute = request.form['minute']
    fom = request.form['from']
    to = request.form['to']
    route = request.form['line']
    precip =  data_precip[int(request.form['month'])-1]

    # Preprocess the input data
    input_data = [[month, day, hour, minute, fom, to, route, precip]]
    # TODO: add preprocessing code here

     # Make a prediction using the loaded model
    prediction = model.predict(input_data)

    # Return the prediction to the user
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)