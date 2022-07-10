import sys
import random
from time import sleep

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

def get_seq():
    """
    Obtiene la secuencia de ácido núcleico.
    """
    seq = input("Inserte la secuencia de ácidos nucleicos: ")
    seq = seq.upper().replace(" ", "")
    return seq

def arn_compl(seq):
    """
    Transcribe secuencia de ADN a ARNm
    """
    bases = {"A":"U", "T":"A", "G":"C", "C":"G"}
    arn_m = ""
    for i in seq:
        arn_m += bases[i]
    return arn_m

def arn_complp(seq):
    """
    Devuelve secuencia complementaria de ARNm
    """
    bases = {"A":"U", "U":"A", "G":"C", "C":"G"}
    arn_m = ""
    for i in seq:
        arn_m += bases[i]
    return arn_m

def transcripcion(seq):
    """
    Transcribe secuencia de ADN a ARNm
    """
    bases = {"A":"U", "T":"A", "G":"C", "C":"G"}
    arn_m = ""
    for i in seq:
        arn_m += bases[i]
    arn_m = arn_m[::-1]
    return arn_m

def trans_peso_DNA(seq):
    """
    Traduce secuencia de DNA y hallar peso de la proteína secuenciada.
    """
    gencode = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T',
                'ACG':'T', 'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
                'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R','CTA':'L', 'CTC':'L',
                'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
                'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
                'CGG':'R','CGT':'R','GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
                'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D',
                'GAA':'E','GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
                'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F',
                'TTA':'L','TTG':'L','TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
                'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

    AminoDict={'A':89.09,'R':174.20,'N':132.12,'D':133.10,'C':121.15,'Q':146.15,
            'E':147.13,'G':75.07,'H':155.16,'I':131.17,'L':131.17,'K':146.19,
            'M':149.21,'F':165.19,'P':115.13,'S':105.09,'T':119.12,'W':204.23,
            'Y':181.19,'V':117.15}

    protein = ""
    peso = 0

    for i in range(0, len(seq), 3):
        if len(seq[i:i+3]) == 3:
            protein += gencode[seq[i:i+3]]
            if gencode[seq[i:i+3]] != '_':
                peso += AminoDict.get(gencode[seq[i:i+3]])
            else:
                break

    peso = round(peso, 2)

    print("Proteína secuenciada: " + str(protein))
    print("Peso: " + str(peso))

def trans_peso_RNA(arn_mr):
    """
    Traduce secuencia de DNA y hallar peso de la proteína secuenciada.
    """
    gencode = {'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 'ACA':'T', 'ACC':'T',
                'ACG':'T', 'ACU':'T','AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
                'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R','CUA':'L', 'CUC':'L',
                'CUG':'L', 'CUU':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
                'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
                'CGG':'R','CGU':'R','GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
                'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A','GAC':'D', 'GAU':'D',
                'GAA':'E','GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
                'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S','UUC':'F', 'UUU':'F',
                'UUA':'L','UUG':'L','UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
                'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}

    AminoDict={'A':89.09,'R':174.20,'N':132.12,'D':133.10,'C':121.15,'Q':146.15,
            'E':147.13,'G':75.07,'H':155.16,'I':131.17,'L':131.17,'K':146.19,
            'M':149.21,'F':165.19,'P':115.13,'S':105.09,'T':119.12,'W':204.23,
            'Y':181.19,'V':117.15}

    protein = ""
    peso = 0

    for i in range(0, len(arn_mr), 3):
        if len(arn_mr[i:i+3]) == 3:
            protein += gencode[arn_mr[i:i+3]]
            if gencode[arn_mr[i:i+3]] != '_':
                peso += AminoDict.get(gencode[arn_mr[i:i+3]])
            else:
                break

    peso = round(peso, 2)

    print("Proteína secuenciada: " + str(protein))
    print("Peso: " + str(peso))

colors = {"A":"1;37;41", "C":"1;37;42", "G":"1;37;43", "T":"1;37;45", "U":"1;37;45"}

while True:
    seq = get_seq()
    if seq.lower() == "q":
        break
    print("Secuencia DNA:\t", "3'", seq ,"5'")
    arn_m = arn_compl(seq)
    n_seq = ""
    for i in seq:
        n_seq += "\x1b["+ colors[i] + "m" + i + "\x1b[0m"

    print("Secuencia DNA:\t", "3'", n_seq ,"5'")
    messages = ""

    for i in range(len(arn_m)):

        message = "\x1b["+ colors[arn_m[i]] + "m" + arn_m[i] + "\x1b[0m"
        messages += message
        prompt = messages + "_"*(len(arn_m)-i-1)
        fprompt = "\rSecuencia RNAm:\t 5' " + prompt + " 3'"
        print(fprompt, end="\r")
        sleep(0.05)

    arn_mrc = ""
    arn_mr = transcripcion(seq)
    arn_mrrev = arn_complp(arn_mr)
    for i in transcripcion(seq):
        arn_mrc += "\x1b["+ colors[i] + "m" + i + "\x1b[0m"
    print("\nSecuencia RNAm:\t", "3'", arn_mrc ,"5'")
    print("Secuencia RNAm:\t", "3'", transcripcion(seq) ,"5'")

    print("\n")

    #Random stuff
    gencode = {'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 'ACA':'T', 'ACC':'T',
                'ACG':'T', 'ACU':'T','AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
                'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R','CUA':'L', 'CUC':'L',
                'CUG':'L', 'CUU':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
                'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
                'CGG':'R','CGU':'R','GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
                'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A','GAC':'D', 'GAU':'D',
                'GAA':'E','GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
                'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S','UUC':'F', 'UUU':'F',
                'UUA':'L','UUG':'L','UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
                'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}

    bases = {"A":"U", "U":"A", "G":"C", "C":"G"}

    combinaciones = list(gencode.keys())
    UP = "\x1B[4A"
    CTRL = "\x1B[0K"

    anticodon = ""
    aminoacid = ""
    protein = ""

    #Highlighting Codones
    for i in range(0, len(arn_mr), 3):
        if len(arn_mr[i:i+3]) == 3:
            message = "\x1b["+ "2;30;47" + "m" + arn_mr[i:i+3] + "\x1b[0m"
            novo = arn_mr[:]
            novo = list(novo)
            for a in range(3):
                novo.pop(i)
            novo.insert(i, message)
            novo = ''.join(novo)
            prompt = "Secuencia RNAm:\t" + " 3' " + novo + " 5'"

            spaces = " "*len(anticodon)
            while True:
                e = random.randint(0, (len(combinaciones)-1))
                anticodon = spaces + combinaciones[e]
                aminoacid = spaces + " " + gencode[arn_complp(anticodon.strip())]
                msg = "Anticodon:     \t    "
                msg_amin = "Aminoácido:\t    "
                msg_prot = "Proteína:\t    "
                allstuff = "".join([UP, prompt, CTRL, "\n", msg, anticodon,
                            CTRL, "\n", msg_amin, aminoacid, CTRL, "\n",
                            msg_prot])
                print(allstuff)
                if arn_mrrev[i:i+3] == combinaciones[e]:
                    aminoacid = spaces + " " + gencode[arn_mr[i:i+3]]
                    protein += aminoacid.strip()
                    print(allstuff + protein)
                    break
                sleep(0.001)


    print("\n")
