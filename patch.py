# patch.py - Place in `HatinTime\Binaries\Win64\` and run to patch Hor+ into the game.

from os import remove, rename
from os.path import exists, join
from shutil import copy

def mod_file(file):
    with open(file, 'r+b') as f:
        
        # Loop for bytes
        while True:
            buff = f.read(4)

            # EOF
            if buff == b'':
                return False

            # Found modded bytes
            if buff == b'\x61\x0B\x66\x3B':
                print('File is already modded!', buff)
                return False 

            # Found our Vert- bytes
            if buff == b'\x61\x0B\x36\x3B':
                print('Found bytes', buff)
                break 

        # Write new bytes
        f.seek(-4, 1)
        f.write(b'\x61\x0B\x66\x3B')
        return True
        

if __name__ == "__main__":
    if not exists('HatinTimeGame.exe'):
        print('`HatinTimeGame.exe` not found. Are you sure you are running patch.py in `HatinTime\Binaries\Win64\`?')
        print('If the main exe is missing, launch the game on steam and steam will redownload the exe.')
        exit(1)

    # Clean up old files
    if exists('HatinTimeGame - Orig.exe'): rename('HatinTimeGame - Orig.exe', 'HatinTimeGame - Orig.exe.old')
    if exists('HatinTimeGame - Mod.exe'): rename('HatinTimeGame - Mod.exe', 'HatinTimeGame - Mod.exe.old')
    
    # Backup original and create a file to modify
    copy('HatinTimeGame.exe', 'HatinTimeGame - Orig.exe')
    copy('HatinTimeGame.exe', 'HatinTimeGame - Mod.exe')

    # Try to mod file
    if not mod_file('HatinTimeGame - Mod.exe'):
        print("Mod failed, reverting.")

        # Clean up mess
        remove('HatinTimeGame - Orig.exe')
        remove('HatinTimeGame - Mod.exe')

        # Return old files
        if exists('HatinTimeGame - Orig.exe.old'): rename('HatinTimeGame - Orig.exe.old', 'HatinTimeGame - Orig.exe')
        if exists('HatinTimeGame - Mod.exe.old'): rename('HatinTimeGame - Mod.exe.old', 'HatinTimeGame - Mod.exe')

        exit(1)

    # Apply the new mod
    print("Setting mod as default exe")
    remove('HatinTimeGame.exe')
    copy('HatinTimeGame - Mod.exe', 'HatinTimeGame.exe')
    print('Done.')
