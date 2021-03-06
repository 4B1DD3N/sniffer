# Sniffer (pre-alpha)

Sniffer is a binary which can capture and analyze network packets on a given device. The aim of the application is to offer DNI selectors for cybersurveillance purposes, based on NSA's Unified Targeting Tool.

The tool is being developed as part of a Bachelor's degree final work together with systematic reviews (not yet open sourced) of the NSA operations like PRISM, Bullrun, etc. 

## Do not use in production.

More information soon.

## Roadmap

- [x] Config file
- [x] Link layer parsing (Ethernet)
- [x] Internet layer parsing
  - [x] IPv4
  - [x] IGMP
  - [x] ICMP
- [x] Transport layer parsing (PDU's)
  - [x] TCP
  - [x] UDP
- [ ] Identify protocols inside TCP/UDP
  - [x] By port number
  - [ ] More... 
- [ ] Application layer parsing (these will be used for the demo at the end of the final work)
  - [ ] HTTP
  - [ ] DNS
  - [ ] FTP
  - [ ] Telnet
- [ ] DNI Selectors
- [ ] Improve Makefile (all, clean, install, prune, help)
  - [ ] All
  - [ ] Clean (cache, *.pyc, etc)
  - [x] Install
  - [ ] Prune
  - [x] Help
  - [x] Tests
- [ ] Documentation
- [ ] Unit Testing
  - [x] Setup
  - [ ] Test all objects
- [ ] Docblocks

### Installation

Makefile assumes Python version 2 and pip package manager are installed on the system.

```
make install
```

### Run the application

```
make run
```

### Cleanup compiled Python bytecode

```
make clean-pyc
```

![](sniffer.PNG)

## Documentation

### Commands

- clear (alias l): clear the terminal
- commands (alias c): list all the commands
- device set (alias ds): set the device to capture
- start (alias s): start capturing traffic on the device
- exit (alias e): exit the terminal
- aliases (alias a): list the commands with aliases