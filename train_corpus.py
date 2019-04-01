import codecs
import sys
import os

def run_train_corpus(template, input_file,model_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    intput_tag = input_file+"_tag.utf8"
    output_data = codecs.open(intput_tag, 'w', 'utf-8')
    for line in input_data.readlines():
        word_list = line.strip().split()
        for word in word_list:
            if len(word) == 1:
                output_data.write(word + "\tS\n")
            else:
                output_data.write(word[0] + "\tB\n")
                for w in word[1:len(word)-1]:
                    output_data.write(w + "\tM\n")
                output_data.write(word[len(word)-1] + "\tE\n")
        output_data.write("\n")
    input_data.close()
    output_data.close()

    cmd = "crf_learn -f 3 -c 4.0 "+template+" "+intput_tag+" "+model_file
    os.system(cmd)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print ("pls use: python train_corpus.py model input model_output")
        sys.exit()

    template = sys.argv[1]
    input_file = sys.argv[2]
    model_file = sys.argv[3]
    run_train_corpus(template, input_file, model_file)