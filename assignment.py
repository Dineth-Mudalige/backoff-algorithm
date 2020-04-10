#Getting the channel specifications using the transmission rate
def channel_specs(transmission_rate):
    """Transmission rate can be 10 and 100. The Mbps values. Accordingly, the IFG and slot time will be found"""
    result =[0,0]
    if transmission_rate==10:
        slot_time = 512*100e-9
        IFG = 9.6e-6
    else:
        slot_time = 512*10e-9
        IFG = 960e-9
    result[0]  = slot_time
    result[1] = IFG
    return result

#The time is set to test the algorithm. The channel is kept block during this time
def block_channel(time):
    channel_blocked = True
    return channel_blocked

import random
def transmit(transmission_rate,data_available,time):
    slot_time = channel_specs(transmission_rate)[0]
    IFG = channel_specs(transmission_rate)[1]
    channel_blocked = block_channel(time)
    total_time = IFG
    attempts = 0
    print("Waiting for the IGF...")#IGF is the ideal time before transmission
    while (data_available):
        if (total_time>=time):
            channel_blocked = False
        if (not channel_blocked):
            print("\nData transmitted. Total time taken {:.3e}".format(total_time))
            break
        else:
            if (channel_blocked):
                print("\nChannel blocked.\nTransmitting the CEJ")
                total_time += ((32e-6)/transmission_rate)
                while (attempts<16):
                    k = min(attempts,10)
                    r = random.randint(0,2**k-1)
                    delay = r*slot_time
                    attempts+=1
                    total_time+=delay
                    print("\nAttempt = %d\nk = %d\nr = %d\ndelay = %.3e\nTime Elapsed = %.3e"%(attempts,k,r,delay,total_time))
                    if (total_time>=time):
                        channel_blocked = False
                        attempts=0
                        break
                if (attempts == 16):
                    print("\nNumber of attempts exceeded 16. Transmission failed")
                    break
    if (not data_available):
        print("\nNo data available.\nTransmission failed")
                
def test(testcases):
    for count,i in enumerate(testcases,1):
        transmission_rate = i[0]
        data_available = i[1]
        time = i[2]
        print("\nTransmission rate = %d\nTest case = %d"%(transmission_rate,count))
        transmit(transmission_rate,data_available,time)

testcases = [[10,True,35e-6],[10,True,1e-9],[100,True,1],[100,True,650e-9],[10,False,2e-6],[100,True,5e-9]]
test(testcases)




