# M1 Abrams writeup

After clicking the link we are redirected to the default apache page, so to find the other pages we need to use the gobuster:

![gobuster](https://user-images.githubusercontent.com/57829161/78535842-7f9e6000-77f5-11ea-9d2c-7083769e5d82.png)

Firstly we are able to find the /cgi-bin/ directory, then we should run the gobuster again on that directory and discover the scriptlet
file located within:

![whoami](https://user-images.githubusercontent.com/57829161/78535847-82995080-77f5-11ea-9036-fb7b122f6b25.png)

This appears to be a bash script that just runs whoami. Since this is bash, let's try exploiting the shellshock using BurpSuite: 

(cgi-bin + ctf - user input = shellshock)

![burp2](https://user-images.githubusercontent.com/57829161/78535856-84fbaa80-77f5-11ea-8772-c7dc7c7c50aa.png)

To test for the shellshock, we can replace the user-agent string with `() { :;}; echo; echo vulnerable`. If the response from the server 
contains the word `vulnerable`, we have a hit:

![burp3](https://user-images.githubusercontent.com/57829161/78535865-888f3180-77f5-11ea-9828-0c158e321ec4.png)

My home network wouldn't allow me to catch a reverse shell, but BurpSuite is all the shell we need at this point. After some poking
around, I have found something interesting at /root directory (full path for ls was required):

![binls](https://user-images.githubusercontent.com/57829161/78535873-8af18b80-77f5-11ea-909d-29bce47715d3.png)

![bincat](https://user-images.githubusercontent.com/57829161/78535884-8dec7c00-77f5-11ea-8ec7-59c694451d9b.png)

So we should just decode that from hex:

![cyberchef](https://user-images.githubusercontent.com/57829161/78535887-90e76c80-77f5-11ea-9a37-6996a4705539.png)

Flag: auctf{$h311_Sh0K_m3_z@ddY}
