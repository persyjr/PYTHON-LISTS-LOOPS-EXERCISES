parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(listin):
  total_slots=len(listin)*len(listin)
  available_slots=0
  occupied_slots=0
  state={}
  for i in listin:
    tempfilas=i
    for i in tempfilas:
      if i==2:
        available_slots=available_slots+1
      if i==1:
        occupied_slots=occupied_slots+1
  
    state["total_slots"]=total_slots
    state["available_slots"]=available_slots
    state["occupied_slots"]=occupied_slots
  return(state)
    

result= get_parking_lot(parking_state)
print(result)