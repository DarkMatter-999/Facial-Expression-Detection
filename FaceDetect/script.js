const video = document.getElementById('video')

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
  faceapi.nets.faceExpressionNet.loadFromUri('/models')
]).then(startVideo)

function startVideo() {
  navigator.getUserMedia(   //only works on chrome :'(
    { video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}

video.addEventListener('play', () => {
  const wsUri = "ws://127.0.0.1:5001";
  websocket = new WebSocket(wsUri);
  websocket.onopen = function(evt) { console.log("WS Connected") };

  const canvas = faceapi.createCanvasFromMedia(video)
  document.body.append(canvas)

  const displaySize = { width: video.width, height: video.height }
  faceapi.matchDimensions(canvas, displaySize)
  setInterval(async () => {

    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    const resizedDetections = faceapi.resizeResults(detections, displaySize)

    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
    try{
      //send feature locations
      // console.log(JSON.stringify(detections[0].landmarks._positions))
      websocket.send(JSON.stringify(detections[0].landmarks._positions))
    }
    catch(err){}  //catch when no face is detected
  }, 10)
})
