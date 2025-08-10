
# SCP-SL-Reverse-Engineering

This repository is a reverse engineering ARCHIVE of the game SCP:Secret-Laboratoratory.
It contains a dump of all the game libraries that each one imports, as well as separate folders with decompilations to C-like code and ASM code: 4 main libraries:


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

Dump program 2: x64dbg (in this case you need to use x32dbg + plugin ScylaHide ) == https://x64dbg.com/

A script file for Ghidra in Python will also be added to store all functions in C-like code and ASM code. As the script name suggests,
scriptC.py is for C-like code and scriptASM.py is for your own purposes.

Folder with a file named: Dump-Files
It collects everything that SCPSL imports, so you can use these dumps in other programs as you see fit ○( ＾皿＾)っ Hehe…

## Additionally

Also in the text file SC-AN.dll.txt there is my own analysis of the anti-cheat, but it is not complete, since there are many functions,
but the main and most important part of the anti-cheat is written there, since the largest functions were analyzed.
In the future, over time, when I analyze everything, I will write a reference about each of the libraries, 
what it does, what it contains, etc., but for now, only about SC-AN.dll :( .

## Files

SCPSL_Dump.rar == Contains all dump and decompilation files.

Dump-Files.rar == Contains only library dumps and what they import in a separate text file.

Decompiled LibrariesC.rar == Contains only folders with decompiled code of all 4 libraries into C-like code.

Decompiled LibrariesASM.rar == Contains decompiled code of all 4 libraries in ASM code.

## Authors

- [@uakabibara01](https://github.com/uakabibara01)


## Using

Download WinRar to unpack the archive.

We download the latest release, unpack the files and get everything we need, then it's up to you:
In the Decompiled Libraries file there are 2 folders, one Decompiled LibrariesC there is C-like code and in Decompiled LibrariesASM ASM code for each of the 4 libraries, 
where the function files are located.
and in Dump-Files there are folders for each library that the game uses, there is a dump of the library and what it imports.

## Regarding updates

For each new update, the archive will be updated, and all dumps will be up to date, but it takes some time, so after the update it takes 1-2, even 4 days, maybe more, 
because I don't just export, but also do a lot of other work, especially for each update
I have to analyze everything again, or at least some part of it.

## !

#### Remark 

The author is not responsible for the use of this archive, use solely for educational purposes.

![Logo](https://raw.githubusercontent.com/uakabibara01/uakabibara01/refs/heads/main/vn5K5O6d_400x400.jpg)


