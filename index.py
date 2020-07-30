import fasttext.util
import pandas as pd

# function
def separate(params):
    print("\n\n----------------------------------- {} ---------------------------------------".format(params))

def getWordVector(word):
    print("Word Vector : {} \n".format(model[word]))

def getSizeVector(word):
    print("Total Size {}".format(model[word].size))

def downloadModel():
    fasttext.util.download_model('id', if_exists='ignore')


# fastText Start!
# todo download word vector model dalam bahasa indonesia
downloadModel()
model = fasttext.load_model("cc.id.300.bin")

# getSizeVector('suka')
# getWordVector('suka')

# print(model['suka'].size)
# no = 1;
# teks = "No. {}: {}";
# for x in model['suka']:
#     print(teks.format(no, x))
#     no+=1



news = pd.read_csv('/Users/bobbyakyong/Projects/python/fastText/bobby/50data2Column.csv',delimiter=',', header=None)
# cols = ['id','title','source','category','link','text']
news.columns = ['category','text']

#news['Product'] = news['category'].replace(' ', '_', regex=True)
news['category']=['__label__'+s.replace(' or ', '$').replace(', or ','$').replace(',','$').replace(' ','_').replace(',','__label__').replace('$$','$').replace('$',' __label__').replace('___','__') for s in news['category']]
# news['category']

news['text']= news['text'].replace('\n',' ', regex=True).replace('\t',' ', regex=True)
#news['text']=news['text'][1:-1]
news.to_csv('labeledData.csv',index=False)
print(news)