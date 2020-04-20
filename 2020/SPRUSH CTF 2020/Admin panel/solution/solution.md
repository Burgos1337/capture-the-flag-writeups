# Admin panel writeup

Our first action on that server is obviously to explore the source code:

![adm(0)](https://user-images.githubusercontent.com/57829161/78890968-44a76100-7a6f-11ea-8188-384f21dfc689.png)

![adm(1)](https://user-images.githubusercontent.com/57829161/78890982-48d37e80-7a6f-11ea-8b72-1f7a92057a4c.png)

Here we have vulnerable ```unserialize``` function, so we need the basic payload to login as an admin:

![adm(2)](https://user-images.githubusercontent.com/57829161/78890990-4b35d880-7a6f-11ea-99ad-213676e77939.png)

![adm(flag)](https://user-images.githubusercontent.com/57829161/78890996-4cff9c00-7a6f-11ea-9cb2-55e0fa895f14.png)

Flag: SPR{DO_N0T_TRUST_PHP_3QU4T1ON_1T_1S_WEAK}
