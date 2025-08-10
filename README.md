## !

#### Remark 

The author is not responsible for the use of this archive, use it exclusively for educational purposes or for your own analysis, 
do not use dumps/code analysis or decompile code to use it to create prohibited software, 
the author is against this and does not support it, and the main purpose is analysis and is of no more interest. 
Thank you for your understanding: ヽ(*￣▽￣*)ノ

# SCP-SL-Reverse-Engineering

This repository is the ARCHIVE of the SCP:Secret-Laboratory game, created using reverse engineering.
It contains a dump of all the game libraries that each of them imports, as well as separate folders with decompilations into C-like code and ASM code: 4 main libraries, 
as well as the C# server code (SCP Secret Laboratory Dedicated Server):


SCPSL.exe == 140000000.SCPSL.exe


SC-AC.dll == 180000000.SL-AC.dll


UnityPlayer.dll == 7ffda05f0000.UnityPlayer.dll


GameAssembly.dll == 7ffd95060000.GameAssembly.dll

Other imported libraries do not require decompilation etc.: they are system ones.
You can also use anti-obfuscation programs to read C++ code etc.
I chose this option, the following programs were used:

[IDA](https://hex-rays.com/ida-free)

[Cutter](https://github.com/rizinorg/cutter)

[Ghidra](https://github.com/NationalSecurityAgency/ghidra)

[dnSpy](https://github.com/dnSpy/dnSpy)

Dump program 1:PE-sieve: scans the given process, recognizes and removes various potentially harmful implants.

Dump program 2: [x64dbg](https://x64dbg.com/) (in this case you need to use x32dbg + plugin ScylaHide )

A script file for Ghidra in Python will also be added to store all functions in C-like code and ASM code. As the script name suggests,
scriptC.py is for C-like code and scriptASM.py is for your own purposes.

Folder with a file named: Dump-Files
It collects everything that SCPSL imports, so you can use these dumps in other programs as you see fit ○( ＾皿＾)っ Hehe…

## Additionally

Also in the text file SC-AN.dll.txt there is my own analysis of the anti-cheat, but it is not complete, since there are many functions,
but the main and most important part of the anti-cheat is written there, since the largest functions were analyzed.
In the future, over time, when I analyze everything, I will write a reference about each of the libraries, 
what it does, what it contains, etc., but for now, only about SC-AC.dll :( .

## Files

SCPSL_Dump.rar == Contains all dump and decompilation files.

Dump-Files.rar == Contains only library dumps and what they import in a separate text file.

Decompiled LibrariesC.rar == Contains only folders with decompiled code of all 4 libraries into C-like code.

Decompiled LibrariesASM.rar == Contains decompiled code of all 4 libraries in ASM code.

Assembly-CSharp.dll.rar == Decompiled Server Code. Basic Logic

Assembly-CSharp-firstpass.dll.rar == Decompiled Server Code 2 

CommandSystem.Core.dll.rar == Server Code Secondary (Command logic)

BouncyCastle.Cryptography.dll.rar == Cryptography

## Authors

- [@uakabibara01](https://github.com/uakabibara01)


## Using

Download WinRar to unpack the archive.

We download the latest release there to choose from, unpack the files and get everything we need, then it's up to you:
There are 2 folders, in one Decompiled LibrariesC there is C-like code, and in Decompiled LibrariesASM there is ASM code for each of the 4 libraries,
where the function files are located.
and in Dump-Files there are folders for each library used by the game, there is a dump of the library and what it imports,
in other RAR files there is the decompiled server code and several of its dlls if you want to know how the server works or rewrite the server logic then download it to suit your task
but I advise you to download [dnSpy](https://github.com/dnSpy/dnSpy)

If you download the RAR file with the decompiled server code, 
please note that it is optimized for visual studio 2022 (.sln) 4.8 .NET Framework VS 2019/2022

## Regarding updates

For each new update, the archive will be updated, and all dumps will be up to date, but it takes some time, so after the update it takes 1-2, even 4 days, maybe more, 
because I don't just export, but also do a lot of other work, especially for each update
I have to analyze everything again, or at least some part of it.


![Logo](https://raw.githubusercontent.com/uakabibara01/uakabibara01/refs/heads/main/vn5K5O6d_400x400.jpg)


