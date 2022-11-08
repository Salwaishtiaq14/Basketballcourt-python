### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###
def calculateArea(width,length):
    area= width * length
    return area


#### End OF MARKER



### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
def checkTilesFit(plot_width, plot_length, tile_width, tile_length):

    if (plot_width % tile_width == 0) and (plot_length % tile_length == 0):
	return True

    elif (plot_width % tile_length == 0) and (plot_length % tile_width == 0):
        return True
 
    else:
        return False
    
    
    




#### End OF MARKER



### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###
def calculateTiles(plot_width, plot_length, tile_wdith, tile_length):

    if (type(plot_width) is str or type(plot_length) is str or type(tile_wdith) is str or type(tile_length) is str):
        return "Invalid Input"

    if (plot_width == 0 or plot_length == 0 or tile_wdith == 0 or tile_length == 0):
        return None

b = checkTilesFit(plot_width, plot_length, tile_wdith, tile_length)

    if b == True:
         return (plot_width * plot_length) / (tile_wdith * tile_length)
    else:

        return "Not Possible"



#### End OF MARKER



