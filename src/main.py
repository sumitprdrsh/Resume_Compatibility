import data_processing as dp
import os
print('------------------------------------------------------------------')

#Getting CV filename from data/CV directory
cv_file_name = os.listdir('data/CV/')
if len(cv_file_name) != 1:
    print('More than one CV found in CV directory.')
    quit()
cv_file_name = 'data/CV/' + str(cv_file_name[0])
print('CV found: ', cv_file_name)

#Getting JD filelist from data/JD directory
JD_file_list = os.listdir('data/JD/')
print('JD file list found: ', JD_file_list)

for file_name in JD_file_list:
    #==========================================================================
    #------------Keywords extraction from JD using spacy---------------------
    jd_file_name = 'data/JD/' + str(file_name)
    data_JD = dp.data_load(jd_file_name)
    keywords_JD = dp.spacy_keywords(data_JD)

    #Write output in a result file
    write_string = 'Keywords found in JD: ' + (', '.join(keywords_JD))
    result_file_name = 'data/Result/Result_CV_' + str(file_name)
    dp.write_file( result_file_name, 'w', write_string)
    print('------------------------------------------------------------------')



    #==========================================================================
    #---------------Keywords extraction from CV using nltk---------------------
    data_CV = dp.data_load(cv_file_name)
    keywords_CV = dp.nltk_keywords(data_CV)

    #Write output in a result file
    write_string = 'Keywords found in CV: ' + (', '.join(keywords_CV))
    result_file_name = 'data/Result/Result_CV_' + str(file_name)
    dp.write_file( result_file_name, 'a', write_string)
    print('------------------------------------------------------------------')



    #==========================================================================
    #----------------Matching Keywords between JD and CV-----------------------

    #Creating a table showing Match Result between JD and CV
    jd_keywords_in_resume_table = []
    for word in keywords_JD:
        if word in keywords_CV:
            Match_Result = [word, 'Match']
        else:
            Match_Result = [word, 'No Match']
        jd_keywords_in_resume_table.append(Match_Result)

    from tabulate import tabulate
    print(f'Comparing CV and {file_name}:')
    print(tabulate( jd_keywords_in_resume_table, headers=['Serial', 'JD Keyword', 'JD-CV Match Result'], showindex='always', tablefmt='psql' ))

    #Write output in a result file
    write_string = 'Match Result between JD and CV Keywords' +  '\n' + tabulate( jd_keywords_in_resume_table, headers=['Serial', 'JD Keyword', 'JD-CV Match Result'], showindex='always', tablefmt='psql' )
    result_file_name = 'data/Result/Result_CV_' + str(file_name)
    dp.write_file( result_file_name, 'a', write_string)
    print('------------------------------------------------------------------')



    #==========================================================================
    #Calculating the percentage of the match result
    jd_keywords_in_resume_list = [w for w in keywords_JD if w in keywords_CV]
    jd_keywords_in_resume_list_count = len(jd_keywords_in_resume_list)
    jd_keywords_count_total = len(keywords_JD)
    

    matchPercentage = (jd_keywords_in_resume_list_count/jd_keywords_count_total) * 100
    matchPercentage = round(matchPercentage, 2) # round to two decimal
    print( f'Match percentage based on Keywords: {matchPercentage}%')

    #Write output in a result file
    write_string = 'Match percentage based on Keywords: ' + str(matchPercentage) + '%'
    result_file_name = 'data/Result/Result_CV_' + str(file_name)
    dp.write_file( result_file_name, 'a', write_string)



    #==========================================================================
    #--------------Cosine Similarity between JD and CV Keywords----------------
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    # A list of text
    text = [data_JD, data_CV]

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)

    #get the match percentage
    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    matchPercentage = round(matchPercentage, 2) # round to two decimal
    print( f'Match percentage based on Cosine Similarity: {matchPercentage}%')

    #Write output in a result file
    write_string = 'Match percentage based on Cosine Similarity: ' + str(matchPercentage) + '%'
    result_file_name = 'data/Result/Result_CV_' + str(file_name)
    dp.write_file( result_file_name, 'a', write_string)

    write_string = 'Try to include unmatched keywords in your CV to improve the JD-CV compatibility.'
    result_file_name = 'data/Result/Result_CV_' + str(file_name)
    dp.write_file( result_file_name, 'a', write_string)

    print('Detailed result file generated at: ', result_file_name)
    print('------------------------------------------------------------------')



    #==========================================================================