#!/usr/bin/env/ python

import sys
import time
from subprocess import check_output
import re



class latex_file:
    
    file_name = ""
    title = ""
    author = "Samuel Barratt"

    content = []


    def __init__(self, date, title):

        self.content = ["\documentclass{article}",
                   "\usepackage{fullpage}",
                   "\usepackage{fancyhdr}",
                   "\usepackage{natbib}",
                   "\usepackage{cite}",
                   "\pagestyle{fancyplain}",
                   "\setlength{\parindent}{0pt}",
                   "\setlength{\headsep}{0.2in}",
                   "\\title{"+self.title+"}",
                   "\\author{"+self.author+"}",
                   "\\begin{document}",
                   "\lfoot{"+self.author+"}",
                   "\\rfoot{\\today}",
                   "\sffamily{",
                   "    \maketitle",
                   "\n\n",
                   "\\bibliography{"+self.file_name+"}{}",
                   "\\bibliographystyle{apalike}"]

        self.title = title #make the class's title equal to the given title
        
        self.file_name = title.replace(" ","_")     #replace all the spaces with underscores and save

        f = open(str(date)+"_"+self.file_name+".tex", "w")   #create and open a file
        
        for x in range(0, len(self.content)):    #write all the lines to the file
                f.write(self.content[x]+"\n")

        f.close()       #close the file.

        return


class bibtex_file:

    title = ""
    file_name = ""

    def __init__(self, date, title):
        self.title = title #make the class's title equal to the given title
        
        self.file_name = title.replace(" ","_")     #replace all the spaces with underscores and save

        f = open(str(date)+"_"+self.file_name+".bib", "w")   #create and open a file
        f.close()

        return




def main():

    if len(sys.argv) != 0:
        proj_title = sys.argv[1]


    date = check_output(["date", "+%s"]) #Get unix time. 
    print str(date)+"somethign"
    date =  re.sub('[^A-Za-z0-9\.]+', '', date)
    print date
    
    ltx = latex_file(date, proj_title)
    bibtex_file(date, proj_title)
    
    return 0 

if __name__ == "__main__":
    main()
