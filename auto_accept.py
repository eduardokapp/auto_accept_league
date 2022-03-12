import pyautogui

# A simple click definition
def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def watch_for_match():
    # try to find the accept_icon.png on screen. the 'confidence' parameter uses opencv-python
    coords = pyautogui.locateOnScreen('accept_icon.png', confidence=0.7)
    if coords is None:
        return False
    # if we have any coordinates, then we can just click
    click(coords.left, coords.top)
    return True

def auto_accept():
    accepted = False
    # Wait until a match is accepted
    while(not accepted):
        accepted = watch_for_match()

    print("Match found and accepted!")

auto_accept()