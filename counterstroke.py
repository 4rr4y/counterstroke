import pickle, random, sys, io

# Restore stroke count for different simplified chinese characters
stroke_count = pickle.load(open('stroke_count.pkl', 'rb'))
if type(stroke_count) != dict:
    exit(0)

# Check mode
ENCODE, DECODE = '-e', '-d'
if len(sys.argv) < 2 or sys.argv[1] not in [ENCODE, DECODE]:
    print('Example Usage:', file=sys.stderr)
    print('echo "[plaintext]" | counterstroke.py -e', file=sys.stderr)
    print('counterstroke.py -e < [input file] > [output file]', file=sys.stderr)
    print('echo "[ciphertext]" | counterstroke.py -d', file=sys.stderr)
    print('counterstroke.py -d < [input file] > [output file]', file=sys.stderr)
    exit(0)
mode = sys.argv[1]

# Load stroke count mapping to potential chinese characters
max_stroke_count = max(list(stroke_count.values()))
stroke_map = []
for _ in range(max_stroke_count + 1):
    stroke_map.append([])
for k, v in stroke_count.items():
    stroke_map[v].append(k)

'''
# Check distribution of filtered simplified characters
for i in range(max_stroke_count + 1):
    print(i, len(stroke_map[i]))
'''
offset = 4 # between 4 to 19 (0x0 - 0xf), most characters

def encode(text):
    result = []
    for c in text:
        for txt_hex in [c >> 4, c & 0xf]:
            char_list = stroke_map[txt_hex + offset]
            result.append(char_list[random.randint(0, len(char_list) - 1)])
    return ''.join(map(chr, result))

def decode(text):
    result = []
    if len(text) % 2 != 0:
        print('Warning: encoding output might be incomplete', file=sys.stderr)
    for i in range(0, len(text), 2):
        byte_value = 0
        for j in range(i, i + 2):
            byte_value = (byte_value << 4) | (stroke_count[ord(text[j])] - offset)
        result.append(byte_value)
    return bytearray(result)

if mode == ENCODE:
    print(encode(sys.stdin.buffer.read()), end='')
if mode == DECODE:
    sys.stdout.buffer.write(decode(sys.stdin.read()))



