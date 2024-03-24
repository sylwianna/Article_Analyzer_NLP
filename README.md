<h1 align="center">
  <br>
  <a href="https://www.theguardian.com/uk-news/2023/sep/08/what-a-year-of-king-charles-has-shown-us-about-how-he-wants-to-reign" target="_blank"><img src="What_a_year_of_King_Charles_has_shown_us_about_how_he_wants_to_reign_wordcloud.png" alt="Article Analyzer NLP" width="350"></a>
  <br>
  Article Analyzer NLP
  <br>
</h1>
<h4 align="center">Extract article's text from web page, transform, load to working directory, analyze content and visualize.</h4>

<p align="center">
  <a href="#general-info">General Info</a> •
  <a href="#features">Features</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#how-to-use">How to use</a> •
  <a href="#inspiration">Inspiration</a>
</p>

## General Info
Article Analyzer is a Python script which allows you to conduct analysis of web article text based on page url. It includes preparing the content - extraction of text from the url (web scraping), text data transformation (parsing, text/words adjustments so it is analysable etc.) and analysis with dataframe, bar chart, word cloud (which is a technique of visual representation of the most frequently occurring words in the given text) and creating report as Word document. Read more about word cloud in a separate repository <a href="https://github.com/sylwianna/WordCloud_Generator" target="_blank">WordCloud_Generator</a> and about the script's features below.

### Features
* extraction of article's text (web scraping)
* parsing extracted text
* saving files with extracted aticle's title
* further text data cleaning (NLP methods): changing structure, removing stopwords and unwanted characters (regex patterns), lemmatization, text partitioning
* creating dataframe with words and gathering basic statistics
* plotting chart
* generating wordcloud
* printing results to Word document report

**Challenges encountered:**
* When the idea popped into my head, I didn't expect so many cleaning steps would be necessary to prepare article's content for the analysis.
* Web pages' structure vary, which means not every scraper will work with every url (or even might stop working after page's structure is being changed by the author).

**Ideas for future development:**
* Create Bash/Powershell script to run two scripts, extract_article and anlyzie_article, one by one with just one command
* Carry out a deeper analysis and add more visuals

## Getting Started

### Prerequisites
* Python - version 3.9.7
* beautifulsoup4 - version 4.10.0
* numpy - version 1.26.4
* requests - version 2.26.0
* trafilatura - version 1.7.0
* spacy - version 3.7.4
* nltk - version 3.8.1
* pandas - version 2.2.1
* matplotlib - version 3.8.3
* mycolorpy - version 1.5.1
* pillow - version 10.2.0
* wordcloud - version 1.9.3
* python-docx - version 1.1.0

### How to use
To install python libraries and clone this repository, you can use below commands:

```bash
# Install prerequisites
$ pip install beautifulsoup4 numpy requests trafilatura spacy nltk pandas matplotlib mycolorpy pillow wodcloud python-docx
```

```bash
# Clone this repository
$ git clone https://github.com/sylwianna/Article_Analyzer_NLP.git

# Go into the repository
$ cd Article_Analyzer_NLP
```

 After that, you can run the scripts directly from terminal by using below command:

 ```bash
 # 1. Run extract_article.py
 $ python extract_article.py

 # 2. Run analyze_article.py
 $ python analyze_article.py
 ```
 
Or you can use the scripts with .ipynb extention and open them in Jupyter Notebook.

Replace the url in extract_article script with your chosen one and mask_image file in the repository to the shape you want for the resulting wordcloud. You can also adjust colors etc.

## Inspiration
:bulb: After creating <a href="https://github.com/sylwianna/WordCloud_Generator" target="_blank">WordCloud_Generator</a>, I was inspired by projects I'm currently involved in at my curret job position, to broaden the scope of the initial script by adding more features, and challenge myself in web scraping. The idea encouraged me to dive deeper into the field of NLP and learn more about the techniques for text analysis, resulting in the script beginning with text extraction and ending with visualising analysis results.
