from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = ":sddsadasdsa"

@app.route('/', methods=['GET'])
def home():
  return 'hello, site running correctly'

if __name__ == '__main__':
  app.run(
    host = '0.0.0.0',
    port = '8080',
    debug = True
  )