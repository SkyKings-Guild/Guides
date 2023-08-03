```yaml {metadata}
title: Securing Your Minecraft Account
description: |
  Learn how to secure your minecraft account.
category: Other
author: plun1331
tags:
  - Security
```

There are a variety of measures you can take to secure your account, as well as a number of ways people can steal it.  
This guide runs through some of these security measures and how to respond to potentially compromised account.

Most of these measures are fairly obvious, such as using secure passwords, enabling 2FA, or using other accounts
security settings that Microsoft provides, however this only covers a very small number of ways one can gain access to
your Minecraft account.

## Mods

Minecraft mods are a very common source of account takeovers. They not only allow someone to find and use your Minecraft
Session ID, which is a long code that allows you to login to Minecraft server, but can also grant access to your
computer, including passwords and stored files.  
Only download mods you trust, from trusted sources.

## Phishing

Phishing is a technique that scammers use to get you to input sensitive information on a website. 
Typically, this website doesn't belong to who you think it does, and is instead run by the scammer.

One of the safest ways to avoid being phished is to not click any links you get sent, however this isn't a very practical method.

To make sure a site belongs to who you think it does, you should try the following:
- **Make sure the domain name is correct.** `hyplxel.net` is not the same as `hypixel.net`. Even domains like `store-hypixel.net` are malicious.
- **Make sure the site is secure (uses HTTPS).** There should be a lock on the left of the URL bar if it does. 
  If the site is not secure, you may not actually be on the correct site, even if the domain is correct.
- **Use common sense.** Question yourself, "Would they actually do this?" or "Does this make sense?" if the anwer is no, it is most likely a scam.

### OAuth2

OAuth2 is a system that allows an application to gain limited access to your account, without exposing any personal
information (unless you give it access).  
Authorizing an untrusted app can allow the app
to [generate its own Minecraft session ID](https://wiki.vg/Microsoft_Authentication_Scheme), and thus allow someone
access to your Minecraft account. Apps that do this will commonly have an "unverified" notice underneath the "Let this
app access your info?" text, and will request permission to "Access your Xbox Live profile information and associated
data, and sign you in to its services".

![Dangerous Oauth2 Prompt](/images/security/dangerous-oauth2.png "Dangerous Oauth2 Prompt")

**Even if you are on the real Microsoft website, this can still compromise your account.** Only authorize apps you trust.

## One-time Passwords

A one-time password (OTP) allows someone to gain access to an account through a code, typically delivered through email. 
This is typically used for password resets and, in some cases, logging into accounts.
Scammers will usually get you to provide them your username and account email, which they will use to send you an OTP.

Here's an example of what that email looks like:

![Microsoft's OTP email](/images/security/msotp.png "Microsoft's OTP email")

The worst part about this? There is no indication whatsoever that the code you were sent can be used to log into your Microsoft account.

Regardless, do not share ***any*** codes you recieve in your email with anyone else. Especially if it tells you not to.

## Reporting a Phishing Site

One of the easiest ways to report a phishing site is [phish.report](https://phish.report/). 
Just put in the site URL and report it to the various companies it recommends.

## Securing your Account

In the event that your account is compromised, we recommend the following steps:

* Reset your password at [account.live.com/password/change](https://account.live.com/password/change). This will log out
  anything logged into your Microsoft account.
* Unauthorize all apps at [microsoft.com/consent](https://microsoft.com/consent). This will prevent malicious apps from
  obtaining new session IDs.
* Visit [account.xbox.com/Settings](https://account.xbox.com/Settings?activetab=main:privilegetab) and block "You can
  join multiplayer games". At the moment there does not seem to be a way to force reset your Minecraft session ID, and
  disabling this setting will prevent it from being used. Leave this disabled for at least 24 hours to allow the session
  ID to expire.

You can also report ratting attempts to us at [skykings.net/forms/report](https://skykings.net/forms/report).
