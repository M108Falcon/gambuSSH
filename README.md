# gambuSSH: Graphical SSH Honeypot

gambuSSH (word play for ambush and g to signify graphical) is a **cli** as well as **GUI** based application.
The application will work with Systemd for starters and support for other init systems such as sysvinit or runit may get added later.

## Working Principle:
gambuSSH serves as a decoy SSH port to prevent SSH bruteforce and DDos attacks by numerous script kiddies that use automated scripts to try crack/crash different servers with default SSH port open worldwide.
As soon as the connection is established, the application returns random flags in arbitrary amount of time so to keep the tool from disconnecting, hence wasting a lot of their time.

## Language and Frameworks used:
- [x] Python for base engine.
- [x] Gnome GTK for for GUI(Utilising Javascript for GUI alongwith integrations API for C/C++, Python and Rust) as it provides easy Linux Desktop integration.

### Features:
- [ ] The script/app will use 1 OS Thread as a process.
- [ ] Support for commandline args for cli application.
- [ ] Service integration with init system (Systemd here).
- [ ] Create a log destination and file.
- [ ] Responive and real-time updatable GUI.


### Additional Features:
- [ ] If possible, a functionality to catch the IP address and send it to Admin's mobile as a text alert after failed attempts.
- [ ] A compilable app that can be compiled using make/cmake and support simple config file edit rather than change in source code.

## Algorithm

1. Import OS and networking libs.
2. Use sysargv utility in the programming language to accept commandline args.
3. Specify port number and machine's ip address.
4. Make a listner to listen at specified Port.
5. If connection establishes, send it to another function that spits out random stmts after certain set period of time unitl connection terminates.
6. Assign Step 4 and 5 single OS Thread.

*We need to think abt addition of log files as well as GUI integration as we are not fully experienced in making one, but here is the idea presented into simple steps.*
