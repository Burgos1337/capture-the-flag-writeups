# dorsia2 writeup

After accessing the task application we immediately get the hint from the video about the directory traversal attack.

From that point the task becomes kinda guessing - after trying several options we find out that way to cat `etc/passwd`:

![dr(1)](https://user-images.githubusercontent.com/57829161/79734024-b77dcb00-82fe-11ea-848c-ab7aa107c05d.png)

All remains is to cat `flag.txt` in the same way:

![dr(flag)](https://user-images.githubusercontent.com/57829161/79734045-bea4d900-82fe-11ea-8f66-9f343ffd992a.png)

Flag: WPI{1_H4VE_2_return_SOME_VIDE0TAP3S}
