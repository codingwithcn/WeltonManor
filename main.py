from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = ":sddsadasdsa"

@app.route('/', methods=['GET'])
def home():
  return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
  return render_template('about.html')

@app.route('/ratings', methods=['GET'])
def ratings():
  return render_template('ratings.html')

@app.route('/images', methods=['GET'])
def images():
  return render_template('images.html')

if __name__ == '__main__':
  app.run(
    host = '0.0.0.0',
    port = '8080',
    debug = True
  )