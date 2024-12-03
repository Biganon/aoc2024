import sys

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()

counter = 0
allow_removals = False

for line in lines:
    line = list(map(int, line.split(" ")))
    versions = [line]
    if allow_removals:
        for i in range(len(line)):
            versions.append(line[:i] + line[i+1:])
    for version in versions:
        print(version)
        if version != sorted(version) and version != sorted(version, reverse=True):
            print("nope, pas incrémentielle ou décrémentielle")
            continue
        if next((x for x in (abs(a-b) for a, b in (zip(version, version[1:]))) if x < 1 or x > 3), None) is not None:
            print("nope, un écart ne va pas")
            continue
        counter += 1
        print("tout bon")
        break

print(counter)