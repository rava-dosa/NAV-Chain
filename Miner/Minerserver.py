import sys, os
sys.path.insert(0, os.path.abspath('..'))

from flask import Flask,request
from Miner import Miner
from Utils.Navtime import NavTime
from Utils.Hash import CalculateFileHash

app = Flask(__name__)
miner = Miner(CalculateFileHash("/home/gaurav/NAV-Chain/demo/id_rsa.pub"),"","","")
time = NavTime()
@app.route("/getNewsFromClient",methods=["POST"])
def getNewsFromClient():
    ip=request.remote_addr
    # print(request.)
    user_id=request.json["id"]
    text=request.json["text"]
    genre=request.json["genre"]
    miner.ReceiveContent(miner.id,user_id,text,genre)
    miner.clientIp.append(ip)
    return ""

@app.route("/getNewsfromPeer",methods=["POST"])
def getNewsfromPeer():
    ip=request.remote_addr
    user_id=request["id"]
    text=request["text"]
    genre=request["genre"]
    miner_id=request["miner_id"]
    miner.ReceiveContent(miner_id,user_id,text,genre)
    miner.peerIp.append(ip)

@app.route("/sendNewsToClient",methods=["GET"])
def sendNewsToClient():
    ip=request.remote_addr
    user_id=request["id"]
    newBlockid=request["blockid"]
    return "newBlockid"

def main():
    app.run(host='0.0.0.0', port=8005)

if __name__ == '__main__':
    main()
