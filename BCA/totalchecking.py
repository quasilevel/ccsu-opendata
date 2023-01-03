import os
import glob
import  pandas as pd

def checkTheSum75():
    all_files_name=glob.glob("*.json")
    currentPath=os.getcwd()
    noFoYears=[]
    check75=0
    #loop for opening file 
    for l in all_files_name:
        print("checking for Year : ",l)
        sampleFile=pd.read_json(currentPath+"\\"+l)
        
        #loop for counting no of year in each file
        for i in range(len(sampleFile['topics'])):
            for j in range(len(sampleFile['topics'][i]['weights'])):
                noFoYears.append(sampleFile['topics'][i]['weights'][j]['year'])
        noFoYears=list(set(noFoYears))
        noFoYears.sort()

        for i in range(len(noFoYears)):
            for j in range(len(sampleFile['topics'])):
                for k in range(len(sampleFile['topics'][j]['weights'])):
                    if sampleFile['topics'][j]['weights'][k]['year']==noFoYears[i]:
                        check75=check75+sampleFile['topics'][j]['weights'][k]['weight']
            if check75 > 75:
                print(noFoYears[i]," This year sum is more than 75 and the total is : ",check75)
            elif check75<75:
                print(noFoYears[i]," This year sum is less than 75 and total is :",check75)
            elif check75==75:
                print(noFoYears[i],"Pass in test and the total is :",check75)
            check75=0
        noFoYears=[]


if __name__=="__main__":
    checkTheSum75()