# Asteroids

![GitHub License](https://img.shields.io/github/license/ellisf09/asteroids)
![GitHub last commit](https://img.shields.io/github/last-commit/ellisf09/asteroids)

<img src="https://skillicons.dev/icons?i=py">

A classic arcade Asteroids clone built in Python using `pygame` and object-oriented game loop design.

## ✨ Features
- **Physics & Hitboxes:** Custom circular collision detection (`circleshape.py`) and vector-based momentum.
- **Splitting Mechanics:** Shooting large asteroids splits them into smaller, faster-moving fragments.
- **Event Logging:** Tracks gameplay events in structured `game_events.jsonl` logs.

## 🎮 Controls
- `W` / `S` – Thrust forward / backward
- `A` / `D` – Rotate ship left / right
- `Space` – Fire projectiles

## 🚀 Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ellisf09/asteroids
   cd asteroids
   ```
2. **Install dependencies and run:**
   ```bash
   uv sync
   uv run main.py
   ```
