import enum
import os

def main():
    # parse('demo/ramfile30.ram')
    # parse('demo/ramfile90.ram)
    parse('RAMFILES/10_03.ram')
    print(os.path.basename('RAMFILES/10_03.ram'))

def parse(file_path):
    delimiters = detect_sections(file_path)
    print(delimiters)
    blocks = split_sections(file_path, delimiters)
    for i, block in enumerate(blocks):
        print(f'Block {i+1}')
        print('~'*150)
        for section_name in block:
            print(f'Section {section_name}')
            print('~'*150)
            print(block[section_name])
            print('~'*150)


def read_file_to_str(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read() 

def detect_sections(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            delimiters = []
            for n, line in enumerate(f):
                print(n, line[:-1]) # [:-1] used to remove the line break
                #if line.startswith('date from'):
                import re
                first_line_pattern = re.compile(
                    '(\S+)\s+(\d{2}.\d{2}.\d{4})\s+(\d{2}:\d{2})')
                if first_line_pattern.match(line):
                    delimiters.append({}) # add new block!
                    delimiters[-1]['first_line'] = n
                elif line.startswith('-'*10):
                    delimiters[-1]['hyphens'] = n
            return delimiters

def split_sections(file_path, delimiters):
    sections = []
    file_str = read_file_to_str(file_path)
    lines = file_str.split('\n')
    for i, delimiter in enumerate(delimiters):
        #Append new section block
        sections.append({})
        # Add 'date' section to last block
        sections[-1]['date']=lines[delimiter['first_line']]
        # Add 'tabel1' section to last block
        table_1_from = delimiter['first_line']+2
        table_1_to = delimiter['hyphens']-1
        sections[-1]['table1'] = '\n'.join(lines[table_1_from:table_1_to])
        #Add 'table 2' section to last block
        table_2_from = delimiter['hyphens'] - 1
        if i+1 < len(delimiters):
            #not the last block, read until next block start
            table_2_to = delimiters[i+1]['first_line']
        else:
            # last block, read until end of file
            table_2_to = None
        sections[-1]['table2'] = '\n'.join(lines[table_2_from:table_2_to])
    return sections

main()