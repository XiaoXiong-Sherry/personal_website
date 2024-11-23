from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True

# Create a context processor to make year available to all templates
@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/research')
def research():
    return render_template('research.html')

if __name__ == '__main__':
    app.run(debug=True) 