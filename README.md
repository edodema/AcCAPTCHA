# AcCAPTCHA

An accessible CAPTCHA test, for more info check the [report.pdf](docs/report.pdf)
## File System
```  
.
├── assets
├── docs
│   ├── assets
│   │   ├── images
│   │   └── plantuml
│   │       ├── activity
│   │       ├── pdf
│   │       │   ├── activity
│   │       │   └── sequence
│   │       └── sequence
│   ├── modules
│   └── old
├── gui
│   ├── static
│   │   ├── assets
│   │   │   ├── captcha
│   │   │   │   └── samples
│   │   │   └── images
│   │   │       └── samples
│   │   │           ├── airplane
│   │   │           ├── car
│   │   │           ├── cat
│   │   │           ├── dog
│   │   │           ├── flower
│   │   │           ├── fruit
│   │   │           ├── motorbike
│   │   │           └── person
│   │   ├── css
│   │   ├── js
│   │   └── logs
│   └── templates
└── src
    ├── finger_count
    ├── image_classification
    ├── text_recognition
    ├── utils
    └── word_reading
```

## Requirements
- Flask
- Google Speech API
- MMPOSE
- NumPy
- OpenCV
- PyAudio
- Python

For more informations check the requirements file [requirements.txt](requirements.txt)

## Execution
Run the script file 
```
$ chmod u+x ./run.sh
$ ./run.sh
```
