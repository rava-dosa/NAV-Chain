import sys, os
sys.path.insert(0, os.path.abspath('..'))

from flask import Flask
from Miner import Miner
from Utils.Navtime import NavTime

app = Flask(__name__)
miner = Miner("1")
time = NavTime()
@app.route("/sendNews",methods=["POST"])
def sendNews():
    ip=request.remote_addr
    user_id=request["id"]
    text=request["text"]
    genre=request["genre"]
    miner.ReceiveContent(user_id,text,genre)


def main():
    app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()
