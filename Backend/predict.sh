#! /bin/bash
conda.bat env create -f environment.yml -n picModel
conda.bat run -n picModel python main.py