# Basketballcourt-python
Calculating area for basket ball court in python.


Consider that Ali has just purchased a plot in Hayatabad of width “plot_width” and length
“plot_length”. Ali is a well known basketball player in FAST NUCES. Ali wants to enhance his
basketball skills. Therefore Ali wants to convert that to a basketball court. For that, Ali first has to
install tiles on the plot. The tiles Ali has purchased have width “tile_width” and length
“tile_length”. Consider that the plot’s surface is already leveled and is ready for tiles installation.
Ali is also too conscious about the basketball court. Ali doesn't want to break the tile into pieces
either it is fully fit or it is not fit in the plot area.

1.1 Tasks to do

There are three main tasks to complete:
1. Write a function with the name “calculateArea” that takes in two inputs (width and
length) and return the area.

2. Write a function with the name “checkTilesFit” which takes in four inputs
(plot_width, plot_length, tile_width, tile_length) and checks the tiles with the
length and width given in the parameter fit into the area of the plot, If yes then
this function return “True” else this function return “False”.

3. Finally, write a function with the name “calculateTiles” that takes in four inputs
(plot_width, plot_length, tile_wdith, tile_length) and returns the number of tiles
required to cover the whole plot without breaking the tiles. The number of tiles
should be an integer not a float.
a. If the type of any of the parameters is “str”, return “Invalid Input”.
b. If the value of any of the parameters is zero, return None.
c. You have to call the “checkTilesFit” function, If this “checkTilesFit” function
returns “True” then you need to return the number of tiles after calculating
the number of tiles else you have to return “Not Possible”.
