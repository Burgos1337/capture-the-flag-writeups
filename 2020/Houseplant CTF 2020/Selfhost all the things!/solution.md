# Selfhost all the things! writeup

In this challenge we’re prompt with a link...

![Снимок экрана (612)](https://user-images.githubusercontent.com/57829161/80566240-322fa000-89fb-11ea-9135-3b588a516f70.png)

...that redirects us to a page like that:

![Снимок экрана (613)](https://user-images.githubusercontent.com/57829161/80566250-36f45400-89fb-11ea-9b86-331fea7cf8f0.png)

I always try to mess around the requests in BurpSuite while solving such kind of tasks, so why not to check that one and to play with
parameters a bit:

![Снимок экрана (614)](https://user-images.githubusercontent.com/57829161/80566256-39ef4480-89fb-11ea-9195-52f1d1cd08a4.png)

Let's try to login with `flag` GET parameter value:

![Снимок экрана (615)](https://user-images.githubusercontent.com/57829161/80566264-41165280-89fb-11ea-95d0-d6ff2075e5c1.png)

So we get `302` status code with redirection to the flag:

![Снимок экрана (616)](https://user-images.githubusercontent.com/57829161/80566271-44a9d980-89fb-11ea-91e9-ac6616947a2d.png)

Flag: `rtcp{rtcp-*is-s/ort-of-se1fh0st3d}`
