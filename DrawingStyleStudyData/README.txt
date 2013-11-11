############################################################################
######################### DRAWING STYLE STUDY DATA #########################
############################################################################

Documented by: Kiley Sobel (ksobel@hmc.edu)
Date: 7/20/11

This is the data collected from the study on how users change their drawing
styles over time in different conditions***.

########################################
# HOW TO RUN STUDY & ANALYSIS Document #
########################################

This document explains how to run the user study program and how to run
the TestRig script on the study data.


###############################
# PILOT DATA AND USER FOLDERS #
###############################

These hold the pilot and study data.

For Pilot Data 1, the files names are based on 

* the user
* the equation of the gate drawn
* the iteration number (which is either the first or second time drawn)
* the number of times the sketch was recognized.

For Pilot Data 2 - 4 and all of the users, the file names are based on

* the order the sketch was drawn (0 - 7)
* the equation
* the condition (Condition 1 is Gates On, Condition 2 is Gates Off)
* the iteration number (which is either the first or second time drawn)
* whether the sketch is recognized or unrecognized
* the number of times the sketch as been recognized (if it's recognized)

#########################################
# FINAL CIRCUIT FOLDERS in USER FOLDERS #
#########################################

In the User folders, the Final Circuit folders contain all of the final
recognized, complete circuits of every equation done in the study (twice).

Most of the folders also contain "Gate Time Variance Data," which is
data collected from TestRig, and "Gate Time Variance Data With Graph,"
which holds the same data as the previous csv file, but also has extra
info and a graph.


###########################
# OTHER FOLDERS AND FILES #
###########################

-----------------------
USER STUDY DATA FOLDER:
-----------------------
This has all of the "Gate Time Variance Data With Graph" data, without
the graph, compiled into one folder for each user.

-----------------------------------
USER STUDY EQUATION SAMPLES FOLDER:
-----------------------------------
This has a list of all of the equations and their corresponding sketches.

---------------------------------------
USER STUDY DOCUMENTS AND VIDEOS FOLDER:
---------------------------------------

This folder holds everything necessary to carry out the user study:

* Tutorial Videos (Condition 1 with Ghost Gates, Condition 2 without)
* Consent Form
* Script
* Prize Description
* Circuit examples (a large circuit, circuit with canes)
* Logic Gate key (in color and black and white for printing)
* Unedited video files

------------------------------------
USER STUDY VERSION INSTALLER FOLDER:
------------------------------------
This holds the installer for the version of LogiSketch we used for the study.

--------------------------------
AGGREGATED USER STUDY DATA FILE:
--------------------------------
This file combines all of the data from the User Study Data Folder and graphs
the correct recognition rate over time by condition.

--------------------------------------
USER STUDY INTERVIEW- GOOGLE DOC FILE:
--------------------------------------
This file holds all of the questions and answers from the user study interview.

-----------------------------------
USER STUDY INTERVIEW DATA ANALYSIS:
-----------------------------------
This file holds all of the scaled answers from the user study interview, and
averages that data in order to perform analysis on it.




***Note:
Condition 1: With Ghost Gates
Condition 2: Without Ghost Gates
Condition 3: Same as Condition 1, but with script change
Condition 3.5: Same as Condition 3, but with script change
(Condition's 3 and 3.5 are ran as Condition 1)