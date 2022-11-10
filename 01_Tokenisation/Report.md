#REPORT

![Korean Hello][hello]

>“Today you are You, that is truer than true.
>There is no one alive who is Youer than You.”

>-Dr. Seuss

##Data

10 paragraphs were randomly extracted from the extracted Korean Language Wiki data dumps for segmentation purposes. I have basic syntactic and reading knowledge of the language but ltlle else, so I chose the language to avoid getting distracted by the language grammar and focus purely on the syntax using computational methods. 

##Segmentation

###1. Segmenters Used: Brief Description

####Pragmatic Segmenter (Ruby)

Kevin Dias' [Pragmatic Segmenter][nltk-resource] was used for segmenting the text. It works on rule-based sentence boundary detection by acting like a **"real-world"** segmenter for multiple languages.
 
**Regular Expressions**: Yes, uses regular expressions to match/replace strings
**Programming Language**: Ruby
**Machine Learning**: Does not use machine learning
**Training Language**: Does not use ML, hence does not require training, although most segmentation tools focus on English
**Training Algorithm**: No training algorithm as such; it uses 50 Golden Rules (English) and similar other language-specific golden rules to segment sentences and check for edge cases
**Training Corpus**: No training data (no ML); For testing the segmenter accuracy, 50 English Golden Rules were combined into one string and run 100 times through the segmenter

**Notes**:
> Defaults to segment on the English Language by default. To specify a language, we need to use its two character ISO 639-1 code. (Korean: "ko")
> It is specifically used for the purpose of segmenting texts for use in translation (and translation memory) related applications

####NLTK Punkt (Python)

deeplearning.ai's [Text Mining Online][nltk-resource] was used for segmenting the text

**Regular Expressions**: Yes, uses regular expressions
**Programming Language**: Python
**Machine Learning**: Yes, uses ML  
**Training Language**: The NLTK data package includes a pre-trained Punkt tokenizer for English. It must be trained on a large collection of plain language in the target language before it can be used. 
**Training Algorithm**: Unsupervised learning; Punkt is designed to learn parameters (a list of abbreviations, etc.) unsupervised from a corpus similar to the target domain.
**Training Corpus**: Large Collection of plain language

####2. Quantitative Evaluation

**Ruby Segmenter accuracy:** 100% (10 of 10 sentence boundaries are correctly detected)
**Python Segmenter accuracy:** 69% (9 of 13 sentence boundaries are correctly detected; 3 of 10 sentences are completely skipped, hence 3 sentences are extra, of which 1 sentence is incorrectly detected)

####3. Qualitative Evaluation

**Ruby Segmenter Mistakes:**

The ruby segmenter works exceptionally well, for the 10 lines that were validated. It is interesting to note, however, that segmenters essentially rely on the assumption that the input text is in a proper format. An instance of this would be the 2nd line which has a comma, so the segmenter treats it like part of a valid sentence.

**Python Segmenter Mistakes**

> It skips some lines completely, while segmenting
> It does not segment texts in parantheses properly; in the 10 lines of korean_py.txt file, we can see a ")" but not the "(" which was skipped. This is visible even more so, if we segment on more lines as in 50 line of segmented text in kowiki.para.py
> It segments correctly for start of quotations but takes the closing quotation marks to a newline.

##Tokenization


[nltk-resource]:https://textminingonline.com/dive-into-nltk-part-i-getting-started-with-nltk
[ruby-resource]:https://github.com/diasks2/pragmatic_segmenter
[hello]:https://tenor.com/view/hello-hi-globe-annyeong-kmmunity-gif-19086010
