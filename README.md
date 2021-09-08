### Face tracking with Python an JS [DEPRECATED]

An application to track, display, and interact with facial expression using python, [Ursina Engine](https://github.com/pokepetter/ursina), and [Faceapi.js](https://github.com/justadudewhohacks/face-api.js/)


#### Usage
This app needs to download pretrained facial detection models before operation:
```
make getfiles
pip3 install -r requirements.txt
```

Afterwards the App can be run by :
```
python3 main.py
```

Then open the web interface on a browser (Chrome/Chromium preferably) and give it permissions to use the camera.
Now we are able to move and rotate the cube (or user provided .obj file) in the window
