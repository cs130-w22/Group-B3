# Instructions

Use Git Bash to clone the Github repository. Then install Node.js and Anaconda. Go to this link: https://ucla.box.com/s/07xh668tuspsycyhzbvlowpngmljcmov
and download "ff.hd5" and put this file into the 'Backend' folder of your machine.

Change directories to "Group-B3/NodejsWebApp1/NodejsWebApp1/" then run the install.sh bash script.

This will install all the necessary libraries. After installation, the server will run and proceed to http://localhost:5000/ where you will be able to use the application.

# How to Run

## Setup
On initial start up run the following command in the Group-B3 directory:
```
./setup.sh
```
This will automatically run the setup for the environment required to run the model. But if that doesn't work as intended, 
you can manually setup the Backend modules by running the following commands: 
```
cd Backend
./setupBack.sh
cd ..
```
After running the setup shell scripts once you don't need to run it again to start the program.

## Program Start
You can start the program by running the following command in the command line
```
./run.sh
```

## Custom Weights
You can run the model using your own weights by replacing the weight file in the Backend directory. The weight file should be named [ff.hdf5]

