# From https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip
import pickle
from os import walk

data = {}

def process_unihan_file(filename):
    lines = open(filename, 'r').read().split('\n')
    print(f'Processing {filename}...')
    for i, line in enumerate(lines):
        if '# EOF' in line:
            break
        if '#' in line or len(line.strip()) <= 0:
            continue
        unicode, entry_type, entry_value = line.split('\t')
        unicode_value = int(unicode.replace('U+', '0x'), 16)
        if unicode_value not in data.keys():
            data[unicode_value] = {}
        data[unicode_value][entry_type] = entry_value

unihan_path = './Unihan'
filenames = list(walk(unihan_path))[0][2]
for filename in filenames:
    if filename.startswith('Unihan') and filename.endswith('.txt'):
        process_unihan_file(unihan_path + '/' + filename)

stroke_data = {}
for i, (k, v) in enumerate(data.items()):
    # Look for simplified characters only that are within UTF-16 range...
    if 'kTraditionalVariant' not in v or k > 0xffff:
        continue
    try:
        stroke_count = int(v['kTotalStrokes'])
        stroke_data[k] = stroke_count
    except:
        print(f'Character {chr(k)} (U+{hex(k)[2:]}) not included due to multiple stroke counts: ' + v['kTotalStrokes'])

with open('stroke_count.pkl', 'wb') as f:
    pickle.dump(stroke_data, f)
