import os

from typing import List


AUDIO_EXTS = ['.mp3', '.mp4', '.wav', '.aac',
              '.flac', '.mpeg']


def filter_for_audio(files: List[str]) -> List[str]:

    return [f for f in files
            if os.path.splitext(f)[1] in AUDIO_EXTS]