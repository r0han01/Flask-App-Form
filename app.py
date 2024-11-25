from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for a simple backend processing (e.g., form submission)
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('name')
        age = request.form.get('age')
        # Process the data (for now just print it)
        return f'Thank you {name}! You are {age} years old.'

if __name__ == '__main__':
    app.run(debug=True)
