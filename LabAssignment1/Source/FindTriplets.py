#Python program to find triplets in the list which gives the sum of zero
def findTriplets(num, len): #function definition to find triplets which result in sum 0
    found = False           #found is False shows zero triplets
    tripletslist = []       #create empty list to store triplets
    for i in range(0,len-2):            #loop from first element in the num list till leaving out last two elements
        for j in range(i+1,len-1):      #loop from next element of i variable till last but one
            for k in range(j+1,len):    #loop from next element of j variable till the end
                if(num[i]+num[j]+num[k]==0):    #if there are triplets
                    tripletslist.extend([(num[i],num[j],num[k])])   #Add triplets to list
                    found = True            #if Triplets found set it to True

    if(found== False):      #prints if no triples
        print("Triplets Not Found")
    else:                   #if triplets are found
        print(tripletslist) #   print triplets list


num = [1, 3, 6, 2, -1, 2, 8, -2, 9]   #list of numbers to find triplets
length = len(num)   #length of the list
findTriplets(num,length)    #function call to findtriplets in a list of numbers