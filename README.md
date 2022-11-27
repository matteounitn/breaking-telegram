# breaking-telegram
Simple PoC script that allows you to exploit telegram's "send with timer" feature by saving any media sent with this functionality.

## ⚠️ Disclaimer
Due to Telegram API Terms of Service, the use of this script is for PoC only.
> 1.4. It is forbidden to interfere with the basic functionality of Telegram. This includes but is not limited to: making actions on behalf of the user without the user's knowledge and consent, **preventing self-destructing content from disappearing**, preventing last seen and online statuses from being displayed correctly, tampering with the 'read' statuses of messages (e.g. implementing a 'ghost mode'), preventing typing statuses from being sent/displayed, etc.
[Telegram API Terms of Service -  Privacy & Security - 1.4](https://core.telegram.org/api/terms#1-privacy--security)

<sub><sup>but that doesn't change the fact that this is a broken API call ¯\_(ツ)_/¯ </sup></sub>

## Status

**Working** - _November 27, 2022_

## PoC

<img src="poc.gif" alt="poc" style="max-width:300px" />


## How to
### Step 0 

`git clone https://github.com/matteounitn/breaking-telegram.git`

### Step 1

- Go to https://my.telegram.org/auth?to=apps;
- Create an app(doesn't matter how do you call it);
- Get API ID and API KEYS;
- Replace them in `config.ini.example` and save it as `config.ini`

### Step 2

1. `cd breaking-telegram`
2. `python3 -m venv venv && source venv/bin/activate`
3. `pip3 install -r requirements.txt`
4. `python3 broke.py`

Now insert your number and your code. 

Eventually you will be asked for a password, if you have one set in your account.

### Step 3

Receive an image with timer (could also be a video or gif).
Check your saved messages.


## Take Home

Use secret chats. 
They're not bulletproof, but they're definitely safer.
