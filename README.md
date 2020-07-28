# python_nlp


### To get started:
**Install:**
```
$ pip install --upgrate tensorflow
$ pip install --upgrade scikit-learn
$ pip install --upgrade matplotlib
$ pip install numpy scipy
$ pip install keras
$ pip install --user -U nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download(“stopwords”)
```
**Сonfigure model parameters**
in *param.json*:
```
    "name": "testCorpus",
    "language": "eng",
    "source": "myCorpusSmall",
    "stemType": "stemming",
    "stopWordsType": "none",
    "metric": "tf",
    "dbCorpusPath": "/mnt/hgfs/vmware D/dataBase/myCorpus.db",
    "docCorpusPath": "/mnt/hgfs/vmware D/topicsSmall",
    "trainPercentage": 70,
    "saveDictionary": false
```

For a complete analysis of the corpus, you can run the *main.py* or *demo_full_analysis.ipynb* file.

For neural network analysis of the corpus based on input vectors, you can run the file *main_nn_analysis.py* or *demo_classification.ipynb*
