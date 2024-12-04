import sys
import regex

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()

w = len(lines[0])
flat = ""

for line in lines:
    flat += line
    flat += "|"

for part in range(1, 3):
    total = 0
    if part == 1:
        total += flat.count("XMAS")
        total += flat.count("SAMX")
        total += len(regex.findall(fr"X.{{{w}}}M.{{{w}}}A.{{{w}}}S", flat, overlapped=True))
        total += len(regex.findall(fr"S.{{{w}}}A.{{{w}}}M.{{{w}}}X", flat, overlapped=True))
        total += len(regex.findall(fr"X.{{{w+1}}}M.{{{w+1}}}A.{{{w+1}}}S", flat, overlapped=True))
        total += len(regex.findall(fr"S.{{{w+1}}}A.{{{w+1}}}M.{{{w+1}}}X", flat, overlapped=True))
        total += len(regex.findall(fr"X.{{{w-1}}}M.{{{w-1}}}A.{{{w-1}}}S", flat, overlapped=True))
        total += len(regex.findall(fr"S.{{{w-1}}}A.{{{w-1}}}M.{{{w-1}}}X", flat, overlapped=True))
    else:
        total += len(regex.findall(fr"M.M.{{{w - 1}}}A.{{{w - 1}}}S.S", flat, overlapped=True))
        total += len(regex.findall(fr"M.S.{{{w - 1}}}A.{{{w - 1}}}M.S", flat, overlapped=True))
        total += len(regex.findall(fr"S.M.{{{w - 1}}}A.{{{w - 1}}}S.M", flat, overlapped=True))
        total += len(regex.findall(fr"S.S.{{{w - 1}}}A.{{{w - 1}}}M.M", flat, overlapped=True))
    print(f"Part {part}: {total}")
















