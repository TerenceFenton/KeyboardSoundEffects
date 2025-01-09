
from pynput import keyboard
from pydub import AudioSegment
from pydub.playback import play


# Func to play sounds from listener
def play_key_input(input):
    
    # Custom Sound effect object setup
    general_key = 'output2025-01-09 16:52:18.mp3' # Bup
    backspace_key = 'output2025-01-09 16:53:31.mp3' # Bup^
    return_key = 'output2025-01-09 16:54:26.mp3' # Shwoop

    # Conditions
    if input == keyboard.Key.backspace:
        sound = AudioSegment.from_mp3(backspace_key)
        play(sound)
    elif input == keyboard.Key.enter:
        sound = AudioSegment.from_mp3(return_key)
        play(sound)
    elif input == keyboard.Key.esc:
        return False
    else:
        sound = AudioSegment.from_mp3(general_key)
        play(sound)

# Listener setup
with keyboard.Listener(on_press=play_key_input) as listener:
    listener.join()


