"""Check the environment before opening a realtime session.

Usage:
    export OPENAI_API_KEY=...
    export REALTIME_USE_CASE=conversation   # translation | transcription
    python3 examples/env_check.py
"""
import os
import sys

from choose_model import MODELS, pick

PLACEHOLDERS = {'', 'your_key_here', 'changeme', 'xxx'}


def main() -> int:
    key = os.environ.get('OPENAI_API_KEY', '').strip()
    if key.lower() in PLACEHOLDERS:
        print('OPENAI_API_KEY is missing or a placeholder. Create one in the API Dashboard.')
        return 1
    if len(key) < 20:
        print('OPENAI_API_KEY looks too short to be a real key; double-check the export.')
        return 1

    use_case = os.environ.get('REALTIME_USE_CASE', 'conversation').strip().lower()
    try:
        model = pick(use_case)
    except KeyError:
        print(f'Unknown REALTIME_USE_CASE={use_case!r}; expected one of {sorted(MODELS)}')
        return 1

    # Never print the key itself, only that it exists.
    print('OPENAI_API_KEY: present')
    print(f'use case: {use_case}')
    print(f'model: {model.name}')
    print(f'next guide: {model.guide}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
