from concurrent.futures import ThreadPoolExecutor
import pygame
from pynput import keyboard

pygame.mixer.init()

sound_files = ["output_bop.wav", "output_bUp.wav", "output_shwoop.wav"]
sounds = [pygame.mixer.Sound(i) for i in sound_files]

def return_key_sound(i):
    global sounds
    sound = sounds[i]
    sound.play()

def task_executor(input):
    i = None
    if input == keyboard.Key.enter:
        i = 2
    elif input == keyboard.Key.backspace:
        i = 1
    elif input == keyboard.Key.esc:
        return False
    else:
        i = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(return_key_sound, i)

with keyboard.Listener(on_press=task_executor) as listener:
    listener.join()
