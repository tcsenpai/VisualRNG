import cv2
import hashlib
import re
import random
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import time

app = FastAPI()

vCapture = cv2.VideoCapture(0)
if (vCapture.isOpened() == False):
    print("Error opening video stream or file")
    exit()
    
# The following method return a number composed from all the digits in a string one after another
def get_number(s):
    ints = re.findall('(\d+)', s)
    intString = ''.join(ints)
    return intString      

def vRandGo():
    global vCapture
    ret, frame = vCapture.read()
    hash = hashlib.sha256(frame).hexdigest()
    print(hash)
    seed = get_number(hash)
    print(seed)
    random.seed(seed)
    visualrandom = random.randrange(1, 10)
    print(visualrandom)
    #cv2.imshow('Video', frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
    return {"visualrandom": visualrandom, "seed": seed, "hash": hash, "time": time.time()}
    
@app.get("/")
async def root():
    return {"rand": vRandGo()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1122)
    

