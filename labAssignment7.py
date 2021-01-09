#!/usr/bin/env python
import re
antiCodon = {"TTT":"F","TTC":"F","TTA":"L","TTG":"L","TCT":"S","TCC":"S",
"TCA":"S","TCG":"S","TAT":"Y","TAC":"Y","TAA":"*","TAG":"*","TGT":"C","TGC":"C",
"TGA":"*","TGG":"W","CTT":"L","CTC":"L","CTA":"L","CTG":"L","CCT":"P","CCC":"P",
"CCA":"P","CCG":"P","CAT":"H","CAC":"H","CAA":"Q","CAG":"Q","CGT":"R",
"CGA":"R","CGG":"R","ATT":"I","ATC":"I","ATA":"I","ATG":"M","ACT":"T","ACA":"T",
"ACG":"T","AAT":"N","AAC":"N","AAA":"K","AAG":"K","AGT":"S","AGC":"S","AGA":"R",
"AGG":"R","GTT":"V","GTC":"V","GTA":"V","GTG":"V","GCT":"A","GCC":"A","GCA":"A",
"GCG":"A","GAT":"D","GAC":"D","GAA":"E","GAG":"E","GGT":"G","GGC":"G","GGA":"G",
"GGG":"G","ACC":"T","CGC":"R"}
filename = "lab7.fa"
f = open(filename,"r")
lines = f.readlines()
f.close()
i = 0
joined = ""
transDna = []
transDna.append("")
foundGenes = []
preTrans = []
preTrans.append("")
geneHolder = []
counter = 0
geneSearch = re.compile(r"(ATG.+)(TAA|TGA|TAG)")#make sure ATG appears and works

for z in lines:
    z = z.rstrip("\n")
    joined = joined + z
#frame 1 start
loc = 0
for l in geneSearch.findall(joined)[0]:
    for pos in range(0,len(l),3):
        codon = l[pos:pos+3]
        if(len(codon)%3 == 0 and antiCodon[codon] != "*"):
            transDna[counter] = transDna[counter] + antiCodon[codon]
            preTrans[counter] = preTrans[counter] + codon
        if(len(codon)%3 == 0 and antiCodon[codon] == "*"):
            transDna[counter] = transDna[counter] + "*"
            preTrans[counter] = preTrans[counter] + codon
            transDna.append("")
            preTrans.append("")
            counter = counter + 1
for x in transDna:
    if(transDna[i] != ""):
        pullOut = re.compile(r"M.+")
        if(pullOut.findall(transDna[i]) != []):
            foundGenes.append((pullOut.findall(transDna[i])[0]))
            geneHolder.append(preTrans[i])  
        i = i+1
counter = 0
i = 0 #frame 1 end
#frame 2 start
transDna = []
transDna.append("")
loc = 0
for l in geneSearch.findall(joined)[0]:
    for pos in range(1,len(l),3):
        codon = l[pos:pos+3]
        if(len(codon)%3 == 0 and antiCodon[codon] != "*"):
            transDna[counter] = transDna[counter] + antiCodon[codon]
            preTrans[counter] = preTrans[counter] + codon
        if(len(codon)%3 == 0 and antiCodon[codon] == "*"):
            transDna[counter] = transDna[counter] + "*"
            preTrans[counter] = preTrans[counter] + codon
            transDna.append("")
            preTrans.append("")
            counter = counter + 1
for x in transDna:
    if(transDna[i] != ""):
        pullOut = re.compile(r"M.+")
        if(pullOut.findall(transDna[i]) != []):
            foundGenes.append((pullOut.findall(transDna[i])[0]))
            geneHolder.append(preTrans[i])
        i = i+1
counter = 0
i = 0 #frame 2 end
#frame 3 start
transDna = []
transDna.append("")
loc = 0
for l in geneSearch.findall(joined)[0]:
    for pos in range(2,len(l),3):
        codon = l[pos:pos+3]
        if(len(codon)%3 == 0 and antiCodon[codon] != "*"):
            transDna[counter] = transDna[counter] + antiCodon[codon]
            preTrans[counter] = preTrans[counter] + codon
        if(len(codon)%3 == 0 and antiCodon[codon] == "*"):
            transDna[counter] = transDna[counter] + "*"
            preTrans[counter] = preTrans[counter] + codon
            transDna.append("")
            preTrans.append("")
            counter = counter + 1
for x in transDna:
    if(transDna[i] != ""):
        pullOut = re.compile(r"M.+")
        if(pullOut.findall(transDna[i]) != []):
            foundGenes.append((pullOut.findall(transDna[i])[0]))
            geneHolder.append(preTrans[i])
        i = i+1
counter = 0
i = 0 #frame 3 end
#frame 4 start
loc = 0
flippedStrand = ""
joinedRev = joined[::-1]
for n in joinedRev:
    if(n == "A"):
        flippedStrand = flippedStrand + "T"
    if(n == "T"):
        flippedStrand = flippedStrand + "A"
    if(n == "G"):
        flippedStrand = flippedStrand + "C"
    if(n == "C"):
        flippedStrand = flippedStrand + "G"
testList = [flippedStrand]
for l in testList:
    for pos in range(0,len(l),3):
        codon = l[pos:pos+3]
        if(len(codon)%3 == 0 and antiCodon[codon] != "*"):
            transDna[counter] = transDna[counter] + antiCodon[codon]
            preTrans[counter] = preTrans[counter] + codon
        if(len(codon)%3 == 0 and antiCodon[codon] == "*"):
            transDna[counter] = transDna[counter] + "*"
            preTrans[counter] = preTrans[counter] + codon
            transDna.append("")
            preTrans.append("")
            counter = counter + 1
for x in transDna:
    if(transDna[i] != ""):
        pullOut = re.compile(r"M.+")
        if(pullOut.findall(transDna[i]) != []):
            foundGenes.append((pullOut.findall(transDna[i])[0]))
            geneHolder.append(preTrans[i])  
        i = i+1
counter = 0
i = 0 #frame 4 end
#frame 5 start
transDna = []
transDna.append("")
loc = 0
for l in testList:
    for pos in range(1,len(l),3):
        codon = l[pos:pos+3]
        if(len(codon)%3 == 0 and antiCodon[codon] != "*"):
            transDna[counter] = transDna[counter] + antiCodon[codon]
            preTrans[counter] = preTrans[counter] + codon
        if(len(codon)%3 == 0 and antiCodon[codon] == "*"):
            transDna[counter] = transDna[counter] + "*"
            preTrans[counter] = preTrans[counter] + codon
            transDna.append("")
            preTrans.append("")
            counter = counter + 1
for x in transDna:
    if(transDna[i] != ""):
        pullOut = re.compile(r"M.+")
        if(pullOut.findall(transDna[i]) != []):
            foundGenes.append((pullOut.findall(transDna[i])[0]))
            geneHolder.append(preTrans[i])
        i = i+1
counter = 0
i = 0 #frame 5 end
#frame 6 start
transDna = []
transDna.append("")
loc = 0
for l in testList:
    for pos in range(2,len(l),3):
        codon = l[pos:pos+3]
        if(len(codon)%3 == 0 and antiCodon[codon] != "*"):
            transDna[counter] = transDna[counter] + antiCodon[codon]
            preTrans[counter] = preTrans[counter] + codon
        if(len(codon)%3 == 0 and antiCodon[codon] == "*"):
            transDna[counter] = transDna[counter] + "*"
            preTrans[counter] = preTrans[counter] + codon
            transDna.append("")
            preTrans.append("")
            counter = counter + 1
for x in transDna:
    if(transDna[i] != ""):
        pullOut = re.compile(r"M.+")
        if(pullOut.findall(transDna[i]) != []):
            foundGenes.append((pullOut.findall(transDna[i])[0]))
            geneHolder.append(preTrans[i])
        i = i+1
counter = 0
i = 0 #frame 6 end
printCounter = 0
#print(geneHolder)
#print(foundGenes)
for x in foundGenes:#check to see if key is correct/adding logic
    print("gene " + str(printCounter + 1))
    print(geneHolder[printCounter])
    print(x)
    printCounter = printCounter + 1