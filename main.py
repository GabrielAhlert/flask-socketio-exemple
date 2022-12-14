from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    socketio.emit('chat message',json)

if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0', port=8080)