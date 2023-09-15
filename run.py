import pg2q as gui

gui_info = {
	# main info
	"title": "Test Title",
	"size": (200, 100),
	"fps": 30,
	"speed": 2,
	"color_bg": (10,10,10),
	"icon_path": False,

	# json sprites
	"json_sprites": "src/vw_spr.json",

	# sounds
	"music_paths": {"bg": "src/melody.ogg",},
	"sfx_paths": {"click": "src/click.ogg",}
	}

display = gui.Scene(gui_info)
run, t = True, 0
while run:
	display.clear()

	# обработка клавиш
	key = display.getKey()
	if key: print(key)
	if key == "Esc": run = False

	t = display.update()
del display