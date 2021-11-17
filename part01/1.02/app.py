from flask import Flask

app = Flask(__name__)
PORT = 5000

@app.route('/')
def index():
    return "Hello from the Dockerize flask app"

if __name__ == "__main__":
    print(f"Server started in port {PORT}")
    app.run(host='0.0.0.0', port=PORT)
    
