
import fontforge
import os
import sys

def handle(path):
	font = fontforge.open(path)
	print(font.hhea_ascent, font.hhea_descent, font.hhea_linegap)
	print(font.os2_typoascent, font.os2_typodescent, font.os2_typolinegap)
	print(font.os2_winascent, font.os2_windescent)
	font.hhea_ascent = font.os2_winascent
	font.hhea_descent = -font.os2_windescent
	font.hhea_linegap = 0
	font.os2_typoascent = font.os2_winascent
	font.os2_typodescent = -font.os2_windescent
	font.os2_typolinegap = 0
	return font

if __name__ == '__main__':
	arguments = sys.argv[1:]
	for path in arguments:
		basename = os.path.basename(path)
		filename = f'baseline-{basename}'
		font = handle(path)
		font.save(filename)
