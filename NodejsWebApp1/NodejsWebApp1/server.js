const path = require("path");//accesss to file path
const express = require("express");//access to express
const multer = require("multer");//access to multer
const cors = require("cors");// for http
const res = require("express/lib/response");
const fs = require("fs");
const admZip = require("adm-zip");
//Constants
const folder = fs.readdirSync('./images');
const downFPath = "../../Backend/output_images/Crop.zip";
const port = 5000;

const application = express();
const shell = require('shelljs');

application.use(cors());
application.use(express.static(path.join(__dirname, '/public')));

const fileStorage = multer.diskStorage({
	destination: (req, file, cb) => {
		cb(null, "./Images"); //directory to where file is gonna be stored when uploaded
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
application.post("/multiple", upload.any("Images"), (req, res) => {
	
	console.log(req.files);

	const zip = new admZip();
	if(req.files){
		req.files.map(file => {
            zip.addLocalFile(file.path);
        });

		zip.writeZip('../../Backend/input_images/input.zip');
	}
	//zip(res);
	shell.cd('../../Backend');
	shell.exec('bash ./predict.sh');

	res.download('./output_images/Crop.zip');
	shell.cd('../NodejsWebApp1/NodejsWebApp1');
/*
	var zip2 = new admZip('../../Backend/output_images/Crop.zip');
	const data = zip2.toBuffer();
 	res.set('Content-Type', 'application.octet-stream');
 	//res.set('Content-Disposition', `attachment; filename=${'Crop.zip'}`);
 	res.set('Content-Length', data.length);
 	res.send(data);
	res.send(downFPath);*/
	/*
	var q = new admZip();
	for (var i = 0; i < folder.length; i++) {
		q.addLocalFile(__dirname + '/' + 'Images/' + folder[i])
	}
	q.writeZip('../../Backend/input_images/input.zip');
	shell.exec('../Backend/predict.sh');
	//post script download portion
	res.send(downFPath);
	*/
});


//download portion
/*
application.get("/download", (req, res) => {
	var q = new admZip();
	for (var i = 0; i < folder.length; i++) {
		q.addLocalFile(__dirname + '/' + 'Images/' + folder[i])
	}
	q.writeZip('../../Backend/input_images/input.zip');
	shell.exec('ls');
	//post script download portion
	//res.send(downFPath);
})
*/
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

/*
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
*/

application.listen(port, () => {
	console.log("Starting server at http://localhost:" + port);
});



