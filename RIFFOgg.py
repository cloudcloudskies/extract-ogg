from __future__ import print_function
import sys
import os
import struct

RIFF_MAGIC = b'RIFF'
WAVE_MAGIC = b'WAVE'
OGG_MAGIC = b'OggS'
META_CHUNKS = (b'RIFF', b'LIST')
GARBAGE_CHUNKS = (b'WAVE', b'INFO', b'adtl')

def validate_header(f):
    f.seek(0)
    magic = f.read(4)
    if magic != RIFF_MAGIC:
        return -1

    length = struct.unpack('<I', f.read(4))[0]
    if length <= 0:
        return -1

    wave_magic = f.read(4)
    if wave_magic != WAVE_MAGIC:
        return -1

    return length + 8

def extract_chunks(f, max_length=None):
    f.seek(12)
    read_length = 12

    while not max_length or read_length < max_length:
        chunk_type = f.read(4)
        if not chunk_type:
            break
        read_length += 4

        if chunk_type in GARBAGE_CHUNKS:
            yield (chunk_type, b'')
            continue
        else:
            chunk_length = struct.unpack('<I', f.read(4))[0]
            read_length += 4

        if chunk_type in META_CHUNKS:
            yield (chunk_type, b'')
        else:
            chunk_data = f.read(chunk_length)
            read_length += chunk_length
            yield (chunk_type, chunk_data)

            if chunk_length % 2:
                f.read(1)
                read_length += 1

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('Usage: {} FILE OUTFILE'.format(sys.argv[0]))

    infile = sys.argv[1]
    outfile = sys.argv[2]

    with open(infile, 'rb') as f:
        length = validate_header(f)
        if length <= 0:
            sys.exit('Not a RIFF file: {}'.format(infile))

        for (type, data) in extract_chunks(f, length):
            if type == b'data' and data[:4] == OGG_MAGIC:
                with open(outfile, 'wb') as out:
                    out.write(data)
                break
        else:
            print('Could not find embedded OGG data.', file=sys.stderr)
