# AcCAPTCHA

### Speech
- Recall to install in Docker the correct dependencies: [https://pypi.org/project/SpeechRecognition/#Requirements](https://pypi.org/project/SpeechRecognition/#Requirements)
#### Read something aloud.
- We should generate n words and do not care about order.

#### Finger counting.
- You should hold your position for some seconds and have a mean to get an answer.
- If it may be too difficult to select a ROI of the correct size you could select a dimension for a given aspect ratio or optionally use quadrants, otherwise pick the dimension of a quadrant and pick it randomly.
- Add a timer and a number of frames (according to the threshold) to get the correct answer

### Misc
- Maybe put everything in a Docker image.
- Add a Verification/Validation/Authentication module for each module, it should also take care of the rest e.g. setting a ROI or picking random words.
- Cite the corpus here [https://github.com/dwyl/english-words](https://github.com/dwyl/english-words)
- In docker update pip to latest version.
- Dialog for many fingers.
- Explain what directories do, maybe with different readmes depedning on the subdir.
- We also have pronunciation issues in voice recogn.
- Add a default setting in which we assume a user is totally able to use everything.
- scripts to build a docker image.

### Future works
- Save user configuration as cookies.
- more accessible and customizable gui for colorblind people.
- Dyslexia font, dark mode, invert color.
- search for colorblind colors, add checkboxes for that too maybe or use a universal colorbind palette (worst case)
- Hearing
- Move your head or face into a specific box, box may have different colors.

# REAL

## File System.
## Installation

## Requirements
- Python
- 
