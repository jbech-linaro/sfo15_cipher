#!/usr/bin/python

def gen_letter_dict():
    d = {}
    for i in range (65, 92):
        d[i - ord("A")] = chr(i)
    return d

def main():
    d = gen_letter_dict()
    #print d

    key = "VZDDNWGOCTCZYQBIVIYGCEFVRPMLQSURCEJNOZZDXLPLPMAYRRBCIYSVPQGIHBIFRQQJHPZRZEZIUFERSGQHREQUIAJFMLOOPCVFBWMRMMXB"
    cipher = "DEBRHJUKIHVNPUHQNBPGVMTINXFSQHCVEIXSDZOHOHXEWKOSIEBOMYFYIXOAJPUUCUJNTTRJZKDGIZAZDRRLVRJYZEMNZECHWGKWJVQUDMTA"

    plain_text = ""
    for i in range(0, len(key)):
        k = d[ord(key[i]) - ord("A")]
        c = d[ord(cipher[i]) - ord("A")]
        p = d[(ord(c) - ord(k)) % 26]
        #print (k, c, p)
        plain_text += p

    print plain_text
        
if __name__ == "__main__":
    main()
