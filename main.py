import sys

#Idee d'algorithme:
# on regarde le i bit et on compte le nombre de 1 dans les devices
# a cette position et le nombre de 1 dans les outlets a cette position.
# si nombre_1_device == nombre_1_outlet, on ne fait pas de switch
# sinon si nombre_1_device == N-nombre_1_outlet, on fait un switch
# verifier le cas limite ou nombre_1_device * 2 = N
# (les deux configurations seraient donc valide pour ce bit)
# apres avoir essayer toute les permutations, on peut declarer
# le probleme impossible

# Faire un tableau des versions valides(avec switch ou sans switch)
# pour chaque des bits
# ensuite permutation avec itertools faire toute sortir les possibilite
# on utilise checkfit pour verifier que cela marche
# aussi il faut favoriser quand on ne fait pas beaucoup de switch

# Verifie si device et outlet sont pareil
def checkfit(device,outlet):
    return sorted(device) == sorted(outlet)

# Counter le nombre de 1 total a la position i
def countOneAtPos(devices, i):
    return sum(map(lambda x: int(x[i]),devices))

#Fonction pour resoudre un cas
# case = (N,L,[device],[outlet])
# il reste a trouver l'algorithme pour determiner le nombre de switch a toggleler
def solve(case):
    N,L,device,outlet = case

    #Cas ou il n'y a pas de changement a faire
    if checkfit(device,outlet):
        return 0

    #Trouve les cas impossibles simples
    
    cpt = 0
    for i in range(L):
        d = countOneAtPos(device, i)
        o = countOneAtPos(outlet, i)
        
        if d != o and d != (N-o):
            return None

    
    #Pas supposer arrive la 
    return -1

def readfile(filename):
    with open(filename) as f:
        t = int(f.readline())
        cases = []
        for i in range(t):
            n, l = f.readline().split()
            n = int(n)
            l = int(l)
            device = f.readline().split()
            outlet = f.readline().split()
            cases.append((n,l,device,outlet))
        return cases

def writeresult(filename, solved):
    with open(filename + ".res",'w') as f:
        for i in range(len(solved)):
            f.write("Case #")
            f.write(str(i+1))
            f.write(": ")
            s = "NOT POSSIBLE"
            if solved[i] != None:
                s = str(solved[i])
            f.write(s)
            f.write("\n")

def main():
    filename = ""
    if len(sys.argv) == 1:
        filename = "sample.txt"
    else:
        filename = sys.argv[1]

    cases = readfile(filename)

    solved = map(solve, cases)

    writeresult(filename, solved)


if __name__ == "__main__":
    main()
