#SnapCatcher
SnapCatcher is a simple solution for taking a photo via webcam and sending it to a specific email everytime someone log into your account. (Current only support windows, but it should work on linux if the scheduler setup is modified)
To use it you will need to: 
* Have python3 installed
* Have a webcam
* Have a email

execute the setup.bat
Modify the main.py parameters.
Then create a task in the task scheduler to run evertime your workstation unlock, and select the start.bat as the program to execute, and set the Start in. ([please check](https://superuser.com/questions/1214736/windows-10-scheduled-tasks-with-workstation-lock-unlock-not-being-triggered)])

Please note, this repo is for educational purposes only. No contributors, major or minor, are to fault for any actions done by this program.
