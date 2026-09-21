"""Map a use case to the realtime model announced on 2026-05-07.

Usage:
    python3 examples/choose_model.py conversation
    python3 examples/choose_model.py translation
    python3 examples/choose_model.py transcription
"""
import sys
from dataclasses import dataclass

DOCS = 'https://developers.openai.com/api/docs'


@dataclass(frozen=True)
class Model:
    name: str
    does: str
    does_not: str
    guide: str


# Facts as stated in the announcement; model identifiers used on the wire
# may be versioned differently, so confirm against the API reference.
MODELS = {
    'conversation': Model(
        name='GPT-Realtime-2',
        does='live voice conversation with GPT-5-class reasoning; can take actions',
        does_not='is not the cheapest way to get a plain transcript',
        guide=f'{DOCS}/guides/websocket-mode',
    ),
    'translation': Model(
        name='GPT-Realtime-Translate',
        does='translates speech from 70+ input languages into 13 output languages',
        does_not='output languages are limited to the 13 listed; check yours',
        guide=f'{DOCS}/guides/audio',
    ),
    'transcription': Model(
        name='GPT-Realtime-Whisper',
        does='streams speech-to-text as the speaker talks',
        does_not='does not reply or reason; pair it with another model for that',
        guide=f'{DOCS}/guides/streaming-responses',
    ),
}


def pick(use_case: str) -> Model:
    return MODELS[use_case]


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] not in MODELS:
        print(f'usage: {argv[0]} ' + '|'.join(MODELS))
        return 2
    m = pick(argv[1])
    print(f'model:    {m.name}')
    print(f'does:     {m.does}')
    print(f'caveat:   {m.does_not}')
    print(f'read:     {m.guide}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
