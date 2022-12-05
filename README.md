# csgo-hops
A CSGO bunny-hop cheat compilied and obfuscated via a python script

## Why?
Obfuscating the variables names with random strings allows a unique file hash on every compile. Making it harder for VAC to spot.

## Showcase
![preview](preview.gif)

## Features
This is just a bunny hop cheat. Press END to stop the cheat.

## How to compile
``` bash
python3 compile_cheats.py -D C:\Users\DrewQ\source\repos\csgo-hops\

  9 of 10 functions (90.0%) were compiled, the rest were copied from previous compilation.
    7 functions were new in current compilation
    1 functions had inline decision re-evaluated but remain unchanged
  Finished generating code
  csgo-hops.vcxproj -> C:\Users\DrewQ\source\repos\csgo-hops\x64\Release\csgo-hops.dll
FinalizeBuildStatus:
  Deleting file "x64\Release\csgo-hops.tlog\unsuccessfulbuild".
  Touching "x64\Release\csgo-hops.tlog\csgo-hops.lastbuildstate".
Done Building Project "C:\Users\DrewQ\source\repos\csgo-hops\csgo-hops\csgo-hops.vcxproj" (default targets).

Done Building Project "C:\Users\DrewQ\source\repos\csgo-hops\csgo-hops.sln" (default targets).

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:02.72
[*] SHA1: 8d79c80a02aba329a266829e9380fe03364cce1c | C:\Users\DrewQ\source\repos\csgo-hops\\x64\Release\csgo-hops.dll
[*] Was compiled @ Sat Dec  3 11:03:07 2022
```

## How to inject
Use the "manual map" setting when injecting the DLL 
