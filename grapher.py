import sys
import os
import re
import subprocess

class Grapher:
    
    def __init__(self, base, args):
        self.base = base
        self.args = args

    def params(self):
        filename = self.base
        f = open(filename, 'r')

        params = []

        regex = re.compile("@target *")
        for line in f:
            if re.match(regex, line):
                break
            else:
                params.append(line)
        return params

    def output_name(self):
        output_name = input("Name the NEW .agr file, then press ENTER: ")
        if ".agr" in output_name:
            return output_name
        else:
            regex = re.compile('\.\W\W\W$')
            if re.search(regex, output_name):
                return output_name.replace(output_name[-1:-5], ".agr")
            else:
                output_name = output_name + ".agr"
                return output_name


    def titles(self):
        title = input('Type in graph title, then press ENTER: ')
        subtitle = input('Type in graph subtitle, then press ENTER: ')
        titles = [title, subtitle]
        
        return titles

    def data(self):
        files = self.args

        data = os.getcwd() + "/files/data.txt"
        datafile = open(data, 'w')

        filepaths = []

        i = 0
        for item in files:
            filename = item
            path = os.getcwd()
            filepaths.append(path + "/" +filename)
            f = open(filename, 'r')
            datafile.write("@target G0.S" + str(i))
            datafile.write("\n")
            datafile.write("@type xydy")
            datafile.write("\n")
            for line in f:
                line_parts = line.split()
                res = line_parts[0]
                avg = line_parts[1]
                if len(line_parts) > 2:
                    std = line_parts[2]
                    datafile.write(str(res) + " " + str(avg) + " " + str(std))
                    datafile.write("\n")   
                else:
                    datafile.write(str(res + " " + str(avg)))
                    datafile.write('\n')
            i += 1 

        datafile.close()

        return filepaths

    def edit_params(self):
        params = self.params()
        output = self.output_name()
        titles = self.titles()
        filepaths = self.data()

        regex = re.compile('@    s\d comment')
        
        filename = os.getcwd() + "/files/data.txt"
        f = open(filename, 'r')
        data = []
        for line in f:
            data.append(line)
        f.close()

        filename = output
        f = open(filename, 'w')

        target = 0
        title_pass = 0
        subtitle_pass = 0
        for line in params:
            if re.match(regex, line):
                f.write('@    s' + str(target) + ' comment "' + filepaths[target] + '"')
                f.write('\n')
                target +=1
                continue
            elif "@    title" in line:
                if title_pass == 0:
                    f.write('@    title "' + titles[0] + '"')
                    f.write('\n')
                    title_pass +=1
                    continue
                else:
                    f.write(line)
                    continue
            elif "@    subtitle" in line:
                if subtitle_pass == 0:
                    f.write('@    subtitle "' + titles[1] + '"')
                    f.write('\n')
                    subtitle_pass += 1
                    continue
                else:
                    f.write(line)
                    continue
            else:
                f.write(line)
        
        for line in data:
            f.write(line)
        
        f.write("@PRINT TO " + os.getcwd() + "/" + output.replace('.agr', '.png'))
        f.write('\n')
        f.write('@HARDCOPY DEVICE “PNG”')
        f.write('\n')
        f.write('@DEVICE “PNG” FONT ANTIALIASING on')
        f.write('\n')
        f.write('@DEVICE “PNG” OP “compression:9”')
        f.write('\n')
        f.write('@DEVICE “PNG” PAGE SIZE 3300, 2550')
        f.write('\n')
        f.write('@DEVICE “PNG” DPI 300')
        f.write('\n')
        f.write('@PRINT')

        f.close()

        





args = sys.argv[1:]
base = input("Type the name of the. agr file you wish to replicate, then press ENTER: ")
if ".agr" not in base:
    regex = re.compile('\.\W\W\W$')
    if re.search(regex, base):
        extention = base[-1:-5]
        base = base.replace(extention, ".agr")
grapher = Grapher(base, args)
grapher.data()
grapher.edit_params()
