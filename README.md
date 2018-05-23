Tool Description:
===

This tool is used to find files that are recently created or modified in the user's machine.



Technical Specification:
===

* Windows 10 Operating System.
* Python 2.7
* No other dependencies or third-party library needed.



Usage:
===
As illustrated below, the user simply needs to specify the script name, the path to directory where new or
modified files need to be checked, the time span in minutes and finally the flag that tell the script whether 
to print the results to the screen (P) or save them to a file (S).

Below is a sample run that print a list of files that are created within the last 30 minutes to the screen.

C:\Python27>python LocateNewFiles.py C:\PathToDirectory 30 P

If no files printed to the screen then all the files in that directory might be created/modified
before the last 30 minutes. The user can then choose to either increase the time span or stop investigating
if he is satisfied with the results.

 

