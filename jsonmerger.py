#Harish Kumar

import os
import json
from jsonmerge import Merger
jsonfile=[]
ip_content=[]
def show_contents(suffix,path="."):
    try:
        for f in os.listdir(path):

            if f.endswith('.json'):
                if suffix in os.path.splitext(os.path.join(path,f))[0]:
                    if os.path.isfile(os.path.join(path,f)):
                        jsonfile.append(os.path.join(path,f))
                        print(f," file size is",os.path.getsize(os.path.join(path,f)))
    except:
        print("\nError, once check the path")
        return


def merge(a, b):
    "merges b into a"
    for key in b:
        if key in a:# if key is in both a and b
            if isinstance(a[key], dict) and isinstance(b[key], dict): # if the key is dict Object
                merge(a[key], b[key])
            else:
              a[key] =a[key]+ b[key]
        else: # if the key is not in dict a , add it to dict a
            a.update({key:b[key]})
    return a







if __name__ == "__main__":
    way=input("Enter the path of the  input files: ")
    ways=way
    suffix=input("Enter the input file suffix: ")
    show_contents(suffix,way)
    empty={}
    outputsuffix=input("Enter the output file suffix: ")
    size=int(input("Enter the max file size in bytes: "))
    way+='\\'
    no=1
    way+=outputsuffix
    firstway=way+str(no)
    firstway+=".json"
    f= open(firstway,"w+")
    f.close()
    jsonfile.append(firstway)
    #print(jsonfile)
    with open(jsonfile[len(jsonfile)-1], 'w') as f:
        json.dump(empty,f,sort_keys=False)

    with open(jsonfile[len(jsonfile)-1]) as fp1:
        with open(jsonfile[0]) as fp2:
            jsondata1=json.load(fp1)
            jsondata2=json.load(fp2)
            with open(jsonfile[len(jsonfile)-1], 'w') as f:
                json.dump(merge(jsondata1,jsondata2),f,sort_keys=False)

            #print("created the result file: ",jsonfile[len(jsonfile)-1]," file size is ",os.path.getsize(jsonfile[len(jsonfile)-1]))
            #print("first way :",firstway)
            for i in range(1,len(jsonfile)-1):

                if os.path.getsize(firstway) >size:
                    #print("greater so merging ")
                    no+=1
                    jsonfile.append(way+str(no)+".json")
                    f= open(way+str(no)+".json","w+")
                    f.close()
                    with open(jsonfile[len(jsonfile)-1], 'w') as f:
                        json.dump(empty,f,sort_keys=False)


                    with open(jsonfile[len(jsonfile)-1]) as fp1:
                        with open(jsonfile[i]) as fp2:
                            jsondata1=json.load(fp1)
                            jsondata2=json.load(fp2)
                            with open(jsonfile[len(jsonfile)-1], 'w') as f:
                                json.dump(merge(jsondata1,jsondata2),f,sort_keys=False)
                    #print("file size of ",firstway[-7:],"size ",os.path.getsize(firstway),"size: ",size)


                    firstway=""
                    firstway=way+str(no)+".json"
                else:
                    #print("file size of ",firstway[-7:],"size ",os.path.getsize(firstway),"size: ",size)
                    with open(jsonfile[len(jsonfile)-1]) as fp1:
                        with open(jsonfile[i]) as fp2:
                            jsondata1=json.load(fp1)
                            jsondata2=json.load(fp2)
                            with open(jsonfile[len(jsonfile)-1], 'w') as f:
                                json.dump(merge(jsondata1,jsondata2),f,sort_keys=False)
    show_contents(outputsuffix,ways)
