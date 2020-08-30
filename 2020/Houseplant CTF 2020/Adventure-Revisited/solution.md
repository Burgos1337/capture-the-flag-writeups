# Adventure-Revisited writeup

Firstly we are given the 7zip archive - let's download this one and explore the corrupted data provided in the archive:

![Снимок экрана (634)](https://user-images.githubusercontent.com/57829161/80571430-48daf480-8a05-11ea-8d99-320f75de441e.jpg)

That for sure looks like base64 encoded data, so I decoded that from base64 in cyberchef and then saved as PNG:

![Снимок экрана (635)](https://user-images.githubusercontent.com/57829161/80571437-4d9fa880-8a05-11ea-8e0b-f28db8124854.jpg)

So we got this PNG image from cyberchef:

![Снимок экрана (636)](https://user-images.githubusercontent.com/57829161/80571445-50020280-8a05-11ea-9ec4-8767ee179747.jpg)

Next, I invited Jade to a private server so that I could test it. Then I noticed that the image told something about an eval function. 
So I thought I would test if an eval existed there:

![Снимок экрана (637)](https://user-images.githubusercontent.com/57829161/80571452-52645c80-8a05-11ea-8bc9-e2c9df4dcda5.jpg)

So the next thing we could perform in that chat was to search for the locals:

![Снимок экрана (638)](https://user-images.githubusercontent.com/57829161/80571471-598b6a80-8a05-11ea-8e4b-8a9eedb96016.jpg)

I wanted to see what the redacted text was, so I tried to return the variables:

![Снимок экрана (639)](https://user-images.githubusercontent.com/57829161/80571476-5c865b00-8a05-11ea-80e9-79df2915357e.jpg)

The final step was to return the `flag` variable:

![Снимок экрана (640)](https://user-images.githubusercontent.com/57829161/80571484-5f814b80-8a05-11ea-82f9-5bcc74a86350.jpg)

Flag: `rtcp{1tz_n0t_4_bug_1ts_a_fe4tur3}`
