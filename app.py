
from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction Form Page
@app.route('/predict_page')
def predict_page():
    return render_template('predict.html')

# Prediction Logic
@app.route('/predict', methods=['POST'])
def predict():

    age = int(request.form['age'])
    studytime = int(request.form['studytime'])
    failures = int(request.form['failures'])
    absences = int(request.form['absences'])
    g1 = int(request.form['g1'])
    g2 = int(request.form['g2'])

    famsup = request.form['famsup']
    schoolsup = request.form['schoolsup']
    paid = request.form['paid']
    higher = request.form['higher']
    address= request.form['address']

    # Simple Prediction Logic

    if failures >= 3 or absences > 20 or g1 < 8 or g2 < 8:
        prediction = "Student is likely to Dropout"

    elif famsup == "no" and schoolsup == "no":
        prediction = "Student may face academic risk due to lack of support"

    elif higher == "no":
        prediction = "Student has low higher education motivation"
    
    elif address == "rural": 
        prediction = "Student may Need Additional Academic Support"

    else:
        prediction = "Student is likely to Continue Studies"

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

