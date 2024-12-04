import sys

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()

counter = 0
allow_removals = False

for part in range(1, 3):
    for line in lines:
        line = list(map(int, line.split(" ")))
        versions = [line]
        if part == 2:
            for i in range(len(line)):
                versions.append(line[:i] + line[i+1:])
        for version in versions:
            if version != sorted(version) and version != sorted(version, reverse=True):
                continue
            if next((x for x in (abs(a-b) for a, b in (zip(version, version[1:]))) if x < 1 or x > 3), None) is not None:
                continue
            counter += 1
            break
    print(f"Part {part}: {counter}")