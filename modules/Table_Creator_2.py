# This Script for generating Tables
# Steps:
#       [1] Get The Table Title
#       [2] Get The Table Cells width
#       [3] Get The Table Column Names
#       [4] Get The Table Cells Data
# ==========================================================

# Import Print Function
from __future__ import print_function

def calc_space_before(word,cell_length):
    # Get Total width of cell
    # Sub The Length of word
    # Return the value devided by 2
    return int((cell_length - len(word))/2)

def Cells_Line(columns_width,cell_line = "-",cells_seperator="+"):
    # Printing The Cell Tob Line
    for i in columns_width:
        print(cells_seperator + (cell_line * i), end="")
    # Closing Row Line
    print(cells_seperator)

def calc_space_after(word,cell_length):
    return int(int(cell_length) - (int((cell_length - len(word))/2) + len(word)))

def table_generator(title,columns_width,columns_names,columns_data,Space = " ",cell_line = "-",cells_seperator="+",data_seperator = "|"):
    """ This Function For Generating Tables """

    # Converting Title To String
    title = str(title)

    # Converting Columns Width to integer
    try:
        for i in range(len(columns_width)):
            columns_width[i] = int(columns_width[i])
            
    except ValueError:
        print("[-] Columns width must be integer values")

    # Converting Columns Data to String
    try:
        for i in range(len(columns_data)):
            for j in range(len(columns_data[i])):
                columns_data[i][j] = str(columns_data[i][j])
    except TypeError:
        print("[-] Data Must be in string type")
    
    # Caching The total Width From Columns Widthes
    total_width = 0

    for i in columns_width:
        total_width += i

    if len(title) >= total_width:
        columns_width[-1] = columns_width[-1] + (len(title)- total_width) + 2
        total_width = len(title) + len(columns_width) + 1
    else:
        total_width += (len(columns_width)-1)

    # Printing Table Header
    print(cells_seperator + (cell_line * total_width) + cells_seperator)

    # Printing The Title
    print(data_seperator + (Space * calc_space_before(title,total_width)) + title + (Space * calc_space_after(title,total_width)) + data_seperator)

    # Printing The Columns Titles Tob Line
    Cells_Line(columns_width,cell_line,cells_seperator)


    # Printing Columns Names
    for i in range(len(columns_width)):
        print(data_seperator + (Space * calc_space_before(columns_names[i],columns_width[i])) + columns_names[i] + (Space * calc_space_after(columns_names[i],columns_width[i])) , end="")

    print(data_seperator)

    # Printing The Columns Titles Bottom Line
    Cells_Line(columns_width,cell_line,cells_seperator)

    # Printing Table Data
    for i in range(len(columns_data)):
        for j in range(len(columns_data[i])):
            print(data_seperator +(Space * calc_space_before(columns_data[i][j],columns_width[j])) + columns_data[i][j] + (Space * calc_space_after(columns_data[i][j],columns_width[j])), end="")
        print(data_seperator)
        # Printing The Seperator Line
        Cells_Line(columns_width,cell_line,cells_seperator)
    
    # ==================== End Of Table Generator Function ============
    

title = "Table Name Table Name Table Name Table Name Table Name Table Name Table Name Table Name Table Name Table Name Table Name Table Name"
columns_width = [7,41,9,15,9,9,9,9,9,8]
columns_names = ["ID","Fullname","Class","Degree","X","XX","XXX","xxxx","xxxx","xxxxx"]
columns_data = list()

for i in range(10):
    columns_data.append([(i+1),str("Mostafa " + str(i) + " Mahmoud"),"A",i*5,"x","xx","xxx","xxxx","xxxxx","xxxxxx"])

table_generator(title, columns_width, columns_names, columns_data)
