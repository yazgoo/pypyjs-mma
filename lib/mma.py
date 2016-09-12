class Main:
    def __init__(self):
        self.MMAdir="/tmp"
        self.platform="Linux"
        self.ffi = self.lib = []
print("test")
import os
def list_dir(d):
    for f in os.listdir(d):
        full_path = d + "/" + f
        if(f != '.' and f != '..' and os.path.isdir(full_path)):
            list_dir(full_path)
        else:
            print(full_path)
list_dir(".")
f = open('in.mma','w')
f.write("""
// I've Got You Under My Skin

Tempo 105
Groove Metronome2-4

	z * 2

Begin Solo
	Voice Piano2
	Octave 4
	Harmony 3above
	Articulate 90
	Accent 1 20
 	Volume f
End

Keysig 3b


Groove Rhumba
Alltracks SeqRnd Off
Bass-Sus Sequence -		// disable the strings

Cresc pp mf 4

// 4 bar intro

1 	Eb		{4.g;8f;2e;}
2 	Ab      {4.a;8g;2f;}
3 	Gm7     {1g;}
4 	Bb7     {2b;}

Delete Solo

Repeat
Groove Rhumba

Cresc pp mf 16

5 	Fm7
6 	Bb7
7 	EbM7
8 	Eb6 /  /  Eb
9 	Fm7
10 	Bb7
11 	EbM7
12 	Eb6 /  /  Eb

Groove RhumbaSus

13 	Fm7
14 	Bb7
15 	EbM7 /  Eb6
16 	/  /  Eb Gm
17 	Fm7
18 	/  /  Bb7
19 	EbM7
20 	Eb6

Groove Rhumba
Decresc mf mp 8

21 	Fm7
22 	Bb7
23 	EbM7
24 	Eb6
25 	Abm6
26 	/  /  Bb7
27 	D /  EbM7
28 	Eb+ /  Eb6
29 	Dm

Groove RhumbaSus
Cresc mf 8

30 	/  G7
31 	Cdim /  C
32 	C
33 	Ab6
34 	Abm7 /  Bb7
35 	EbM7
36 	Eb6

Groove Rhumba1

37 	Fm7
38 	Bb7
39 	Eb
40 	Eb7
41 	Ab6
42 	Abm6
43 	Eb

Groove RhumbaTriple34

44 	Bb7

Groove $_LastGroove
Volume mp

45 	Cm
46 	Ab Bb7
47 	Eb
48 	/  /  F#dim

Volume mf

49 	Fm7
50 	Bb7

Volume mp

51 	Eb
52 	Bb+ /  Eb

Cresc mf 4

53 	Ab
54 	Abm6
55 	Eb
56 	Bbm /  C7 z

Cut -1
Groove Rhumba

57 	Fm7
58 	Bb7b9

Repeatending

59 	Eb
60 	/
61 	/  z  /  Bb7

Repeatend

Groove RhumbaEnd1
Decresc ppp 3


62 	Eb
Seq 1
63 	/
64 	/ z!""")
f.close()
import sys
sys.argv = ["", "in.mma"]
main = Main()
sys.modules['__main__'] = main
sys.modules['_pwdgrp_cffi'] = main
print("test2")
import MMA.main
list_dir(".")
