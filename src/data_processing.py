#==========================================================================
#Read source CV and JD files and write output to a result file
#==========================================================================

def data_load(file):
    '''
    This function reads different types of source files.
    Input: Multiple file types like docx, pdf, txt
    Output: text string
    '''
    import textract
    data = str(textract.process(file), 'UTF-8')
    return data

def write_file(file_name, write_mode, write_string):
    '''
    This function writes the CV and JD comparison result to an output file.
    Input: Output file name, Write mode, Write string
    Output: Writes result to the output file
    '''
    output_file = open(file_name, write_mode)
    output_file.write(write_string)
    output_file.write('\n\n')
    output_file.write('-------------------------------------------------------------------------')
    output_file.write('\n\n')
    output_file.close()


#==========================================================================
#General Data Processing functions

def clean_text(text):
    '''
    This function cleans non-ASCII special characters from input text data.
    Input: Text string
    Output: Text string
    '''
    import re
    cleaned_data = re.sub(r'[^a-zA-Z0-9\s\/]', '', text)
    cleaned_data = cleaned_data.replace('/', ' ')
    return cleaned_data

def filter_token_tag(tagged_token_list, filter_tag_list):
    '''
    This function filters the tagged token list present in the filter tag list.
    Input: Tagged token list, filter tag list
    Output: List containing tokens corresponding to tags present in the filter tag list
    '''
    filtered_token_list = [t[0] for t in tagged_token_list if t[1] in filter_tag_list]
    filtered_token_list = [str(item) for item in filtered_token_list]
    return filtered_token_list

def unique_tokens(token_list):
    '''
    This function removes duplicate tokens from the input token list.
    Input: Token list
    Output: Unique token list
    '''
    unique_token_list = []
    for x in token_list:
        x = x.lower()
        if x not in unique_token_list:
            unique_token_list.append(x)
    return unique_token_list


#==========================================================================
#NLTK Data Processing

import nltk

def nltk_tokenizer(text):
    '''
    This function uses the NLTK tokeniser to tokenise the input text.
    Input: Text string
    Output: Tokens
    '''
    from nltk import word_tokenize
    tokens = word_tokenize(text)
    #tokens = text.split()
    return tokens

def nltk_pos_tag(token_list):
    '''
    This function uses the NLTK parts of speech tagger to apply tags to the input token list.
    Input: Token List
    Output: Tagged token list
    '''
    nltk.download('averaged_perceptron_tagger')
    from nltk import pos_tag
    tagged_list = pos_tag(token_list)
    return tagged_list

def nltk_stopwords_removal(token_list):
    '''
    This function removes stopwords from the input token list using the NLTK stopwords dictionary.
    Input: Token List
    Output: Stopwords filtered list
    '''
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    stopwords_filtered_list = [w for w in token_list if w not in stop_words] 
    return stopwords_filtered_list

def nltk_keywords(data):
    '''
    This function contains the NLTK pipeline to detect keywords from input text data.
    Input: Text data
    Output: Keywords
    '''
    data = clean_text(data)
    tokens = nltk_tokenizer(data)
    pos_tagged_tokens = nltk_pos_tag(tokens)
    keywords = filter_token_tag(pos_tagged_tokens, ['NNP', 'NN', 'VBP', 'JJ'])
    keywords = nltk_stopwords_removal(keywords)
    keywords = unique_tokens(keywords)
    #print('NLTK Keywords: ', keywords)
    return keywords



#==========================================================================
#Spacy Data Processing

import spacy
nlp = spacy.load('en_core_web_sm')

def spacy_tokenizer(text):
    '''
    This function uses the spacy tokeniser to tokenise the input text.
    Input: Text string
    Output: Tokens
    '''
    tokens = nlp(text)
    #tokens = text.split()
    return tokens

def spacy_pos_tag(token_list):
    '''
    This function uses the spacy parts of speech tagger to apply tags to the input token list.
    Input: Token List
    Output: Tagged token list
    '''
    tagged_list = []
    for tok in token_list:
        tagged_list.append((tok,tok.tag_))
    return tagged_list

def spacy_stopwords_removal(token_list):
    '''
    This function removes stopwords from the input token list using the spacy stopwords dictionary.
    Input: Token List
    Output: Stopwords filtered list
    '''
    stop_words = nlp.Defaults.stop_words
    stopwords_filtered_list = [w for w in token_list if w not in stop_words] 
    return stopwords_filtered_list

def spacy_keywords(data):
    '''
    This function contains the spacy pipeline to detect keywords from input text data.
    Input: Text data
    Output: Keywords
    '''
    data = clean_text(data)
    tokens = spacy_tokenizer(data)
    pos_tagged_tokens = spacy_pos_tag(tokens)
    keywords = filter_token_tag(pos_tagged_tokens, 'NNP')
    keywords = spacy_stopwords_removal(keywords)
    keywords = unique_tokens(keywords)
    #print('Spacy Keywords: ', keywords)
    return keywords



#==========================================================================