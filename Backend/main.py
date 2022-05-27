from Pipeline import Pipeline
import os

if __name__ == "__main__":
    parseArgs = None

    pipe = Pipeline()
    pipe.process_all()

    os.remove('./input_images/input.zip')

    front_end_dir = './../NodejsWebApp1/NodejsWebApp1/Images'
    for file in os.listdir(front_end_dir):
        os.remove(os.path.join(front_end_dir, file))
