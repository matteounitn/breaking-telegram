# breaking-telegram
PoC script that allows you to exploit telegram's "send with timer" feature, automatically saving any media sent with this functionality.

## PoC

<img src="poc.gif" alt="poc" style="max-width:300px" />


## How to
### Step 0 

`git clone https://github.com/matteounitn/broking-telegram.git`

### Step 1

- Go to https://my.telegram.org/auth?to=apps;
- Create an app(doesn't matter how do you call it);
- Get API ID and API KEYS;
- Replace them in `config.ini.example` and save it as `config.ini`

### Step 2

1. `cd broking-telegram`
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
They still are not bulletproof, but they are safer.
