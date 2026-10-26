Falling Star Game
A simple 2D game built with Python's built-in turtle graphics module. Move the red player bar left and right to catch the falling blue star. Each successful catch increases your score. If the star falls past the bottom of the screen, the game ends.
Features
- Black game window with a red player bar and a blue falling star
- Keyboard controls for moving left and right
- Randomized star starting position and falling speed
- Score counter that updates when you catch the star
- Game-over message when you miss the star
Requirements
- Python 3
- The turtle module (usually included with standard Python installations)
- A graphical desktop environment that can open a Turtle graphics window
The game uses random, which is also included with Python.
How to Run
1. Save the game code as main.py.
2. Open a terminal or command prompt in the folder containing main.py.
3. Run:
   python main.py
   On some systems, you may need to use:
   python3 main.py
Controls
Key / Action	Result
Left Arrow	Move the red player bar left
Right Arrow	Move the red player bar right
Click after Game Over	Close the game window


How to Play
1. Start the program to open the game window.
2. Use the left and right arrow keys to move the red bar.
3. Catch the falling blue star to earn one point.
4. Keep catching the star to increase your score.
5. If you miss the star and it falls below the screen, the game displays GAME OVER.
6. Click the game window after the game-over message to close it.
How It Works
- Player class: Creates the red player bar and defines its left/right movement.
- Star class: Creates the blue star, places it at a random horizontal position at the top, and gives it a random falling speed.
- Collision detection: The game checks the distance between the player and the star. If it is less than 30 pixels, the star is reset and the score increases.
- Game loop: The game_loop() function updates the star's position and refreshes the screen about every 20 milliseconds.
- Game over: If the star falls below the lower boundary without being caught, the game stops and displays a game-over message.
Project Structure
.
├── main.py
└── README.md
Troubleshooting
- The game window does not open: Run the script in a desktop environment with graphical interface support.
- turtle or Tkinter errors: Check that your Python installation includes Tkinter, which Turtle uses to create its window.
- The arrow keys do not respond: Click the game window to focus it, then try the arrow keys again.
Possible Improvements
- Add multiple falling stars.
- Add lives or levels.
- Increase the falling speed as the score grows.
- Add a restart option after Game Over.
- Improve the player boundary checks so the bar stays fully inside the window.
License
No license is specified. Add a license file if you intend to distribute or publish this project.
