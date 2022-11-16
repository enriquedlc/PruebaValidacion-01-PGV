import time
import os
import datetime as dt

def main():
    # initialize "process" variable to 0. Inside the loop, in the else statement, it will be incremented by 1
    process = 0
    while process < 10:
        # the process is created
        pid = os.fork()
        if pid == 0:
            # if the process is a child (equal to 0), it will print the process number and the current time using the datetime module 
            print("Process created", os.getpid(), dt.datetime.now().strftime("%H:%M:%S"))
            # the process will sleep 3 seconds as requested and then it will finish
            time.sleep(3)
            print("Process finished con PID", os.getpid(), dt.datetime.now().strftime("%H:%M:%S"))
            os._exit(0)
        else:
            # if the process is a parent, it will wait for the child to finish
            # and then it will increment the process variable by 1
            process += 1
            time.sleep(10)

if __name__ == "__main__":
    main()
