# The Three Investigators (Die drei ???)

## Prerequisites
- python 3.12

## Install virtual environment and packages
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Install spacy for german language
```sh
source venv/bin/activate
python -m spacy download de_core_news_lg
```

## Download audiobook transcripts
```sh
source venv/bin/activate
python download_scripts/download.py
````
