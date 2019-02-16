global offset

if starting:
  	offset = [-0.2, -0.4, -0.4] # offset for second controller
	alvr.two_controllers = True

# passthroughs for Oculus Go controller
alvr.buttons[0][alvr.Id("trackpad_click")] = alvr.input_buttons[alvr.InputId("trackpad_click")]
alvr.buttons[0][alvr.Id("trackpad_touch")] = alvr.input_buttons[alvr.InputId("trackpad_touch")]
alvr.buttons[0][alvr.Id("application_menu")] = alvr.input_buttons[alvr.InputId("back")]
alvr.buttons[0][alvr.Id("trigger")] = alvr.input_buttons[alvr.InputId("trigger")]
alvr.trigger[0] = 1.0 if alvr.buttons[0][alvr.Id("trigger")] else 0.0

alvr.trackpad[0][0] = alvr.input_trackpad[0]
alvr.trackpad[0][1] = alvr.input_trackpad[1]

# set static position for second controller
alvr.controller_position[1][0] = offset[0]
alvr.controller_position[1][1] = offset[1]
alvr.controller_position[1][2] = offset[2]

# custom mappings of freepie's wiimote input to our second ALVR controller
map = [["application_menu", WiimoteButtons.Plus],
       ["trigger", WiimoteButtons.B],
       ["a", WiimoteButtons.A],
       ["grip", WiimoteButtons.Two],
       ["back", WiimoteButtons.Minus],
       ["start", WiimoteButtons.Home],
       ["dpad_left", WiimoteButtons.DPadLeft],
       ["dpad_up", WiimoteButtons.DPadUp],
       ["dpad_right", WiimoteButtons.DPadRight],
       ["dpad_down", WiimoteButtons.DPadDown]]

for k in map:
	alvr.buttons[1][alvr.Id(k[0])] = wiimote[0].buttons.button_down(k[1])
	diagnostics.watch(wiimote[0].buttons.button_down(k[1]))

# substituting trackpad on Vive wand for wiimote's (4-way) dpad
if wiimote[0].buttons.button_down(WiimoteButtons.DPadLeft):
	alvr.trackpad[1][0] = -0.8
	alvr.trackpad[1][1] = 0
	alvr.buttons[1][alvr.Id("trackpad_click")] = True
elif wiimote[0].buttons.button_down(WiimoteButtons.DPadRight):
	alvr.trackpad[1][0] = 0.8
	alvr.trackpad[1][1] = 0
	alvr.buttons[1][alvr.Id("trackpad_click")] = True
elif wiimote[0].buttons.button_down(WiimoteButtons.DPadUp):
	alvr.trackpad[1][0] = 0
	alvr.trackpad[1][1] = 0.8
	alvr.buttons[1][alvr.Id("trackpad_click")] = True
elif wiimote[0].buttons.button_down(WiimoteButtons.DPadDown):
	alvr.trackpad[1][0] = 0
	alvr.trackpad[1][1] = -0.8
	alvr.buttons[1][alvr.Id("trackpad_click")] = True
else:
	alvr.trackpad[1][0] = 0
	alvr.trackpad[1][1] = 0
	alvr.buttons[1][alvr.Id("trackpad_click")] = False