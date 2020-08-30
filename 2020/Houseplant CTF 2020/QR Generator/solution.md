# QR Generator writeup

Taking the hint about `backticks` into the account I had got an idea of performing RCE in this challenge. While exploring the task 
functionality it becomes obvious that QR code return us only the first symbol of our string:

![Снимок экрана (632)](https://user-images.githubusercontent.com/57829161/80568779-4aee8480-8a00-11ea-97c1-54991f9d624c.jpg)

In this case after scanning the QR we will get `q` letter... so why not to use some well-known bash commands to find out anything 
interesting there:

![Снимок экрана (633)](https://user-images.githubusercontent.com/57829161/80568786-4e820b80-8a00-11ea-883c-edceeda016af.jpg)

Now we get the `R` letter, that can't help but suggest an idea to retrieve the whole flag symbol by symbol, so I have made the 
python script to automate this process...

After launching the `get_flag.py` we finally get the flag: `rtcp{fl4gz_1n_qr_c0d3s???_b1c3fea}`
