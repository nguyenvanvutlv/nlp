# FINE TUNE BERT WITH CUSTOM DATASET

## DATASET

- AIVIVN 2019: Sentiment Analysis Challenge: [link](https://github.com/undertheseanlp/NLP-Vietnamese-progress/blob/master/tasks/sentiment_analysis.md)

- NTC_SV [link](https://github.com/thoailinh/Sentiment-Analysis-using-BERT)

## INSTALLATION

*Python env: 3.9.13*

- **Install requirements**:

```bash
pip install -r requirements.txt
```

- **Install pytorch**:

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
 or

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```


- **RUN web**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## TRAINING

file training is in [train.py](fine_tune_bert_on_custom_dataset.pdf)
