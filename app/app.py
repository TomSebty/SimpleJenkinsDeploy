from flask import Flask, request, render_template

app = Flask(__name__)

# Initialize a counter
counter = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global counter
    if request.method == 'POST':
        counter += 1
    return render_template('index.html', count=counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)