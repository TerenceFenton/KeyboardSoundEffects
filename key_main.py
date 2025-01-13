# Libraries
from concurrent.futures import ThreadPoolExecutor
import pygame
from pynput import keyboard
import random

# Pygame and wav file setup
pygame.mixer.init()
general_sound_files = ["output_bop.wav", "output_beep.wav", "output_bap.wav"]
return_sound_files = ["output_shwoop.wav"]
backspace_sound_files = ["output_back.wav", "output_back?.wav", "output_back!.wav"]

# List of sound types
g_sounds = [pygame.mixer.Sound(i) for i in general_sound_files]
r_sounds = [pygame.mixer.Sound(i) for i in return_sound_files]
b_sounds = [pygame.mixer.Sound(i) for i in backspace_sound_files]
mega_list = [g_sounds, b_sounds, r_sounds]

# Sound player
def return_key_sound(i):
    global mega_list
    sound_files = mega_list[i]

    if len(sound_files) > 1:
        random_number = random.randrange(0, len(sound_files))
        print(random_number)
        sound = sound_files[random_number]
    
    else:
        sound = sound_files[0]
    sound.play()

# Threadpooling Function
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

# Pynput keyboard listener
with keyboard.Listener(on_press=task_executor) as listener:
    listener.join()
