import data_processing as dp
import os
print('------------------------------------------------------------------')



#Getting resume filename from data/resume directory
resume_file_name = os.listdir('data/resume/')
if len(resume_file_name) != 1:
    print('More than one resume found in data/resume directory.')
    quit()
resume_file_name = 'data/resume/' + str(resume_file_name[0])
print('Resume found: ', resume_file_name)



#Getting JD filelist from data/jd directory
jd_file_list = os.listdir('data/jd/')
print('JD file list found: ', jd_file_list)

for file_name in jd_file_list:
    #==========================================================================
    #------------Keywords extraction from JD using spacy---------------------
    jd_file_name = 'data/jd/' + str(file_name)
    data_jd = dp.data_load(jd_file_name)
    keywords_jd = dp.spacy_keywords(data_jd)

    #Write output in a result file
    write_string = 'Keywords found in JD: ' + (', '.join(keywords_jd))
    result_file_name = 'data/result/Result_Resume_' + str(file_name)
    dp.write_file( result_file_name, 'w', write_string)
    print('------------------------------------------------------------------')



    #==========================================================================
    #---------------Keywords extraction from resume using nltk---------------------
    data_resume = dp.data_load(resume_file_name)
    keywords_resume = dp.nltk_keywords(data_resume)

    #Write output in a result file
    write_string = 'Keywords found in resume: ' + (', '.join(keywords_resume))
    dp.write_file( result_file_name, 'a', write_string)
    print('------------------------------------------------------------------')



    #==========================================================================
    #----------------Matching Keywords between JD and Resume-----------------------

    #Creating a table showing Match Result between JD and Resume
    jd_keywords_in_resume_table = []
    for word in keywords_jd:
        if word in keywords_resume:
            match_result = [word, 'Match']
        else:
            match_result = [word, 'No Match']
        jd_keywords_in_resume_table.append(match_result)

    from tabulate import tabulate
    print(f'Comparing Resume and {file_name}:')
    print(tabulate( jd_keywords_in_resume_table, headers=['Serial', 'JD Keyword', 'JD-Resume Match Result'], showindex='always', tablefmt='psql' ))

    #Write output in a result file
    write_string = 'Match Result between JD and Resume Keywords' +  '\n' + tabulate( jd_keywords_in_resume_table, headers=['Serial', 'JD Keyword', 'JD-Resume Match Result'], showindex='always', tablefmt='psql' )
    dp.write_file( result_file_name, 'a', write_string)
    print('------------------------------------------------------------------')



    #==========================================================================
    #Calculating the percentage of the match result
    jd_keywords_in_resume_list = [w for w in keywords_jd if w in keywords_resume]
    jd_keywords_in_resume_list_count = len(jd_keywords_in_resume_list)
    jd_keywords_count_total = len(keywords_jd)
    

    matchPercentage = (jd_keywords_in_resume_list_count/jd_keywords_count_total) * 100
    matchPercentage = round(matchPercentage, 2) # round to two decimal
    print( f'Match percentage based on Keywords: {matchPercentage}%')

    #Write output in a result file
    write_string = 'Match percentage based on Keywords: ' + str(matchPercentage) + '%'
    dp.write_file( result_file_name, 'a', write_string)



    #==========================================================================
    #--------------Cosine Similarity between JD and Resume Keywords----------------
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    # A list of text
    text = [data_jd, data_resume]

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)

    #get the match percentage
    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    matchPercentage = round(matchPercentage, 2) # round to two decimal
    print( f'Match percentage based on Cosine Similarity: {matchPercentage}%')

    #Write output in a result file
    write_string = 'Match percentage based on Cosine Similarity: ' + str(matchPercentage) + '%'
    dp.write_file( result_file_name, 'a', write_string)

    write_string = 'Try to include unmatched keywords in your Resume to improve the JD-Resume compatibility.'
    dp.write_file( result_file_name, 'a', write_string)

    print('Detailed result file generated at: ', result_file_name)
    print('------------------------------------------------------------------')



    #==========================================================================