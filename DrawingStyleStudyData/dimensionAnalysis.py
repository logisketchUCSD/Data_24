from dimensions import Dimensions
import os
import csv

def run_analysis():

    d = Dimensions()

    user_nums = [0, 2, 4, 6, 8, 10, 12, 25, 27,
                28, 29, 30, 31, 32, 33, 34, 35,
                36, 38, 39, 40, 41]

    for num in user_nums:

        # The path for the sketches
        path = "User" + str(num) + "/Final Circuits/"
        listing = os.listdir(path)

        # The path for the analysis
        directory = "Fall 2011 Study Analysis/dimensions/User" + str(num)

        if not os.path.exists(directory):
            os.mkdir(directory)
            
        write_file = directory + "/User" + str(num) + "_dimensionsAnalysis"
        output = open(write_file + ".txt", 'w')

        d.initDimensions()
        writer = csv.writer(open(write_file + ".csv", 'wb'))
 
        # Run for each sketch in the user's directory
        for infile in listing:

            extension = os.path.splitext(infile)[1]

            if extension == ".xml":
                d.getSketchInfo(writer, output, num, infile)

        d.writeToCSV()
        output.close()
