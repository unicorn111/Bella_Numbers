from flask import Flask, render_template, request
app = Flask(__name__)
from bella_numbers import bella_number

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = bella_number(int(request.form['number']))  
        return render_template('index.html', ind=request.form['number'], num=num)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
