
import fontforge
import os
import sys

def handle(path):
	font = fontforge.open(path)
	name = os.path.basename(path)
	a = font.os2_winascent
	d = font.os2_windescent
	print(font.hhea_ascent, font.hhea_descent, font.hhea_linegap)
	font.hhea_ascent = a
	font.hhea_descent = -d
	font.hhea_linegap = 0
	print(font.os2_typoascent, font.os2_typodescent, font.os2_typolinegap)
	font.os2_typoascent = a
	font.os2_typodescent = -d
	font.os2_typolinegap = 0
	print(font.os2_winascent, font.os2_windescent)
	font.save(f'baseline-{name}')

if __name__ == '__main__':
	arguments = sys.argv[1:]
	for path in arguments:
		handle(path)
