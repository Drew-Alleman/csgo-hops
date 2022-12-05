# csgo-hops
A CSGO bunny-hop cheat compilied and obfuscated with python

## Showcase
![preview](preview.gif)

## How to compile
``` bash
python3 compile_cheats.py -D C:\Users\DrewQ\source\repos\csgo-hops\
...
   /IMPLIB:"C:\Users\DrewQ\Desktop\csgo-hops-main\Release\csgo-hops.lib" /MACHINE:X86 /SAFESEH /DLL Release\cheat.obj
  Release\dllmain.obj
  Release\_cheat.obj
  Generating code
  16 of 123 functions (13.0%) were compiled, the rest were copied from previous compilation.
    10 functions were new in current compilation
    1 functions had inline decision re-evaluated but remain unchanged
  Finished generating code
  csgo-hops.vcxproj -> C:\Users\DrewQ\Desktop\csgo-hops-main\Release\csgo-hops.dll
FinalizeBuildStatus:
  Deleting file "Release\csgo-hops.tlog\unsuccessfulbuild".
  Touching "Release\csgo-hops.tlog\csgo-hops.lastbuildstate".
Done Building Project "C:\Users\DrewQ\Desktop\csgo-hops-main\csgo-hops\csgo-hops.vcxproj" (default targets).

Done Building Project "C:\Users\DrewQ\Desktop\csgo-hops-main\csgo-hops.sln" (build target(s)).


Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:03.89
[*] SHA1: d680917df2449546b04cb15e96d2e3a9266c6d77 | C:\Users\DrewQ\Desktop\csgo-hops-main\Release\csgo-hops.dll
[*] Was compiled @ Sun Dec  4 14:57:38 2022
```

## How to inject
Use the "manual map" setting when injecting the DLL 

## How to stop
Press end to stop the cheat

## Why?
Obfuscating the variables names with random strings allows a unique file hash on every compile. Making it harder for VAC to spot.

## Where to update signatures
If the cheat is crashing please try updating the signatures in _cheat.cpp.
```c++
ptrdiff_t dwForceJump = 0x52B9C0C;
ptrdiff_t dwLocalPlayer = 0xDE8964;
ptrdiff_t m_fFlags = 0x104;
```


