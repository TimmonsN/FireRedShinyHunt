import pyautogui
from PIL import ImageGrab
import time


shiny = False

def read_file():
    with open("counter.txt", 'r') as file:
        return int(file.read())

def write_to_file(z):
    with open("counter.txt", 'w') as file:
        file.write(str(z))

def countDown():
    for i in range(10):
        print("T minus " + str(10- i) + " seconds")
        time.sleep(1)
        
def capture_screen():
    # Capture the screen
    screenshot = ImageGrab.grab()
    return screenshot

def openSummary():
    pyautogui.keyDown('1')

    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')
    time.sleep(2.5)

    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')
    time.sleep(2.5)

    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')
    time.sleep(2.5)

    # Simulate pressing 'x' four times
    pyautogui.keyDown('x')
    time.sleep(0.1)
    pyautogui.keyUp('x')
    time.sleep(2.5)

    pyautogui.keyDown('x')
    time.sleep(0.1)
    pyautogui.keyUp('x')
    time.sleep(2.5)

    pyautogui.keyDown('x')
    time.sleep(0.1)
    pyautogui.keyUp('x')
    time.sleep(2.5)

    pyautogui.keyDown('x')
    time.sleep(0.1)
    pyautogui.keyUp('x')
    time.sleep(3.5)

    # Simulate pressing 'q'
    pyautogui.keyDown('q')
    time.sleep(1)
    pyautogui.keyUp('q')
    time.sleep(1)

    # Simulate pressing 'a' three times
    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')
    time.sleep(1)

    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')
    time.sleep(1)

    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')
    time.sleep(3)

    pyautogui.keyUp('1')

def save_screenshot():
    screenshot_filename = "shiny_capture.png"
    screen.save(screenshot_filename)
    print(f"Screenshot saved as {screenshot_filename}")


z = read_file()


countDown()
while not shiny:
    #get screen
    



    openSummary()

    screen = capture_screen()

    if screen is not None:

        x, y = 631, 361

        pixel_color = screen.getpixel((x, y))

        #rgb(240,202,45) g > 200
        #shiny_color = (240,202,45)
        g_bound = 150

        if pixel_color[1] > g_bound:
            print("Shiny Pokémon detected!" + str(pixel_color))
            save_screenshot()
            shiny = True
        else:
            print("not yet" + str(pixel_color))
            pyautogui.keyDown('4')
            pyautogui.keyUp('4')
            write_to_file(z)
            z += 1

    time.sleep(1)
