import pyautogui
import time

# Warte ein paar Sekunden, um das Zielprogramm zu öffnen
time.sleep(5)

# Pfad zu deinem Bild
button_image_path = '../buttons/test.PNG'

# Suche das Bild auf dem Bildschirm
try:
    button_location = pyautogui.locateCenterOnScreen(button_image_path)
    if button_location is not None:
        # Bewege die Maus zur Position des Bildes und klicke
        pyautogui.moveTo(button_location)
        pyautogui.click()
    else:
        print("Knopf nicht gefunden.")
except FileNotFoundError:
    print(f"Bilddatei nicht gefunden: {button_image_path}")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
