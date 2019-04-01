#!/usr/local/bin/python2

import codecs
import sys

import CRFPP


def run_segment(input_file, output_file, tagger):
    """
    Segment a chinese text file, write the result to output file
    :param input_file: inputfile name
    :param output_file: outputfile name
    :param tagger: CRFPP object
    """
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')

    for line in input_data.readlines():
        tagger.clear()
        for word in line.strip():
            word = word.strip()
            
            if word:
                tagger.add((word + "\tB\n").encode('utf-8'))
        tagger.parse()
        size = tagger.size()
        xsize = tagger.xsize()
        for i in range(0, size):
            for j in range(0, xsize):
                char = tagger.x(i, j).decode('utf-8')
                tag = tagger.y2(i)
                output_data.write(char)
                if tag == 'E' or tag == 'S':
                    output_data.write(' ')
        output_data.write("\n")
    input_data.close()
    output_data.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print ("pls use: python segment.py model input output")
        sys.exit()
    crf_model = sys.argv[1]  
    input_file = sys.argv[2]  
    output_file = sys.argv[3]
    tagger = CRFPP.Tagger("-m " + crf_model)  
    run_segment(input_file, output_file,tagger)
