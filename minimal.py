#!/usr/bin/env python3

src = '.config'
dst = 'arch/arm64/configs/defconfig'

with open(src) as f:
    srclines = f.readlines()

with open(dst) as f:
    dstlines = f.readlines()

for line in srclines:
    if line not in dstlines:
        if line[0] != '\n' and line[0] != '#':
            print(line.strip())
