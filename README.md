# auto_accept_league
A simple python script that automatically accepts a match in league of legends.

It works by trying to find anything in your screen that is very similar to the accept button icon. When it does find it, it automatically clicks the button.

Note that you may need to update the icon image, especially if you're playing league in a different language than PT-BR.

# Requirements

```
pip install pyautogui
pip install Pillow
pip install opencv-python
```

or

```
pip install -r requirements.txt
```

# How to use
1. Make sure the `accept_icon.png` matches whatever accept button you see when playing league.
2. Run the `auto_accept.py` script.
