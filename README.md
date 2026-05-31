# Playground

A personal sandbox for experiments, prototypes, and small projects. Each subfolder is a self-contained project with its own dependencies and setup.

**Remote:** [github.com/KamranRizvi265/Playground](https://github.com/KamranRizvi265/Playground)

---

## Projects

| Project | Description |
|---------|-------------|
| [**Jarvis**](Jarvis/) | Voice assistant that listens for commands, speaks responses, and can search Wikipedia or open sites in your browser |

---

## Jarvis

A minimal desktop voice assistant inspired by Iron Man’s JARVIS. It greets you by time of day, listens through your microphone, and handles a small set of spoken commands.

### Features

- Text-to-speech greetings (morning / afternoon / evening)
- Speech-to-text via Google Speech Recognition (`en-IN`)
- Wikipedia summaries (say “search” plus a topic)
- Open common sites: YouTube, Google, Stack Overflow, GitHub

### Requirements

- Python 3.13
- A working microphone
- Internet access (for speech recognition and Wikipedia)

### Setup

```powershell
cd Jarvis
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On Windows, **PyAudio** sometimes fails to install from pip alone. If that happens, install a prebuilt wheel for your Python version, then run `pip install -r requirements.txt` again.

### Run

```powershell
cd Jarvis
.\venv\Scripts\Activate.ps1
python Jarvis.py
```

Jarvis will initialize, speak a greeting, then listen for one command. Supported phrases include:

| Say something like… | Action |
|---------------------|--------|
| “search *topic*” | Short Wikipedia summary (spoken and printed) |
| “open youtube” | Opens YouTube in the default browser |
| “open google” | Opens Google |
| “open stack overflow” | Opens Stack Overflow |
| “open github” | Opens GitHub |

Recognition is case-insensitive and looks for keywords inside your phrase.

### Project layout

```
Jarvis/
├── Jarvis.py          # Main entry point
├── requirements.txt   # Pinned dependencies
└── .gitignore         # Ignores venv/
```

---

## Adding a new project

1. Create a folder at the repo root (e.g. `MyProject/`).
2. Add a `README` or section here describing what it does and how to run it.
3. Keep dependencies local (`requirements.txt`, `package.json`, etc.) inside that folder.

---

## License

Unless noted otherwise in a subproject, treat this repo as personal experimentation—use and adapt at your own discretion.
