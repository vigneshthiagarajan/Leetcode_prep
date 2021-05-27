class Solution:
    def maximumTime(self, time: str) -> str:

        # Handle hours
        # if first two values are "?"
        if (time[0] == "?" and time[1] == "?"):
            time = time.replace("?", "2", 1)
            time = time.replace("?", "3", 1)
        # if units greater than 3 in HH: tens will be one
        elif (time[0] == "?"):
            if (time[1] > "3"):
                time = time.replace("?", "1", 1)
            else:
                time = time.replace("?", "2", 1)
        elif (time[1] == "?"):
            if (time[0] == "2"):
                time = time.replace("?", "3", 1)
            else:
                time = time.replace("?", "9", 1)

        # Handle minutes
        if (time[3] == "?" and time[4] == "?"):
            time = time.replace("?", "5", 1)
            time = time.replace("?", "9", 1)
        elif (time[3] == "?"):
            time = time.replace("?", "5", 1)
        elif (time[4] == "?"):
            time = time.replace("?", "9", 1)

        return time

    # # if hour 10's aand Units value is "?"
    #     if time[0]=="?" and time[1]=="?":
    #                 time = time.replace("?", "2", 1)
    #                 time = time.replace("?", "3", 1)
    #     # If hour units value greater than 3, hour tens value will be 1 else 2
    #     if time[0]=="?" :
    #             if time[1]>"3":
    #                     time=time.replace("?","1",1)
    #             else:
    #                     time = time.replace("?", "2", 1)
    #     # if hour 10's value is 0 or 1
    #     if time[0]=="1" or time[0]=="0":
    #             if time[1]=="?":
    #                     time = time.replace("?", "9", 1)
    #     # if hour 10's value is 2
    #     if time[0] == "2":
    #             if time[1] == "?":
    #                     time = time.replace("?", "3", 1)
    #     # if minute 10's and units value is ?
    #     if time[3]=="?":
    #             time = time.replace("?", "5", 1)
    #     if time[4]=="?":
    #             time = time.replace("?", "9", 1)
    #     return(time)
