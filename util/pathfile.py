import os

from typing import List


AUDIO_EXTS = ['.mp3', '.mp4', '.wav', '.aac',
              '.flac', '.mpeg']


def audio_paths_in_dir(dir: str) -> List[str]:
    return [os.path.join(dir, f) for f in filter_for_audio(os.listdir(dir))]


def filter_for_audio(files: List[str]) -> List[str]:
    return [f for f in files if is_audio(f)]


def is_audio(file: str):
    return os.path.splitext(file)[1] in AUDIO_EXTS