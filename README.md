
# SCP-SL-Reverse-Engineering

This repository is a reverse engineering ARCHIVE of the game SCP:Secret-Laboratoratory.
It contains a dump of all the game libraries that each one imports, as well as separate folders with decompilations to C-like code: 4 main libraries:


SCPSL.exe == 140000000.SCPSL.exe


SC-AC.dll == 180000000.SL-AC.dll


UnityPlayer.dll == 7ffda05f0000.UnityPlayer.dll


GameAssembly.dll == 7ffd95060000.GameAssembly.dll


Other imported libraries do not require decompilation etc.: they are system ones.
You can also use anti-obfuscation programs to read C++ code etc.
I chose this option, the following programs were used:

IDA == https://hex-rays.com/ida-free

Cutter == https://github.com/rizinorg/cutter

Ghidra == https://github.com/NationalSecurityAgency/ghidra

Dump program 1:PE-sieve: scans the given process, recognizes and removes various potentially harmful implants.

Dump program 2: x64dbg (in this case you need to use x32dbg + plugin) == https://x64dbg.com/

A script file for Ghidra in Python will also be added to store all functions in C-like code.

Folder with a file named: Dump-Files
It collects everything that SCPSL imports, so you can use these dumps in other programs as you see fit ○( ＾皿＾)っ Hehe…


## Authors

- [@uakabibara01](https://github.com/uakabibara01)


## Installation

Using

```bash
gh repo clone uakabibara01/SCP-SL-Reverse-Engineering
```

## !

#### Remark 1

The author is not responsible for the use of this archive, use solely for educational purposes.

![Logo](https://raw.githubusercontent.com/uakabibara01/uakabibara01/refs/heads/main/vn5K5O6d_400x400.jpg)

