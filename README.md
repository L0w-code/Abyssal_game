🌍 Abyssal_game – 2D Adventure Game

Treasure Explorer is a Python-based 2D exploration game developed using Pygame and Tiled Map Editor.
The player controls a small boat moving across different maps, collecting treasures while navigating around obstacles.

🧩 Key Features

Animated player movement in four directions (up, down, left, right).

Tile-based environment created with Tiled (.tmx/.tsx) and rendered via PyTMX and PyScroll.

Collision detection for walls and restricted zones.

Dynamic treasure collection system with an on-screen counter.

Victory screen displayed upon collecting all treasures.

🧱 Project Structure
main.py        → Launches the game and initializes the main loop
game.py        → Core gameplay logic, rendering, and interactions
player.py      → Player sprite management and animation handling
carte.tmx      → Main map file designed with Tiled
*.tsx, *.png   → Tilesets and graphic assets
win.png        → Victory screen image

⚙️ Installation & Execution
# Install dependencies
pip install pygame pytmx pyscroll

# Run the game
python main.py

🗺️ Tools & Technologies

Python 3.x

Pygame for game logic and rendering

PyTMX and PyScroll for map handling

Tiled for map and tileset design
