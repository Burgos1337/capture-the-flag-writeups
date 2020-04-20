```
burgos1337@burgos1337-VirtualBox:~/Desktop$ ssh ctf@sigknock.wpictf.xyz
Password: 
~ $ ls
~ $ cd ../../
/ $ ls
bin    dev    etc    home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
/ $ /usr/bin/irqknock &
/ $ for i in 2 3 11 13 17; do pkill -$i /usr/bin/irqknock;done
Got signal 2
State advanced to 1
Got signal 2
State advanced to 1
Got signal 3
State advanced to 2
Got signal 3
State advanced to 2
Got signal 11
State advanced to 3
Got signal 11
State advanced to 3
Got signal 13
State advanced to 4
Got signal 13
State advanced to 4
Got signal 17
State advanced to 5
WPI{1RQM@St3R}
Got signal 17
State advanced to 5
WPI{1RQM@St3R}
[1]+  Done(1)                    /usr/bin/irqknock
/ $ ^C
/ $ exit
Connection to sigknock.wpictf.xyz closed.
burgos1337@burgos1337-VirtualBox:~/Desktop$
```