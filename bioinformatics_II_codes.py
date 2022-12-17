# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:30:16 2022

@author: AAND0774
"""
"""
def MotifEnumeration(list,k,d):
    patterns=[]
    for i in range(0,len(list[0])-k):
"""        
"""
def EulerianCycle(dict):
    path=[]
    banned_init_key=[]
    while len(path)!=len(dict):
        for key in dict:
            if len(path)==0 and key in banned_init_key:
                continue
            else:
                if len(path)==0 or path[-1]==key:
                    print(key)
                    init_len=len(path)
                    for i in dict[key]:
                        if i not in path:
                            path.append(i)
                            break
                    print(path)
                    print(banned_init_key)
                    if init_len==len(path):
                        if path[0] not in banned_init_key:
                            banned_init_key.append(path[0])
                        path=[]
    return path
"""

##### string composition problem #####
def Kcomposition(text,d):
    output=[]
    for i in range(0,len(text)-d+1):
        output.append(text[i:i+d])
    return output

"""
def genconstruct(list,d):
    proces="running"
    genome_size=0
    for i in list:
        genome_size+=len(i)-d
    while proces=="running":
        genome=""
        for i in list:
            if len(i)<d:
                break
            for y in list:
                if i[-d:len(i)]==y[0:d]:
"""                    
            
def GraphOverlap(list,d):
    output={}
    for i in list: 
        output[i]=[]
        for y in list:
            if i[-d:len(i)]==y[0:d]:
                output[i].append(y)
    remove_key=[]
    for key in output:
        if len(output[key])==0:
            remove_key.append(key)
    for x in remove_key:
        del output[x]
    return output

"""
def DeBruijn(text,d):
    output={}
    for i in range(0,len(text)-d+1):
        if text[i:i+d] not in output:
            output[text[i:i+d]]=[]
        for y in range(0,len(text)-d+1):
            if text[i:i+d]==text[y:y+d]:
                output[i].append(text[y:y+d])
    return output
"""
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

def unique(list):
    result=[]
    for i in list:
        if i not in result:
            result.append(i)
    return result

def lowest(int1,int2):
    if int1<int2:
        return int1
    elif int1>int2:
        return int2
    elif int1==int2:
        return int1

def N50(input):
    result=[]
    maks=0
    if type(input)==list and type(input[0])==str:
        for i in input:
            maks+=len(i)
    elif type(input)==list and type(input[0])==int:
        for i in input:
            maks+=i
    input=sorted(input)
    count=0        
    if type(input)==list and type(input[0])==str:
        for i in input:
            count+=len(i)
            if count>=maks/2:
                result.append(len(i))
    elif type(input)==list and type(input[0])==int:
        for i in input:
            count+=i
            if count>=maks/2:
                result.append(i)
    result.sort()
    return len(result[0])

def NX(input,X):
    if type(X)==int and X not in [0,1]:
        X=X/100
    result=[]
    maks=0
    if type(input)==list and type(input[0])==str:
        for i in input:
            maks+=len(i)
    elif type(input)==list and type(input[0])==int:
        for i in input:
            maks+=i        
    count=0
    if type(input)==list and type(input[0])==str:
        for i in input:
            count+=len(i)
            if count>=maks*X:
                result.append(len(i))
    elif type(input)==list and type(input[0])==int:
        for i in input:
            count+=i
            if count>=maks*X:
                result.append(i)
    result.sort()
    return len(result[0])

def NG50(list,genomesize):
    contigSizes=[]
    if type(list[0])==str:
        for n in list:
            contigSizes.append(len(n))
        contigSizes=sorted(contigSizes,reverse=True)
    elif type(list[0])==int:
        contigSizes=sorted(list,reverse=True)

    contigSum=0
    result=0
    for i in contigSizes:
        contigSum+=i
        if contigSum>=genomesize/2:
            result=i
            break
    return result

def NGA50(genome,contig):
    contig_break_ups=[]
    new_contig=""
    for i in range(len(contig)):
        new_contig+=contig[i]
        if new_contig not in genome:
            contig_break_ups.append(new_contig[0:-1])
            new_contig=contig[i]
        elif i==len(contig)-1:
            contig_break_ups.append(new_contig)
    return contig_break_ups


#def PairedCompose(dict,k,d):
#    for key1 in dict:
#        process="processing " + key1
#        while process=="processing " + key1:
#            for key2 in dict:
#                if key2!=key1 and key1[1:3]==key2[0:2] and dict[key1][1:3]==dict[key2][0:2]:
                    
def translation(string,start="RNA",letters=1):
    # makes the correct transcription before translating
    if start=="DNA" or "T" in string.upper():
        new_string=""
        for i in string:
            if string[i].upper()=="A":
                new_string+="U"
                
            elif string[i].upper()=="T":
                new_string+="A"
            
            elif string[i].upper()=="G":
                new_string+="C"
            
            elif string[i].upper()=="C":
                new_string+="G"
        string=new_string[::-1]
    
    # define the translation library
    trans_lib={"AGG":["R","Arg"],
               "AGA":["R","Arg"],
               "AGC":["S","Ser"],
               "AGU":["S","Ser"],
               "AAG":["K","Lys"],
               "AAA":["K","Lys"],
               "AAC":["N","Asn"],
               "AAU":["N","Asn"],
               "ACG":["T","Thr"],
               "ACA":["T","Thr"],
               "ACC":["T","Thr"],
               "ACU":["T","Thr"],
               "AUG":["M","Met"],
               "AUA":["I","Ile"],
               "AUC":["I","Ile"],
               "AUU":["I","Ile"],
               "CGG":["R","Arg"],
               "CGA":["R","Arg"],
               "CGC":["R","Arg"],
               "CGU":["R","Arg"],
               "CAG":["Q","Gln"],
               "CAA":["Q","Gln"],
               "CAC":["H","His"],
               "CAU":["H","His"],
               "CCG":["P","Pro"],
               "CCA":["P","Pro"],
               "CCC":["P","Pro"],
               "CCU":["P","Pro"],
               "CUG":["L","Leu"],
               "CUA":["L","Leu"],
               "CUC":["L","Leu"],
               "CUU":["L","Leu"],
               "GGG":["G","Gly"],
               "GGA":["G","Gly"],
               "GGC":["G","Gly"],
               "GGU":["G","Gly"],
               "GAG":["E","Glu"],
               "GAA":["E","Glu"],
               "GAC":["D","Asp"],
               "GAU":["D","Asp"],
               "GCG":["A","Ala"],
               "GCA":["A","Ala"],
               "GCC":["A","Ala"],
               "GCU":["A","Ala"],
               "GUG":["V","Val"],
               "GUA":["V","Val"],
               "GUC":["V","Val"],
               "GUU":["V","Val"],
               "UGG":["W","Trp"],
               "UGC":["C","Cys"],
               "UGU":["C","Cys"],
               "UAC":["Y","Tyr"],
               "UAU":["Y","Tyr"],
               "UCG":["S","Ser"],
               "UCA":["S","Ser"],
               "UCC":["S","Ser"],
               "UCU":["S","Ser"],
               "UUG":["L","Leu"],
               "UUA":["L","Leu"],
               "UUC":["F","Phe"],
               "UUU":["F","Phe"]}
    result=""
    for i in range(0,len(string),3):        
        codon=string[i:i+3]
        if len(codon)==3 and codon in list(trans_lib.keys()):
            if letters==1:
                result+=trans_lib[codon][0]
            elif letters==3:
                result+=trans_lib[codon][0] + "-"
        else:
            break
    if letters==3:
        result=result[:-1]
    return result
        
def Cyclo(text,list,we_want="T/F"):
    mass={"A":71,"C":103,"D":115,"E":129,
          "F":147,"G":57,"H":137,"I":113,
          "K":128,"L":113,"M":131,"N":114,
          "P":97,"Q":128,"R":156,"S":87,
          "T":101,"V":99,"W":186,"Y":163,"":0}
    
    # make the various (cyclical) combinations of the string
    variations=[text]
    count=len(text)
    while count!=0:
        for i in range(len(text)):
            #print(i)
            temp=text.replace(text[i],"",1)
            if temp in text:
                variations.append(temp)
                for j in range(len(temp)):
                    temp2=temp.replace(temp[j],"",1)
                    if temp2 in text:
                        variations.append(temp2)
                    elif text[0] in temp and text[-1] in temp:
                        variations.append(temp2)
            elif text[0] in temp and text[-1] in temp:
                variations.append(temp2)

            variations.append(text[i])
            count-=1
    variations.append("")
    if we_want=="peptides":
        return variations
    
    # make the actual spectrum based on the input string
    spectrum=[]
    for x in variations:
        count=0
        for i in range(len(x)):
            count+=mass[x[i]]
        spectrum.append(count)
    spectrum.sort()
    if we_want=="spectrum":
        return  spectrum
    
    
    ## scoring
    if we_want=="score":
        return len(set(list) & set(spectrum))
    
    # compare the actual spectrum with the theoretical spectrum
    elif we_want=="T/F": 
        for x in spectrum:
            if x not in list:
                return False
                break
        return True

def linear(list):
    spec=[""]
    mass={"A":71,"C":103,"D":115,"E":129,
          "F":147,"G":57,"H":137,"I":113,
          "K":128,"L":113,"M":131,"N":114,
          "P":97,"Q":128,"R":156,"S":87,
          "T":101,"V":99,"W":186,"Y":163,"":0}    
    for key in mass:
        if mass[key] in list:
            spec.append(key)
    for x in spec:
        for key in mass:
            temp=x+key
            if pMW(temp) in list:
                spec.append(temp)
        if max(pMW(spec))>=max(list):
            break
    spec_mass=pMW(spec)
    
    mass_check=False
    for x in spec_mass:
        if x in list:
            mass_check=True      
    if mass_check==False:
        return False
    else:
        result=[""]
        for x in spec:
            if x!="":
                if Cyclo(x, list):
                    result.append(pMW(x))
        return len(set(list) & set(result))

def specfix(text):
    text=text.split(" ")
    result=[]
    for i in text:
        result.append(int(i))
    return result
    
def pMW(text):
    mass={"A":71,"C":103,"D":115,"E":129,
          "F":147,"G":57,"H":137,"I":113,
          "K":128,"L":113,"M":131,"N":114,
          "P":97,"Q":128,"R":156,"S":87,
          "T":101,"V":99,"W":186,"Y":163,"":0}
    count=0
    if type(text)==str:
        for i in range(len(text)):
            count+=mass[text[i].upper()]
        return count
    elif type(text)==list:
        result=[count]
        for x in text:
            count=0
            for i in range(len(x)):
                if x[i]!="":
                    count+=mass[x[i].upper()]
            result.append(count)
        return result


def specCon(spectrum):
    spectrum.sort()
    result=[]
    for i in spectrum:
        if i!=0:
            for j in spectrum:
                if i>j:
                    number=i-j
                    if number!=0:
                        result.append(number)
    return result

def DNA_AA_prop(text):
    AA_prop={'R': 6,'S': 6,'K': 2,'N': 2,
             'T': 4,'M': 1,'I': 3,'Q': 2,
             'H': 2,'P': 4,'L': 6,'G': 4,
             'E': 2,'D': 2,'A': 4,'V': 4,
             'W': 1,'C': 2,'Y': 2,'F': 2}
    prop=1
    for i in range(len(text)):
        if text[i].upper() in list(AA_prop.keys()):
            prop*=AA_prop[text[i].upper()]
        else:
            print("the used string does not seem to be an amino acid sequence or unknown amino acids are included.")
            exit()
    return prop

def score(ex_spec,theo_spec):
    return(len(set(ex_spec) & set(theo_spec)))


def subpeptides(peptide):
    result=[]
    l = len(peptide)
    looped = peptide + peptide
    for start in range(0, l):
        for length in range(1, l):
            result.append(looped[start:start+length])
    return result