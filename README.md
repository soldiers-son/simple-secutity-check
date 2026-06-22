# simple-secutity-check

POS.py Version: 1.0

Python: 3.11+

Platform: Windows / Linux / Mac

Dependencies: 

----------------------------------------------------
0. Acknowledgments
----------------------------------------------------
Thank you to the open source community, whose 
work makes this project possible.

----------------------------------------------------
1. Introduction
----------------------------------------------------
This is a basic automation script that performs updates and security checks for Linux(currently only supports Ubuntu)

Author: soldiers-son
----------------------------------------------------
2. Features
----------------------------------------------------
-Terminal Based
Performs autmated update &full upgrade
-Nmap for local network scanning
-Clamscan for file scanning
----------------------------------------------------
3. Requirements
----------------------------------------------------
nmap
clamscan
----------------------------------------------------
4. Installation
----------------------------------------------------
1. Clone or download this repository.
2. Place the project folder on your desktop or 
   desired directory.
3. Install required dependencies.

----------------------------------------------------
5. Dependencies
----------------------------------------------------
Install required packages via pip:

   sudo apt install nmap && sudo apt install clamscan

6. Usage
----------------------------------------------------

1.In terminal run "ifconfig" and find your host ip
2. Update 'server_sec.py' with your host ip
4. Run the application:

   Ubuntu:
   $ sudo python3 server_sec.py

----------------------------------------------------
7. Future Goals
----------------------------------------------------
Planned expansions include:
-OpenSCAP for vulnerablity scans


----------------------------------------------------
8. Contributing
----------------------------------------------------
Suggestions and improvements are welcome. 
Fork the repo, make your changes, and submit a PR.

----------------------------------------------------
9. License
----------------------------------------------------
This project is open source under the MIT License.

----------------------------------------------------
10. Contact
----------------------------------------------------
Author: soldiers-son

GitHub: (https://github.com/soldiers-son?tab=repositories)

Email: (soldiers.son1618@gmail.com)
