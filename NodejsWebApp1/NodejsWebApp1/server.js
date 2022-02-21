const path = require("path");//accesss to file path
const express = require("express");//access to express
const multer = require("multer");//access to multer
const cors = require("cors");// for http
const res = require("express/lib/response");
const fs = require("fs");
const admZip = require("adm-zip");

const folder = fs.readdirSync(__dirname +'/'+'Images/');
const downName = "ZippedPhotos.zip";
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

//download portion

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
})

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
application.listen(port, () => {
	console.log("Starting server at http://localhost:" + port);
});