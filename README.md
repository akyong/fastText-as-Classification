**FASTTEXT**

saya ada download file `cc.id.300.bin` dari https://fasttext.cc/docs/en/crawl-vectors.html
namun karena filenya 4,5GB dan ketika di extract 7,5GB maka tidak dipush kesini.


setelah file `index.py` dijalankan akan menghasilkan file `10ribuLabeled.csv`
kemudian masuk ke terminal untuk split data, karena data ada 10ribu. 

kita akan memakai 8000 untuk training dan 2000 untuk validasi.
```
head -n 8000 bobby/data/10ribuLabeled.csv > bobby/data/8ribuNews.train.csv
head -n 2000 bobby/data/10ribuLabeled.csv > bobby/data/2ribuNews.validation.csv
```

kemudian melatih model menggunakan fastText dengan perintah
```
./fasttext supervised -input bobby/data/8ribuNews.train.csv -output bobby/model/newsModel
Read 2M words
Number of words:  113994
Number of labels: 92
Progress: 100.0% words/sec/thread: 1668711 lr:  0.000000 avg.loss:  2.096904 ETA:   0h 0m 0s
```

perintah diatas akan menghasilkan 2 file yaitu:
- newsModel.bin
- newsModel.vec

kemudian kita akan melakukan validasi data terhadap 2ribu data tadi:
```
(venv) bobbyakyong@Bobby fastText % ./fasttext test bobby/model/newsModel.bin bobby/data/2ribuNews.validation.csv 
N   1999
P@1 0.466
R@1 0.466
```

N adalah jumlah record yang ditest.
```
P -> Precision
R -> Recall
```



