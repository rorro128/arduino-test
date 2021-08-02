from pyfirmata2 import Arduino

DELAY = 1
PORT = Arduino.AUTODETECT

board = Arduino(PORT)
#board.samplingOn(100)
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()

while True:
    print(board.analog[0].read(), board.analog[1].read())
    board.pass_time(1)

