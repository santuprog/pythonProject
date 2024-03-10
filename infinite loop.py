import time
while True:
    try :
        print('Loop Processing .....')
        print('use ctrl+c to break')
        time.sleep(1)
    except KeyboardInterrupt :
        print('user interrupted the loop ....... exiting .....')
        break

        #ctrl+c does not work