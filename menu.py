
import subprocess
import os

running = True
state = 0


def printHeader():
    os.system('clear')
    print 'S N A K E\n'

def tutorial():
    global state

    if state == 0:
        printHeader()
        print '\nHi there! Welcome to Snake.'
        print 'Type snake to launch the game'
        success = False
        while not success:
            command = raw_input()
            if command == 'snake':
                print '\nUse the keys to move and Q to quit'
                subprocess.call("sleep 1", shell=True)
                print '3...'
                subprocess.call("sleep 1", shell=True)
                print '2...'
                subprocess.call("sleep 1", shell=True)
                print '1...'
                subprocess.call("sleep 1", shell=True)
                subprocess.call("python __main__.py", shell=True)
                success = True
                state += 1
            else:
                print 'Type snake to launch the game'

    elif state == 1:
        printHeader()
        print 'Great game. Now let\'s see what options are available.'
        print 'Type snake --help'
        success = False
        while not success:
            command = raw_input()
            if command == 'snake --help' or command == 'snake -h':
                subprocess.call("python . --help", shell=True)
                subprocess.call("sleep 1", shell=True)
                success = True
                state += 1
            else:
                print 'Type snake --help'

    elif state == 2:
        print '\n\nYou can try different themes for the game'
        print 'For example, type snake --theme minimal'
        print 'Or type snake --help to get a list of available themes and then snake --theme "name"'
        success = False
        while not success:
            command = raw_input()
            cmdArray = command.split(' ')
            if len(cmdArray) == 3 and \
                cmdArray[0] == 'snake --theme' and \
                cmdArray[1] == '--theme' or cmdArray[1] == '--t' and \
                cmdArray[2] == 'classic' or cmdArray[2] == 'minimal':
                command = "python . --theme " + cmdArray[2]
                subprocess.call(command, shell=True)
                success = True
                state += 1
            elif command == 'snake --help' or command == 'snake -h':
                success = False
            else:
                print 'Try typying snake --theme minimal'

def run():
    try:
        while running:
            tutorial()
    except KeyboardInterrupt:
        exit()

run()