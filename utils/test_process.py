import codecs
import sys

def character_split(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')

    for line in input_data.readlines():
        for word in line.strip():
            word = word.strip()
            if word:
                output_data.write(word + "\tB\n")
        output_data.write("\n")# 每行话之间隔一行就好处理了
        
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ("pls use: python make_crf_test_data.py input output")
        sys.exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    character_split(input_file, output_file)
