#----------------------------------------------
# Elementary one-dimensional cellular automata
# Author: Pablo Villanueva-Domingo
# Last modification: 6/2022
#---------------------------------------------

#---------------------------------------------
# Binary cellular automata (CA) which update the value of each cell based on its neighborhood, following a binary rule
# These CA were first studied and classified by Stephen Wolfram
# A cell is updated depending on its value and that of its 2 neighbors, there are 2^3 possible binary states for the neighborhood, leading to 2^8=256 possible CA
# Hence, the rules 0-255 defines the possible CA, which encode the update procedure through its binary value
# For more info, see https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
#---------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Set the size of the grid
size = 200
# Set the number of iterations to run the CA
epochs = 100

# Transform the name of the rule to a binary number
def ruletobin(rule):
    # Convert to string of binary values
    binario = str(bin(rule))
    # Remove two first characters, which indicate that the number is binary
    binario = binario[2:]
    # Insert 0s at the beginning to have a size 8 digits number
    binario = binario.zfill(8)
    return binario

# Apply the binary update rule
def apply_rule(neighbors, binrule):
    # Convert neighborhood list to string
    neighbors = ''.join(str(x) for x in neighbors)
    # Convert neighborhood to binary digits
    bin_to_dec = int(neighbors,2)
    # Apply rule based on digit position in the binary encoding
    newstate = binrule[bin_to_dec]
    return newstate

#--- MAIN ---#

if __name__=="__main__":

    # Choose the rules
    rules = [30,126,145]

    # Create figure, with as many axes as rules
    fig, axs = plt.subplots(len(rules), 1, figsize=(2.*size//100, 2.*len(rules)), constrained_layout=True)

    # Loop for each rule
    for j, ax in enumerate(axs):

        rule = rules[j]
        binrule = ruletobin(rule)
        print("Rule",rule, "- Binary encoding:", binrule)

        # Initialize randomly the first line
        line = np.random.randint(2, size=size)
        lines = [line]

        # Start loop over epochs
        for n in range(epochs):
            newline = np.zeros(len(line), dtype=int)

            # Apply update rule for every cell (except boundaries)
            for i in range(1,size-1):
                neighbors = list(line[i-1:i+2])
                newline[i] = apply_rule(neighbors, binrule)

            # Update boundaries using boundary conditions
            neighbors = list(np.append([line[-1]], line[:2]))
            newline[0] = apply_rule(neighbors, binrule)
            neighbors = list(np.append(line[-2:], [line[0]]))
            newline[-1] = apply_rule(neighbors, binrule)

            # Update line
            line = newline
            lines.append(newline)

        # Plot
        ax.set_title("Rule "+str(rule))
        ax.imshow(lines)
        ax.axis('off')


    plt.savefig("CA.png", dpi=fig.dpi)
    plt.show()
