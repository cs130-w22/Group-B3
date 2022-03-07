const path = require("path");//accesss to file path
const express = require("express");//access to express
const multer = require("multer");//access to multer
const cors = require("cors");// for http
const res = require("express/lib/response");
const fs = require("fs");
const admZip = require("adm-zip");
const fetch = require('node-fetch');
const open = require("open");
const FormData = require("form-data");

const folder = fs.readdirSync(__dirname +'/'+'Images/');
const downName = "ZippedPhotos.zip";
const port = 8700;

const application = express();

application.use(cors());
application.use(express.static(path.join(__dirname, '/public')));


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
	//console.log(req.files);
	const formData = new FormData();

	var q = new admZip();
	for (var i = 0; i < folder.length; i++) {
		q.addLocalFile(__dirname + '/' + 'images/' + folder[i])
	}
	var data = q.toBuffer();
	formData.append('data', data);

	console.log(data);
	//download(data);
	open('http://127.0.0.1:8000/handlepost');
	fetch('http://127.0.0.1:8000/handlepost', {
		method: 'POST',	
		body: formData,
	})
	
		.then(response => response.content)
		.then(result => {
			console.log(result);
		})
		.catch(error => {
			console.error('Error:', error);
		});

	/*res.send("Files Uploaded");*/
});

function download(data) {
	console.log('....');
	console.log(data);
	console.log('.....');
	//res.set('Content-Type', 'application.octet-stream');
	//res.set('Content-Disposition', `attachment; filename=${downName}`);
	//res.set('Content-Length', data.length);
	res.send(data);
}

/*
application.get("/download", (req, res) => {
	var q = new admZip();
	for(var i = 0; i < folder.length; i++){
		q.addLocalFile(__dirname + '/' + 'Images/' + folder[i])
	}

	const data = q.toBuffer();
	res.set('Content-Type', 'application.octet-stream');
	res.set('Content-Disposition', `attachment; filename=${downName}`);
	res.set('Content-Length', data.length);
	res.send(data);
})*/

//********** */
//USELESS BUT WILL USE IF CURRENT ZIP DOWNLOAD IS NOT WHAT WE NEED
//********** */
/*
application.get('/compress', (req, res) => {
	res.render('compress')
})

application.post("/compress", (req, res) => {
	var zip = new admzip();
	var output = Date.now() + "output.zip";
	if(req.files){
		req.files.forEach((file) => {
			console.log(file.path)
			zip.addLocalFile(file.path)
		});
		fs.writeFileSync(output, zip.toBuffer());
		res.download(output, (error) => {
			if(error){
				req.files.forEach((file) => {
					fs.unlinkSync(file.path)
				});
				fs.unlinkSync(output)
			}
			req.files.forEach((file) => {
				fs.unlinkSync(file.path)
			});
			fs.unlinkSync(output)
		})
	}
});
*/
//localhost 5000


function uploadFiles() {
	var files = document.getElementById('file_upload').files;
	if (files.length == 0) {
		alert("Please first choose or drop any file(s)...");
		return;
	}
	var filenames = "";
	for (var i = 0; i < files.length; i++) {
		filenames += files[i].name + "\n";
	}
	alert("Selected file(s) :\n____________________\n" + filenames);
}


application.listen(port, () => {
	console.log("Starting server at http://localhost:" + port);
});



