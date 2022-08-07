from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])

def index():
    height = 0
    weight = 0.000
    bmi = ''
    if request.method == 'POST' and 'height' and 'weight' in request.form:
        height = float(request.form.get('height'))/100
        weight = float(request.form.get('weight'))
        
        if(height == 0):
            raise ZeroDivisionError("height must not be zero!")
        elif(height < 0 or weight < 0):
            raise ValueError("height and weight must be non-negative!")
        
        bmi = calc_bmi(weight, height)
    return render_template('index.html', result=bmi,)

def calc_bmi(weight, height):
    bmi = round(weight/height**2, 2)  # *calc BMI and limit the value to 2 decimal places
    return bmi
