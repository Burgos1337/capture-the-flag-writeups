# Left Foot Two Stomps writeup

After executing the script (check the `rsa_decode.py`) we get this string:

![cr(1)](https://user-images.githubusercontent.com/57829161/79130299-6bd39a80-7daf-11ea-870c-ca3147da85a4.jpg)

So we have got the string encoded with vigenere cipher with by the key = `visionary`:

![cr(3)](https://user-images.githubusercontent.com/57829161/79130311-6ece8b00-7daf-11ea-93de-c44b039868a5.jpg)

Now it's time to decipher the base64:

![cr(2)](https://user-images.githubusercontent.com/57829161/79130320-71c97b80-7daf-11ea-8b99-720a60b8e8b6.jpg)

And again we have a hint: now we need to decode the ROT cipher by bruteforcing the key:

![cr(4)](https://user-images.githubusercontent.com/57829161/79130330-74c46c00-7daf-11ea-9852-cd9425ec00d6.jpg)

![cr(5)](https://user-images.githubusercontent.com/57829161/79130333-77bf5c80-7daf-11ea-94f1-e624dd332605.jpg)

Flag: DawgCTF{Lo0k_@t_M3_1_d0_Cr4p7o}
