from tank import Tank
tanks = {"a":Tank("Alice"), "b":Tank("Bob"), "c":Tank("Carol")}
# experimenting with manually creating a new tank 'f'
f = Tank("Fred")
# adding the new manual tank to the dictionary of tanks
tanks['f'] = f

alive_tanks = len(tanks)
while alive_tanks > 1:
    print
    for tank_name in sorted(tanks.keys()):
        print tank_name, tanks[tank_name]
        
    first = raw_input("Who fires? ").lower()
    second = raw_input("Who at? ").lower()
    
    if first == second:
        print "Can't fire at yourself!"
        continue

    
    try:
        first_tank = tanks[first]
        second_tank = tanks[second]
    except KeyError, name:
        print "No such tank! ",name
        continue
    
    if not first_tank.alive or not second_tank.alive:
        print "One of those tanks is dead!"
        continue
    
    print
    
    print "*" * 30
    
    first_tank.fire_at(second_tank)
    if not second_tank.alive:
        alive_tanks -=1
        
    print "*" * 30
    
for tank in tanks.values():
    if tank.alive:
        print tank.name, "is the winner!"
        break

print "The game has ended"