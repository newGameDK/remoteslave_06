# Clear after blinking

def on_received_number(receivedNumber):
    global arrowDirection, endTime
    # Show the arrow based on the received number using commandToArrow for correct mapping
    arrowDirection = commandToArrow[receivedNumber]
    radio.send_string("ACK")
    # Start with a fast blink rate
    endTime = input.running_time() + 5000
    # Set end time for 5 seconds later
    # Blink the received direction, slowing down over 5 seconds
    # Ensure blink interval doesn't exceed 500ms
    while input.running_time() < endTime:
        basic.show_arrow(arrowDirection)
    basic.clear_screen()
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global group
    if not (selected):
        group = (group + 1) % len(letters)
        showGroupLetter()
input.on_button_pressed(Button.A, on_button_pressed_a)

def showGroupLetter():
    basic.show_string("" + (letters[group]))

def on_button_pressed_b():
    global selected
    if not (selected):
        selected = True
        radio.set_group(group + 1)
        basic.show_string("G" + letters[group])
input.on_button_pressed(Button.B, on_button_pressed_b)

group = 0
selected = False
endTime = 0
arrowDirection = 0
commandToArrow: List[number] = []
letters: List[str] = []
letters = ["A", "B", "C", "D", "E"]
radio.set_transmit_power(7)
# This matches the Master's commandToArrow array
# 0: forward
# 1: backward
# 2: left
# 3: right
commandToArrow = [ArrowNames.NORTH,
    ArrowNames.SOUTH,
    ArrowNames.WEST,
    ArrowNames.EAST]
showGroupLetter()