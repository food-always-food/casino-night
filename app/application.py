from flask import render_template, session, request, redirect, Flask
from flask_socketio import SocketIO, emit, send, join_room
from time import sleep
import eventlet, reader

eventlet.monkey_patch()

application = Flask(__name__)
application.config["SECRET_KEY"] = "1023912038109823aljksdflkajds"
socketio = SocketIO(application, async_mode=None)
app = application


@app.route("/", methods=["GET"])
def welcome():
    return render_template("home.html", page={"background": "test.jpg"})


@socketio.on("connect")
def test_connect():
    print("recevied connection")


@socketio.on("server")
def test_connect(data):
    print(data)
    id = reader.get_card()
    emit("client", id)
    join_room("page")


def wait_for_card():
    card_sent = False
    while card_sent == False:
        socketio.emit("client", "second function", room="page")
        card_sent = True


if __name__ == "__main__":
    socketio.run(app, debug=False)
