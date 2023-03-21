# citire
import copy
f = open("input.in", 'r')
date_intrare = f.read().split('\n')
f.close()

# construire dict automat ?? yey

automat = {}
starifinale = []
cuvinte = []
cititstare = False

for linie in date_intrare:
    linie = linie.split()
    if len(linie) > 2:
        if tuple([linie[0], linie[1]]) not in automat:
            automat[tuple([linie[0], linie[1]])] = [linie[2]]
        else:
            automat[tuple([linie[0], linie[1]])].append(linie[2])
    try:
        if linie[1][0] == 'q' or (len(linie) == 1):
            for stare_finala in linie:
                starifinale.append(stare_finala)
                cititstare = True
    except:
        if len(linie) == 1:
            if cititstare == False:
                starifinale.append(linie[0])
                cititstare = True
            else:
                cuvinte.append(linie[0])


# ce bag in stari     [stare actuala, cuvant actual, traseu pana acum]
for cuvant in cuvinte:
    Q = [['q0', cuvant, []]]

    solutie = False

    while len(Q) > 0:
        if len(Q[0][1]) > 0:
            if tuple([Q[0][0], Q[0][1][0]]) in automat:
                for el in automat[tuple([Q[0][0], Q[0][1][0]])]:
                    new_element = [el, Q[0][1][1:], copy.deepcopy(Q[0][2])]
                    new_element[2].append(Q[0][0])
                    Q.append(new_element)
                Q.pop(0)
            else:
                Q.pop(0)

        else:
            if Q[0][0] in starifinale:
                Q[0][2].append(Q[0][0])
                print(Q[0][2])
                solutie = True
                break
            else:
                Q.pop(0)

    if solutie == False:
        print("Rejected")
