import re
from pyvi.ViTokenizer import tokenize
from nltk import flatten
import torch
import torch
from torch.nn import functional as F




def preprocess(text, pos, neg, replace_list):
    check = re.search(r'([a-z])\1+', text)
    if check:
        if len(check.group()) > 2:
            text = re.sub(r'([a-z])\1+', lambda m: m.group(1), text,
                          flags=re.IGNORECASE)  # remove các ký tự kéo dài như hayyy,ngonnnn...

    text = text.strip()  # loại dấu cách đầu câu
    text = text.lower()  # chuyển tất cả thành chữ thường

    text = re.sub('< a class.+</a>', ' ', text)

    for k, v in replace_list.items():  # replace các từ có trong replace_list
        text = text.replace(k, v)

    text = re.sub(r'_', ' ', text)

    text = ' '.join(i for i in flatten(tokenize(text).split(" ")))  # gán từ ghép

    for i in pos:  # thêm feature positive
        if re.search(' ' + i + ' ', text):
            text = re.sub(i, i + ' positive ', text)
    for i in neg:  # thêm feature negative
        if re.search(' ' + i + ' ', text):
            text = re.sub(i, i + ' negative ', text)
    return text


def bert(model, tokenizer, text):
    # Tokenize văn bản
    inputs_load = tokenizer(text, return_tensors="pt")

    # Dự đoán
    with torch.no_grad():
        outputs = model(**inputs_load)

    # Lấy dự đoán
    predictions = outputs.logits

    # Áp dụng softmax để có xác suất
    probs = F.softmax(predictions, dim=1)

    # Lấy nhãn có xác suất cao nhất
    predicted_class = torch.argmax(probs, dim=1).item()

    return "NEGATIVE" if predicted_class == 0 else "POSITIVE"