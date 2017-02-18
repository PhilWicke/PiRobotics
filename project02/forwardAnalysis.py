import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
import controls as ct


running_time = 10

'''
Every 34th forwards step is being replace by a turnLeft
This results in an almost straight forward driving with 2m in 10sec
'''

# 195cm
# 190cm
# 211cm
# 193cm
# 200cm

def key_input(event):
    counter = 1
    offStep = 34
    ct.init()
    #print 'Key:', event.char
    key_press = event.char
    sleep_time = 0.030

    # Define keys
    if key_press.lower() == 'w':
        t0    = time.time()
        t_end = t0 + running_time
        
        while time.time() < t_end:
            ct.init()
            if counter % offStep == 0:
                ct.turnLeft(sleep_time)
            else:
                ct.forward(sleep_time)    
            sys.stdout.write("\rTime elapsed: %.2f" % round(time.time()-t0,2))
            sys.stdout.flush()
            counter = counter + 1
    else:
        time.sleep(sleep_time)
        
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
