const path = require("path");//accesss to file path
const express = require("express");//access to express
const multer = require("multer");//access to multer
const cors = require("cors");// for http
const port = 5000;

const application = express();

application.use(cors());
application.use(express.static(path.join(__dirname, 'public')));
const fileStorage = multer.diskStorage({
	destination: (req, file, cb) => {
		cb(null, "./images"); //directory to where file is gonna be stored when uploaded
	},
	filename: (req, file, cb) => {
		cb(null, file.originalname);
	},
});


application.get("/", (req, res) => {
	res.sendFile(path.join(__dirname, "index.html"));
});


const upload = multer({ storage: fileStorage });


// Multiple Files Route Handler
application.post("/multiple", upload.any("images"), (req, res) => {
	console.log(req.files);
	res.send("Files Uploaded");
});
//localhost 5000
application.listen(port, () => {
	console.log("Starting server at http://localhost:" + port);
});