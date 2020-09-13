import sys, os
sys.path.insert(0, os.path.abspath('..'))

from flask import Flask
from Miner import Miner
from Utils.Navtime import NavTime
from Utils.Hash import CalculateFileHash

app = Flask(__name__)
miner = Miner(CalculateFileHash("/home/user/NAV-Chain/demo/id_rsa"))
time = NavTime()
@app.route("/getNewsFromClient",methods=["POST"])
def getNewsFromClient():
    ip=request.remote_addr
    user_id=request["id"]
    text=request["text"]
    genre=request["genre"]
    miner.ReceiveContent(miner.id,user_id,text,genre)
    miner.clientIp.append(ip)

@app.route("/getNewsfromPeer",methods=["POST"])
def getNewsfromPeer():
    ip=request.remote_addr
    user_id=request["id"]
    text=request["text"]
    genre=request["genre"]
    miner_id=request["miner_id"]
    miner.ReceiveContent(miner_id,user_id,text,genre)
    miner.peerIp.append(ip)

def main():
    app.run(host='0.0.0.0', port=8005)

if __name__ == '__main__':
    main()
