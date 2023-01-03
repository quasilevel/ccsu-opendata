import os
import glob
import  pandas as pd

def checkTheSum75():
    all_files_name=glob.glob("BCA/*.json")
    currentPath=os.getcwd()
    check75=0
    #loop for opening file 
    for l in all_files_name:
        noOfYears=[]
        print("\nCode :",l)
        sampleFile=pd.read_json(os.path.join(currentPath, l))
        
        #loop for counting no of year in each file
        for i in range(len(sampleFile['topics'])):
            for j in range(len(sampleFile['topics'][i]['weights'])):
                noOfYears.append(sampleFile['topics'][i]['weights'][j]['year'])
        noOfYears=list(set(noOfYears))
        noOfYears.sort()

        for i in range(len(noOfYears)):
            for j in range(len(sampleFile['topics'])):
                for k in range(len(sampleFile['topics'][j]['weights'])):
                    if sampleFile['topics'][j]['weights'][k]['year']==noOfYears[i]:
                        check75=check75+sampleFile['topics'][j]['weights'][k]['weight']
            if check75 > 75:
                print("Year ",noOfYears[i],": total is : ",check75,"expected 75")
            elif check75<75:
                print("Year ",noOfYears[i],": total is : ",check75,"expected 75")
            elif check75==75:
                print("Year ",noOfYears[i],": total is : ",check75,"expected 75")
            check75=0
        noOfYears=[]


if __name__=="__main__":
    checkTheSum75()