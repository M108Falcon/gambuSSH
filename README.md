# gambuSSH: Graphical SSH Honeypot

gambuSSH is a commandline as well as graphical application that acts as a tarpit to defend against Dictionary as well as DDoS attacks on SSH Ports.  
The app acts as a decoy SSH port that traps autmoized scripts for indefinite amount of time, wasting a lot of attacker's time and also slowing down their attacks on other open SSH ports worldwide.

*The app works exclusively on Linux systems for now*

## Working Prinicple
SSH has no limit on banner length as well as timeout limit for conneciton in it's source code. The app utilizes the same principal to trap  attackers and botnets. As soon as the connection is established the script sends a random flag of arbitrary length as a response and keeps the automated script busy.

### Features
1. Multithreaded applicaiton.
2. Since we do not need to authenticate the user, need for cryptographic key exchange in traditional SSH is elminated. This keeps the script  pretty lightweight.
3. Only default system modules that are present in Linux distros are used to enhance security by avoiding extra modules. This also means **commandline script has no additional dependencies.**
4. Bounded semaphores to control max no of connecitons.


### Usage
Use the following flags alongwith the commandline script to enter your own parameters.
```bash
-h or --help to display help menu
-f or --file to speicfy location of custom configuration file
-p or --port to specify port number (default 8000)
-m or --max connections to specify maximum number of connections (default 3000)
-p or --port to specify port number (default 8000)
-m or --max connections to specify maximum number of connections (default 3000)
-4 to listen on IPv4
-6 to listen on IPv6
```

#### NOTE: The application is still in early stages of development, thus, you may expect crashes sometimes. We are experiencing difficulties with Linux Policy kits, thus GUI hasn't been added to main branch although CLI app is fully functional.


### Future
Following features will be added to future updates:
1. Self contained executable binaries.
2. Service Integration with System Daemons(Mainly SystemD for start).
3. Fully working GUI with policy kit implementation.
