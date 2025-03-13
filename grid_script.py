# https://namethattech.wordpress.com/2017/03/22/how-to-make-a-snap-to-grid-in-fontforge/comment-page-1/

# This script outputs instructions to draw a snap grid in FontForge.
# python3 script.py > grid.txt
# Then copy these instructions just below the only occurence of ‘Grid’ in a .sfd (FontForge file).

GRID_STEP = 64
SNAP_STEP = 16
MIN_X = GRID_STEP * -2
MAX_X = GRID_STEP * 16
MIN_Y = GRID_STEP * -3
MAX_Y = GRID_STEP * 10

# Lines
for y in range(MIN_Y, MAX_Y + 1, GRID_STEP):
	print(f"{MIN_X} {y} m 1")
	print(f"{MAX_X} {y} l 1")

# Lines
for x in range(MIN_X, MAX_X + 1, GRID_STEP):
	print(f"{x} {MIN_Y} m 1")
	print(f"{x} {MAX_Y} l 1")

# By moving the pen, we can add snap points without drawing anything
for y in range(MIN_Y, MAX_Y + 1, SNAP_STEP):
	for x in range(MIN_X, MAX_X + 1, SNAP_STEP):
		print(f"{x} {y} m 1")