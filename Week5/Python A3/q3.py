# input a string
# validate the string as AGCT

from unittest import result


dna = input("Enter DNA string ")


def validate(dna):
    for i in dna:
        if i == "A" or i == "T" or i == "C" or i == "G":
            continue
        else:
            return(print("DNA string isn't valid"))


validate(dna)

# reverse the string


def reverse(dna):
    revstring = ""
    for i in range(len(dna)-1, -1, -1):
        revstring = revstring+dna[i]
    return(revstring)


revtring = reverse(dna)

# complement

print(revtring)


def complement(revtring):
    result = ""
    for i in range(len(revtring)):
        if revtring[i] == "A":
            result = result+"T"
        elif revtring[i] == "T":
            result = result+"A"
        elif revtring[i] == "C":
            result = result+"G"
        elif revtring[i] == "G":
            result = result+"C"
    return(print(result))


complement(revtring)
