# Instagram Spammer Bot
This script was developed to spam comments with usernames on that boring giveaways that often happen on Instagram platform. (i.e.: *Comment the name of a friend to compete a product*).

It uses mainly `pyautogui` to simulate a person refreshing, clicking and typing in the comment section, in this way, the instagram won't detect that's a bot and you can be 24/7 spawning usernames or whatever you're up to.

## Instructions
### Dependencies
This script was made using `python3`, in order to install all dependencies, please run:
```bashrc
pip install -r requirements.txt
```

### System dependencies
Appears that `pyautogui` module cannot support Wayland yet, so i strongly recommend to use this script on a unix/linux env with **XORG** support.

### How to use
First, you will need to generate a list with all the usernames you want to spawn. It only needs to be on `.csv` format, stay inside the `./assets` folder and have a column named `username`. To generate mines, i had used a plugin called [*Helper Tools for Instagram*](https://chrome.google.com/webstore/detail/helper-tools-for-instagra/hcdbfckhdcpepllecbkaaojfgipnpbpb) (for Chrome).

To use this script:
1. Open a Instagram post page that you will spam, on your favorite browser (tested on `chrome` and `chromium`) and put aside.
2. Open the terminal on the project folder and run `python3 spam.py`.
3. The script will wait a key to be pressed, when waiting, you will move the mouse to the *click* position (where you can type, i.e.: comment section) **without clicking** and press `Enter` key on the terminal window.
4. The script will read the `.csv` files and start to spam. (PS: Recommended to use this script on a VM, because you can't use the computer while the script is running!).

#### Considerations
+ The script uses a random interval number generation on the range [TIME_TO_SLEEP - 5, TIME_TO_SLEEP + 5), where `TIME_TO_SLEEP` it's a global variable inside `spam.py` that you can tweak if needed.
+ The script always does: Get username, type username and hit `Enter` key, hit `f5` key to reload the page. This is needed because instagram normally blocks text input on comment section after some comments.

## Authorship
Script developed by FelipeCRamos, with MIT License, without using **anything** from Instagram API.
Not optimized at all, made in 15 minutes just to place a whole lot of comments on a giveaway page.
