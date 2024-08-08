import pyautogui
import time
import argparse

def autoclicker(delay, duration):
    """
    Un autoclicker simple.
    Args:
        delay: Délai entre les clics en secondes.
        duration: Durée totale pour laquelle l'autoclicker fonctionnera.
    """
    end_time = time.time() + duration
    while time.time() < end_time:
        pyautogui.click()
        time.sleep(delay)

parser = argparse.ArgumentParser(description='Autoclicker')
parser.add_argument('delay', type=float, help='Délai entre les clics en secondes.')
parser.add_argument('duration', type=int, help='Durée totale pour laquelle l\'autoclicker fonctionnera.')
args = parser.parse_args()

autoclicker(args.delay, args.duration)
