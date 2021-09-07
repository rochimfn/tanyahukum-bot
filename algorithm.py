import pandas as pd
import numpy as np
import re


def get_data():
    return pd.read_csv("dataset.csv" ,sep='\t', quotechar="'")


def cleandata(kalimat):
    stop_words = {'begitu','maupun','hanya','adalah','yakni','bagi','yang','dengan','itu','ada','dan','atau', 'ini', 
                  'itu','di','ke','ini','jika','of','dalam','pada','yaitu','saja','untuk','dapat','adalah','dari','karena','tidak','juga','dan/atau',
                  'bahwa','harus','kita','apabila','oleh','apakah','mengapa','bagaimana','bagaimanakah','apa','dimaksud'
                 ,'sajakah','pada','maka','bolehkah'}
    kalimat = kalimat.replace("-", " ")
    kalimat = kalimat.replace("berapa", "jumlah")
    kalimat = kalimat.replace("mengapa", "alasan penyebab")
    kalimat = kalimat.replace("apakah yang dimaksud", "definisi")
    kalimat = kalimat.replace("apa yang dimaksud", "definisi")
    kalimatbaru=re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', kalimat)
    kalimatbaru=re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", kalimatbaru)
    word_list=kalimatbaru.split()
    output = [w for w in word_list if not w in stop_words]
  
    kalimatbaru = " ".join(output)
    return kalimatbaru

def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return float(len(s1.intersection(s2)) / len(s1.union(s2)))

lawdata=get_data()
jawab=np.array(lawdata.Response)
lawdata['gabung']=lawdata.Context.str.lower()+ ' ' +lawdata.Keywords.str.lower()
lawdata['gabung']=lawdata['gabung'].apply(lambda x :cleandata(x))
lawdata['gabung2']=lawdata.Response.str.lower()+ ' ' +lawdata.Keywords.str.lower()
lawdata['gabung2']=lawdata['gabung2'].apply(lambda x :cleandata(x))

def get_response(q):
	data=np.array(lawdata.gabung)
	similarity=np.zeros((len(data)))
	for i,line in enumerate(data):
		if (type(line)==str):
			qlist=cleandata(q).lower().split()
			linelist=cleandata(line).lower().split()
			similarity[i]=jaccard_similarity(qlist,linelist)
	idx=(-similarity).argsort()[:5]
	dataku = []
	i=1
	for y in idx:
    		dataku.append([i,jawab[y],similarity[y]])
    		i = i +1
	return(dataku)  

def ask(question):
    mydata=get_response(question.title().lower())
    return mydata[0][1]