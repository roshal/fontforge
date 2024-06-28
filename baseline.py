
import os
import pathlib

def open_font(path: str):

	font = fontforge.open(path)

	return font

def operate_font(font: fontforge.font):

	print(font.hhea_ascent, font.hhea_descent, font.hhea_linegap)
	print(font.os2_typoascent, font.os2_typodescent, font.os2_typolinegap)
	print(font.os2_winascent, font.os2_windescent)

	font.hhea_ascent = font.os2_winascent
	font.hhea_descent = -font.os2_windescent
	font.hhea_linegap = 0

	font.os2_typoascent = font.os2_winascent
	font.os2_typodescent = -font.os2_windescent
	font.os2_typolinegap = 0

def get_subtitle():

	filename = os.path.basename(__file__)

	subtitle = os.path.splitext(filename)[0]

	return subtitle

def operate_arg(arg: str):

	path = arg

	font = open_font(path)

	operate_font(font)

	subtitle = get_subtitle()

	filename = os.path.basename(path)

	subtitlePath = pathlib.Path(subtitle)

	subtitlePath.mkdir(exist_ok=True)

	filePath = subtitlePath.joinpath(filename)

	filepath = str(filePath)

	font.generate(filepath)

if __name__ == '__main__':

	arg_list = sys.argv[1:]

	for arg in arg_list:
		operate_arg(arg)
