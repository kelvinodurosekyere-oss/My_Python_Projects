
Random Geometric Pattern Generator
A small Python drawing project that uses the built-in turtle graphics module to create a colorful grid of randomly selected geometric shapes.

The program draws shapes in 13 columns and 10 rows. Each shape is given a randomly selected size/step configuration and a color from a predefined RGB palette, so each run can produce a different pattern.
Features
- Generates a grid with 13 columns and 10 rows (130 shapes).
- Randomly selects shape configurations from a predefined list.
- Uses a palette of RGB colors for a coordinated look.
- Alternates the drawing direction in each column.
- Uses Python Turtle graphics to draw the pattern.
Requirements
- Python 3
- The turtle module, usually included with Python.
- A desktop environment that supports graphical windows.
The random module is part of Python's standard library.
How to Run
1. Save the script as main.py.
2. Open a terminal or command prompt in the project folder.
3. Run:
   python main.py
   Depending on your system, you may need to run:
   python3 main.py
4. When the drawing appears, click the Turtle window to close it.
How It Works
- Color mode: screen.colormode(255) enables RGB color values from 0 to 255.
- Color palette: color_palet stores the available RGB colors.
- Shape options: dif_shapes stores pairs used as the radius and step count passed to Turtle.circle().
- Grid layout: Nested loops place shapes across 13 columns and 10 rows, with 50 pixels between positions.
- Random variation: Each position receives a randomly selected shape configuration and color.
- Drawing: The Turtle moves to each grid position, draws a filled shape, and lifts its pen before moving to the next position.
Project Structure
.
├── main.py
└── README.md
Troubleshooting
- The Turtle window does not open: Run the script in a desktop environment with graphical interface support.
- Turtle/Tkinter errors: Check that your Python installation includes Tkinter.
- The window closes immediately: Make sure the script ends with screen.exitonclick() so the window remains open until clicked.
Customization
You can change the pattern by editing these values in the script:
- columns and rows to change the grid dimensions.
- spacing to change the distance between shapes.
- start_x and start_y to move the grid.
- dif_shapes to change the available circle step configurations.
- color_palet to add or remove RGB colors.
Notes
The script currently sets the Turtle screen to RGB color mode but does not explicitly set a background color. The displayed background therefore uses Turtle's default screen background.
License
No license is specified. Add a license if you plan to distribute or publish this project
