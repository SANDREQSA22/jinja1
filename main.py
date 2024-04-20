from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/music')
def king_musicans():
    # You can add dynamic content generation here using Python
    kings = ['Sting', 'B.B King', 'Michael Jackson ', 'Frank Sinatra', 'Freddie Mercury', 'Chuck Berry', 'Louis Armstrong', 'Bob Dylan', 'Princ']
    return render_template('kings.html', kings=kings)

if __name__ == '__main__':
    app.run(debug=True)
