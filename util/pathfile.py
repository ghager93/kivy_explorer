import os

from typing import List

def filter_for_audio(files: List[str]) -> List[str]:

    AUDIO_EXTS = ['.mp3', '.mp4', '.wav', '.aac',
                  '.flac', '.mpeg']

    return [f for f in files
            if os.path.splitext(f)[1] in AUDIO_EXTS]