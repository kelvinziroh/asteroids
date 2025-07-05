# 🚀 Asteroids ☄️

A lightweight recreation of the classic **Asteroids** arcade game built with **Python** and **Pygame**. This project is a fun, retro-inspired demo showcasing game development basics in the **Object Oriented Programming (OOP)** paradigm using a modern Python packaging tool — **uv**, the Python equivalent of npm.

![Asteroids](asteroids.gif)

## 🧰 Tech Stack

- **Language:** Python 3.11+
- **Game Engine:** [Pygame](https://www.pygame.org/) – a python library for building games
- **Package Manager:** [uv](https://github.com/astral-sh/uv) – a fast Python package/dependency manager built on Rust
- **Environment:** Cross-platform (Windows, macOS, Linux)

## 🛠️ Getting Started

You can get this game up and running on any system using just your terminal. No need for `git` or `venv` — everything is managed by `uv`.

### ✅ Prerequisites

- [Install Python 3.11+](https://www.python.org/downloads/)
- [Install uv](https://github.com/astral-sh/uv#installation)

```bash
# Recommended way to install uv
curl -Ls https://astral.sh/uv/install.sh | sh
```

## 📦 Setup Instructions

### Option 1: Download the ZIP archive (for users without Git)

1. Click the green **"Code"** button at the top of this repo and select **"Download ZIP"**.
2. Extract the contents to a folder of your choice.
3. Open a terminal and navigate to that folder:

```bash
cd path/to/asteroids
```

4. Run the game using `uv`:

```bash
uv venv
uv pip install
uv run python main.py

# or just
uv run main.py
```

### Option 2: Clone via Git (if you have Git installed)

```bash
git clone https://github.com/kelvinziroh/asteroids.git
cd asteroids
uv venv
uv pip install
uv run python main.py

# or just
uv run main.py
```

## 🎮 Controls
- ← / →: Rotate ship
- ↑: Thrust forward
- Space: Fire bullet
- Esc: Quit game

## 💡 Notes
- This implementation is intentionally simple and modular for learning purposes.
- You can easily customize and expand on this with new features like enemies, power-ups, or score tracking.
