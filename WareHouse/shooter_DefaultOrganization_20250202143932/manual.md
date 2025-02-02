# Terminal Blaster

An insanely addictive fast-paced action CLI shooter game.

## Table of Contents

- [Introduction](#introduction)
- [Game Features](#game-features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [How to Play](#how-to-play)
  - [Game Controls](#game-controls)
  - [Objective](#objective)
  - [Scoring](#scoring)
- [Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
- [License](#license)

## Introduction

Welcome to **Terminal Blaster**, a ridiculously addictive and fast-action shooter game that runs right in your command line interface (CLI). Battle endless waves of enemies in this retro-style ASCII arcade game, sharpen your reflexes, and climb your way to the top of the leaderboard.

## Game Features

- **Fast-Paced Gameplay**: Experience quick and intense action as enemies spawn rapidly.
- **Simple Controls**: Easy to learn controls, perfect for players of all levels.
- **Retro Aesthetics**: Enjoy the nostalgic feel of classic arcade games with ASCII graphics.
- **Dynamic Difficulty**: The game speeds up as you progress, providing a continuous challenge.
- **Scoring System**: Keep track of your high scores and challenge yourself to beat them.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux systems with Python installed.

## Installation

### Prerequisites

- **Python 3.6 or higher** installed on your system.
- **pip** package manager (usually comes with Python).
- A terminal or command prompt to run the game.

### Installation Steps

1. **Download the Game**

   Clone the repository or download the source code from the release page.

   ```bash
   git clone https://github.com/yourusername/terminal-blaster.git
   ```

2. **Navigate to the Game Directory**

   ```bash
   cd terminal-blaster
   ```

3. **Install the Required Dependencies**

   Install the game dependencies listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

   **Note for Windows Users**:

   The `curses` module is not available by default on Windows. You need to install the `windows-curses` package.

   ```bash
   pip install windows-curses
   ```

## How to Play

### Starting the Game

Run the following command in your terminal:

```bash
python main.py
```

### Game Controls

- **Move Left**: Press `a` or the **Left Arrow** key.
- **Move Right**: Press `d` or the **Right Arrow** key.
- **Shoot**: Press **Spacebar** or `w`.
- **Quit Game**: Press `q`.

### Objective

- **Destroy Enemies**: Shoot down incoming enemies represented by `V` before they reach the bottom of the screen.
- **Survive**: Avoid letting enemies collide with your player character, represented by `^`.

### Scoring

- **+1 Point**: For each enemy you successfully destroy.
- **-1 Point**: For each enemy that reaches the bottom of the screen.
- **Game Over**: If an enemy collides with your player character.

### Game Over Screen

At the end of the game, your final score will be displayed. Press any key to exit the game.

## Troubleshooting

### Common Issues

#### Error Importing `curses` Module

**On Windows**:

If you receive an error message similar to:

```
Error importing curses module. On Windows, please install the 'windows-curses' package:
pip install windows-curses
```

**Solution**:

Install the `windows-curses` package:

```bash
pip install windows-curses
```

#### Terminal Size Issues

If the game doesn't display correctly, ensure your terminal window is large enough to accommodate the game interface. Resize your terminal window if necessary.

#### Unicode Errors

If you experience Unicode errors, make sure your terminal supports UTF-8 encoding.

## License

This game is released under the [MIT License](LICENSE).

---

Enjoy the game, and have fun blasting those enemies!