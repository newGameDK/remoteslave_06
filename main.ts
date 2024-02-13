//  Clear after blinking
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    //  Show the arrow based on the received number using commandToArrow for correct mapping
    arrowDirection = commandToArrow[receivedNumber]
    radio.sendString("ACK")
    //  Start with a fast blink rate
    endTime = input.runningTime() + 5000
    //  Set end time for 5 seconds later
    //  Blink the received direction, slowing down over 5 seconds
    //  Ensure blink interval doesn't exceed 500ms
    while (input.runningTime() < endTime) {
        basic.showArrow(arrowDirection)
    }
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (!selected) {
        group = (group + 1) % letters.length
        showGroupLetter()
    }
    
})
function showGroupLetter() {
    basic.showString("" + letters[group])
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (!selected) {
        selected = true
        radio.setGroup(group + 1)
        basic.showString("G" + letters[group])
    }
    
})
let group = 0
let selected = false
let endTime = 0
let arrowDirection = 0
let commandToArrow : number[] = []
let letters : string[] = []
letters = ["A", "B", "C", "D", "E"]
radio.setTransmitPower(7)
//  This matches the Master's commandToArrow array
//  0: forward
//  1: backward
//  2: left
//  3: right
commandToArrow = [ArrowNames.North, ArrowNames.South, ArrowNames.West, ArrowNames.East]
showGroupLetter()
