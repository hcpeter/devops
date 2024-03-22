from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None 
    if request.method == 'POST':
        try: 
            number1 = float(request.form['number1'])
            number2 = float(request.form['number2'])
            operation = request.form['operation']

            if operation == 'add':
                result = number1 + number2
            elif operation == 'subtract':
                result = number1 - number2
            elif operation == 'multiply':
                result = number1 * number2
            elif operation == 'divide':
                result = number1 / number2
        except ValueError:
            result = "Please enter valid numbers."

    return render_template('index.html', result=result)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)  #pragma: no cover