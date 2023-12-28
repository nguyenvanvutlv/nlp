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


- **Get checkpoint**:

Go to [checkpoint](https://nogdev-my.sharepoint.com/:u:/g/personal/vunguyen_nogdev_onmicrosoft_com/Ea4c4-YglN9FtDqt6vRyEKIBI0MayWLvZAWsf9FBKaQ02g?e=4SWjLi)

Extract and put it in folder `static/`


- **RUN web**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## TRAINING

file training is in [train.py](fine_tune_bert_on_custom_dataset.pdf)
