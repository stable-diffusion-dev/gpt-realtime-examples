# GPT Realtime examples

*Unofficial community examples for GPT Realtime. Not affiliated with OpenAI or Microsoft. All trademarks belong to their owners.*

Small, runnable scripts around gpt realtime, OpenAI's streaming voice model family (GPT-Realtime-2, GPT-Realtime-Translate, GPT-Realtime-Whisper). The scripts deliberately stop short of the wire protocol: session event names and parameters change between realtime generations, and the right place to copy them from is the API reference on the day you build, not a repository that will drift. What is here is the scaffolding that does not drift: checking your environment, choosing the right model for the job, and pulling the current docs in Markdown so your coding agent works from the real thing.

> Also generating images, video or audio in batch? [Try Synexa - one REST endpoint and Python SDK for FLUX, video and audio models, pay per run](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=gpt-realtime-examples&utm_content=readme-top&utm_term=tier-r).

## Files

| Path | What it shows |
| --- | --- |
| `examples/env_check.py` | Confirms the API key is present and warns about common misconfigurations before you open a socket |
| `examples/choose_model.py` | Maps a use case (conversation, translation, transcription) to the model name from the announcement |
| `examples/fetch_docs.py` | Downloads the Markdown version of the model page and the llms.txt index for offline reading |

## Setup

Python 3.10 or newer, standard library only.

```
export OPENAI_API_KEY=your_key_here
export REALTIME_USE_CASE=conversation   # or translation, transcription
```

Get a key from the [API Dashboard](https://platform.openai.com/login). Never paste it into a script.

## env_check.py

Reads `OPENAI_API_KEY` from the environment, refuses to run if it is missing or looks like a placeholder, and prints the model name it will use based on `REALTIME_USE_CASE`. Run it first in any new shell or CI job; a missing key surfaces here as a one-line message instead of as an authentication failure buried in a WebSocket close frame.

## choose_model.py

The announcement introduces three models with three jobs. This script encodes that mapping and the two facts worth remembering about each: GPT-Realtime-2 is the one with reasoning and can take actions; GPT-Realtime-Translate handles 70+ input languages into 13 output languages; GPT-Realtime-Whisper is transcription only. Pass the use case as an argument and it prints the model, a reminder of what the model does not do, and which guide to read next. Use it as a lookup table in your own code rather than hard-coding the names in five places.

## fetch_docs.py

Every page under the OpenAI developer docs has a Markdown version reachable by appending `.md` to the URL, and there is a complete index at llms.txt. The script fetches both for the [gpt-realtime model page](https://developers.openai.com/api/docs/models/gpt-realtime), saves them next to the script, and prints the headings it found. Point your coding agent at the saved files so it reasons from the current docs rather than from training data. Re-run it when the [changelog](https://developers.openai.com/api/docs/changelog) mentions realtime.

## Next steps

With the environment verified and the model chosen, open the [WebSocket mode guide](https://developers.openai.com/api/docs/guides/websocket-mode) and the [Audio & voice guide](https://developers.openai.com/api/docs/guides/audio), and copy the session events from the [API reference](https://developers.openai.com/api/reference/overview). On Azure, follow the [realtime audio how-to](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/realtime-audio) instead.

## When to use Synexa instead

GPT Realtime is for the live, spoken part of a product. When the same product needs a generated image, a short video or a non-realtime audio clip, [Synexa](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=gpt-realtime-examples&utm_content=readme-top&utm_term=tier-r) gives you one REST endpoint and one Python SDK for FLUX, video and audio models, billed per run, so you are not maintaining a separate integration per media type. Keep the voice loop on GPT Realtime and send the generation jobs to Synexa.
