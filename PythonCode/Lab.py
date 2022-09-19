import random  # perfect way(using randomization)

location = ['A', 'B']
status = ['Clean', 'Dirty']

percepts = []  # bool list

table = {('A', 'Clean'): 'Right',
         ('B', 'Dirty'): 'Suck',
         ('B', 'Clean'): 'Left',
         ('A', 'Dirty'): 'Suck'  # database
         }

def table_agent(percept):
    action = True
    percepts.append(percept)  # appending new data #(Sending  to the list)
    print("Complete History: ", percepts)

    if (action == True):
        print(table[percept])

    else:
        print("No Action")  # lookup table_agent(percept)


for _ in range(3):
    l = random.choice(location)  # Choose the data randomly
    s = random.choice(status)  # Choose status randomly

    percept = (l, s)
    table_agent(percept)  # method declare


def reflex_vaccume_agent(location, status):
    location = random.choice(location)
    status = random.choice(status)

    if status == 'Dirty':
        return "Suck"
    elif location == 'A':
        return "Right"
    elif location == 'B':
        return "Left"


print(reflex_vaccume_agent(location, status))


def model_base_reflex_agent(percepts):
    detect_loc = random.choice(location)
    detect_stat = random.choice(status)

    det = {
        detect_loc: detect_stat
    }
    if (det[detect_loc] == 'Clean'):
        percepts.append(True)
    else:
        percepts.append(False)

    action1 = "Already Clean"
    action2 = "Don't Clean"
    if percept is True:
        return action2
    else:
        return action1


print(model_base_reflex_agent(percepts))
