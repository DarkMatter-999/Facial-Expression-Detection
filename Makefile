getfiles:
	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js/master/dist/face-api.min.js -O ./FaceDetect/face-api.min.js
	mkdir ./FaceDetect/models
	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js-models/master/face_expression/face_expression_model-weights_manifest.json -O ./FaceDetect/models
	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js-models/master/face_expression/face_expression_model-weights_manifest.json -O ./FaceDetect/models

	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js-models/master/face_landmark_68/face_landmark_68_model-shard1 -O ./FaceDetect/models
	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js-models/master/face_landmark_68/face_landmark_68_model-weights_manifest.json -O ./FaceDetect/models

	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js-models/master/face_landmark_68_tiny/face_landmark_68_tiny_model-shard1 -O ./FaceDetect/models
	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js-models/master/face_landmark_68_tiny/face_landmark_68_tiny_model-weights_manifest.json -O ./FaceDetect/models

	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js-models/master/face_recognition/face_recognition_model-shard1 -O ./FaceDetect/models
	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js-models/master/face_recognition/face_recognition_model-shard2 -O ./FaceDetect/models
	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js-models/master/face_recognition/face_recognition_model-weights_manifest.json -O ./FaceDetect/models

	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js-models/master/tiny_face_detector/tiny_face_detector_model-shard1 -O ./FaceDetect/models
	wget https://raw.githubusercontent.com/justadudewhohacks/face-api.js-models/master/tiny_face_detector/tiny_face_detector_model-weights_manifest.json -O ./FaceDetect/models
