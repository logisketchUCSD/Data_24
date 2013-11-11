import xml.etree.ElementTree as etree
import os

class Dimensions:

    output = None
    gate_names = None
    writer = None

    def __init__(self):
        self.gate_names = ["AND", "NAND", "NOR", "NOT", "OR", "XNOR", "XOR"]
        self.initDimensions()
        
    def initDimensions(self):
        self.gate_heights = dict()
        for name in self.gate_names:
            self.gate_heights[name] = []
            self.gate_heights[name].append("Heights:")
            
        self.gate_widths = dict()
        for name in self.gate_names:
            self.gate_widths[name] = []
            self.gate_widths[name].append("Widths:")

        self.gate_ratios = dict()
        for name in self.gate_names:
            self.gate_ratios[name] = []
            self.gate_ratios[name].append("Ratios (width/height):")

    def getSketchInfo(self, writer, output, user_num, filename):

        self.output = output
        self.output.write(filename + '\n')

        self.writer = writer

        self.fromXML(user_num, filename)

        self.output.write('\n\n')
        
    def fromXML(self, user_num, filename):
        doc = etree.parse("User" + str(user_num) + "/Final Circuits/" + filename)
        node = doc.getroot()

        for child in node.getchildren():

            if child.tag == "shape":
                self.getDimensions(child)

    def getDimensions(self, xmlObject):
        
        shapeType = xmlObject.get("type")

        if shapeType in self.gate_names:
            height = xmlObject.get("height")
            width = xmlObject.get("width")

            self.writeToFile(shapeType, height, width)
            self.addToCSV(shapeType, height, width)

    def writeToFile(self, shapeType, height, width):
        self.output.write("Shape Type: " + shapeType + '\n')
        self.output.write("Height: " + height + '\n')
        self.output.write("Width: " + width + '\n')
        ratio = float(width)/float(height)
        self.output.write("Ratio (width/height): " + str(ratio) + '\n\n')

    def addToCSV(self, shapeType, height, width):

        assert(shapeType in self.gate_heights.keys())
        
        self.gate_heights[shapeType].append(height)
        self.gate_widths[shapeType].append(width)
        self.gate_ratios[shapeType].append(float(width)/float(height))

    def writeToCSV(self):

        perfect_ratios = self.calcPerfectRatios()

        for gate in self.gate_heights.keys():

            # Fix length of perfect ratios list
            for x in range(len(self.gate_heights[gate]) - 2):
                perfect_ratios[gate].append(perfect_ratios[gate][1])
                
            self.writer.writerow(tuple([gate]))
            self.writer.writerows((tuple(self.gate_heights[gate]),
                                   tuple(self.gate_widths[gate]),
                                   tuple(self.gate_ratios[gate]),
                                   tuple(perfect_ratios[gate])))

    def calcPerfectRatios(self):
        backCurveDepth = 2.9
        widthToSpace = 6.0
        widthToRadius = 8.0

        width = 100.0
        height = 100.0
        
        perfect_ratios = dict()
        perfect_ratios["AND"] = ["Perfect Ratio:",
                                 (width - width / widthToRadius * 2) / height]
        perfect_ratios["NAND"] = ["Perfect Ratio:",
                                  width / height]
        perfect_ratios["NOR"] = ["Perfect Ratio:",
                                 (width - width / widthToSpace) / height]
        perfect_ratios["NOT"] = ["Perfect Ratio:",
                                 width / height]
        perfect_ratios["OR"] = ["Perfect Ratio:",
                                (width -
                                width / (widthToRadius * 2) -
                                width / widthToSpace) / height]
        perfect_ratios["XNOR"] = ["Perfect Ratio:", width / height]
        perfect_ratios["XOR"] = ["Perfect Ratio:",
                                 (width - width / (widthToRadius * 2)) / height]

        return perfect_ratios
        
    

    

    
