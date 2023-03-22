# Network-Stress-Test-Tool
This is a network stress test tool using python that includes a GUI
## Installation
there is no installation, just download the python file 
## Converting to .exe
- open the folder location of **tool.py** and type **cmd** and **enter** in the top left
- enter these into the command prompt: 
```bash
pip install pyinstaller
```
```bash
pyinstaller --onefile -w tool.py
```
- **--onefile** makes the exe compact instead of having multiple files
- **-w** hides the command prompt when the it is running
## How to use tool
- enter the network IP
- enter amount of users you want to simulate
- enter the duration of the test
- click run and confirm 
- ![GUI](https://user-images.githubusercontent.com/124969847/226770248-5fd2f5f4-91ad-4fa3-88b7-11b619e5d14a.png)
# ⚠️DISCLAIMER/WARNING⚠️
- **THIS IS FOR EDUCATIONAL PURPOSES ONLY**
- This tool is intended for network stress testing and should only be used on systems that you have explicit permission to test. It is not intended for malicious purposes, such as denial-of-service attacks or any other form of cyber attack. I am not responsible for any misuse or damage caused by this tool.
