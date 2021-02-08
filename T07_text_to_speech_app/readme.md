# Python Application: Text To Speech Application
**1- Install PyQt5 & gtts Library by cmd**

`pip install PyQt5`
`pip install gtts`

**2- I designed the front end part (text_to_speech.ui) by Qt Designer software, if you want to make any modifications, you can download the software through the link below**

[Qt Designer software (Link)](https://build-system.fman.io/qt-designer-download)

**3- if you made any modification, save your work on the Desktop and you will have a .ui file, to convert it to python file (.py), open cmd and navigate the directory of the file and type thef following commands**

`cd Desktop`

`pyuic5 -x text_to_speech.ui -o text_to_speech.py`

`pyrcc -x source.qrc -o source.py`

**Note: the converted python file will be saved on the Desktop as (text_to_speech.py)**


**4- Run the python file and put your text and press on "convert to audio" button**

![alt text](https://github.com/AI-MOO/PythonProjects/blob/master/T07_text_to_speech_app/images_for_explination/1.PNG?raw=true)

**5- check the output file to listen to your generated audio file**

![alt text](https://github.com/AI-MOO/PythonProjects/blob/master/T07_text_to_speech_app/images_for_explination/2.png?raw=true)
