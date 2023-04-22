```yaml {metadata}
title: Securing Your Minecraft Account
description: |
    Learn how to secure your minecraft account.
category: Other
author: SkyKings
tags:
    - Security
```

There are a variety of measures you can take to secure your account, as well as a number of ways people can steal it.  
This guide runs through some of these security measures and how to respond to potentially compromised account.

Most of these measures are fairly obvious, such as using secure passwords, enabling 2FA, or using other accounts security settings that Microsoft provides, however this only covers a very small number of ways one can gain access to your Minecraft account.

Mods
----

Minecraft mods are a very common source of account takeovers. They not only allow someone to find and use your Minecraft Session ID, which is a long code that allows you to login to Minecraft server, but can also grant access to your computer, including passwords and stored files.  
Only download mods you trust, from trusted sources.

OAuth2
------

OAuth2 is a system that allows an application to gain limited access to your account, without exposing any personal information (unless you give it access).  
Authorizing an untrusted app can allow the app to [generate its own Minecraft session ID](https://wiki.vg/Microsoft_Authentication_Scheme), and thus allow someone access to your Minecraft account. Apps that do this will commonly have an "unverified" notice underneath the "Let this app access your info?" text, and will request permission to "Access your Xbox Live profile information and associated data, and sign you in to its services".

  
![Image](./images/security/dangerous-oauth2.png "Dangerous 2FA")

Only authorize apps you trust.

Securing your Account
---------------------

In the event that your account is compromised, we recommend the following steps:

*   Reset your password at [account.live.com/password/change](https://account.live.com/password/change). This will log out anything logged into your Microsoft account.
*   Unauthorize all apps at [microsoft.com/consent](https://microsoft.com/consent). This will prevent malicious apps from obtaining new session IDs.
*   Visit [account.xbox.com/Settings](https://account.xbox.com/Settings?activetab=main:privilegetab) and block "You can join multiplayer games". At the moment there does not seem to be a way to force reset your Minecraft session ID, and disabling this setting will prevent it from being used. Leave this disabled for at least 24 hours to allow the session ID to expire.

You can also report ratting attempts to us at [skykings.net/forms/report](https://skykings.net/forms/report).
