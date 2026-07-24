from server.app import app
from server.models import Event 

events = []

if __name__ == "__main__":
    app.run(port=5555)