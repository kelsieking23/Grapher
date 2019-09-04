# Grapher
## Creates .agr files with new data based on a previously made .agr file in qtGrace.

Grapher.py creates new .agr files based on the .agr file of a previous graph in qtGrace. This script is useful if you have several graphs to make of the same style. For example, if you have many hydrogen bond analysis graphs between different groups, this script will automate the graphing process. Currently one graph can be made at a time. In the near future, a tool will be added to automate the entire process over many groups/replicates. 

To begin, you must make a graph in qtGrace. qT grace creates .agr files for each graph. The .agr file contains information about the design of the graph (fonts, colors, etc). When you are happy with your graph, you can begin the download process. 

To begin, click the green Clone/Download button. From there, click Download ZIP. Once the file is downloaded, extract the ZIP to access its contents. You should now have a new folder called **Grapher-master**.

The grapher.py script assumes that you have created .dat files to plot in qtGrace. Move all .dat files you want to graph into the Grapher-master folder. 

To make a graph, in your terminal, cd into the Grapher-Master folder where you have placed your .dat files. For each .dat file you wish to put into a *single* graph, you must pass those file names as arguments in the command line. 
For example, I want to make a graph with hbonds1.dat, hbonds2.dat, and hbonds3.dat. In the command line, I will type:

```
python3 grapher.py hbonds1.dat hbonds2.dat hbonds3.dat
```
The script will then ask you for input. In your terminal, you will recieve the prompt:
```
Type the name of the. agr file you wish to replicate, then press ENTER:
```
Here, you will type in the name of the .agr file you made previously.

Then, the script will ask you what you want to name the new .agr file to be created. 
```
Name the NEW .agr file, then press ENTER: 
```
Type in the file name for the new file.
A few more prompts. The script will ask you to input a Title and a Subtitle for the graph. In these feilds, you can type your title as you would into qtGrace, including special charecters. 
```
Type in graph title, then press ENTER: 
Type in graph subtitle, then press ENTER: 
```
The script will then run and create your new .agr file. The file will be deposited in the Grapher-master folder. 
