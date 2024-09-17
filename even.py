import numpy as np
def updateflight(fno,flights):
    c=0
    for x in flights:
        if(flights[c][0]==fno):
            flights[c][4]-=1
        c+=1    
    return flights
def reservation(pid,passengerr):
    c=0
    for x in passengerr:
        if(passengerr[c][0]==pid):
            print(passenger[c][2])
        c+=1
def fullybooked(flights):
    c=0
    for x in flights:
        if(flights[c][4]==0):
            print(flights[c][0])
            
            
flight=[[1,'t3','t5',2105,50],[2 ,'t3','t4',2010,0], [3,'t1','t8',2210,5]]
flight_schedule=np.array(flight)

passenger=[[200 ,'ansh',[2,'31f']],[201, 'purav',[3,'12d']],[202, 'yatharth',[2,'40a']]]
passenger_record=np.array(passenger)

reservation(200,passenger)
updateflight(3,flight)
fullybooked(flight)
