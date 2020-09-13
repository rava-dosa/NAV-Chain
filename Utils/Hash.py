import hashlib
def CalculateFileHash(filename):
	with open(filename,"rb") as f:
		byte = f.read()
		readable_hash = hashlib.sha256(byte).hexdigest()
		return readable_hash


