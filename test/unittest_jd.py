import unittest
import subprocess
import sys #For importing utility file, Ref-https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
sys.path.append('.')  #This will enable file import when program is executed from root directory
import src.data_processing as dp #Importing the utility file



class TestJD(unittest.TestCase):
    
    #==========================================================================
    #Testing spacy library's capability in capturing correct JD keywords

    def test_jd1_spacy_truepositive(self):
        jd_file_name = 'data/jd/JD1.txt'
        data_jd = dp.data_load(jd_file_name)
        actual = dp.spacy_keywords(data_jd) #Returns list of keywords (in lowercase) found in JD
        expected = ['BODS', 'ETL', 'Consultant', 'SME', 'Data', 'BAU', 'BO', 'Services', 'Information', 'Steward', 'profiling', 
                    'BI', 'Management', 'Business', 'Objects', 'Reporting', 'Microsoft', 'Office', 'Teams', 'Power', 'Azure']
        expected = [x.lower() for x in expected] #converting the expected list to lowercase

        count = 0
        for keyword in expected:
            if keyword in actual:
                count = count+1
        percent_match = round((count / len(expected)) * 100, 1)
        #print('Spacy JD1 TP: ', percent_match)
        self.assertGreaterEqual(percent_match, 75.0) #Pass testcase if true-positive is greater than 75%
    

    def test_jd1_spacy_falsepositive(self):
        jd_file_name = 'data/jd/JD1.txt'
        data_jd = dp.data_load(jd_file_name)
        actual = dp.spacy_keywords(data_jd) #Returns list of keywords (in lowercase) found in JD
        expected = ['BODS', 'ETL', 'Consultant', 'SME', 'Data', 'BAU', 'BO', 'Services', 'Information', 'Steward', 'profiling', 
                    'BI', 'Management', 'Business', 'Objects', 'Reporting', 'Microsoft', 'Office', 'Teams', 'Power', 'Azure']
        expected = [x.lower() for x in expected] #converting the expected list to lowercase

        count = 0
        for keyword in actual:
            if keyword not in expected:
                count = count+1
        percent_match = round((count / len(actual)) * 100, 1)
        #print('Spacy JD1 FP: ', percent_match)
        self.assertLessEqual(percent_match, 50.0) #Pass testcase if false-positive is less than 50%

    
    def test_jd2_spacy_truepositive(self):
        jd_file_name = 'data/jd/JD2.txt'
        data_jd = dp.data_load(jd_file_name)
        actual = dp.spacy_keywords(data_jd) #Returns list of keywords (in lowercase) found in JD
        expected = ['Cloud', 'Data', 'Engineer', 'AI', 'business', 'critical', 'end-to-end', 'solutions', 'strategy', 'governance', 
                    'transform', 'design', 'implement', 'scalable', 'Agile', 'DevOps', 'implementation', 'delivery', 'communication', 
                    'skills', 'deliver', 'client', 'AWS', 'GCP', 'Azure', 'architecture', 'pipelines', 'Spark', 'Scala', 'Python', 'Java', 
                    'Kafka', 'client-facing', 'consulting', 'interpersonal', 'analytical', 'creative', 'team-oriented', 'high-quality', 
                    'MDM', 'Metadata', 'Management', 'Data', 'Quality', 'Data', 'Lineage', 'tools', 'E2E', 'non-functional', 'operations', 
                    'Regulatory', 'Compliance', 'Lifecycle', 'Solution', 'Prototyping', 'Usability', 'testing', 'data', 'visualization', 'SQL', 
                    'NoSQL', 'stores']
        expected = [x.lower() for x in expected] #converting the expected list to lowercase

        count = 0
        for keyword in expected:
            if keyword in actual:
                count = count+1
        percent_match = round((count / len(expected)) * 100, 1)
        #print('Spacy JD2 TP: ', percent_match)
        self.assertGreaterEqual(percent_match, 75.0) #Pass testcase if true-positive is greater than 75%


    def test_jd2_spacy_falsepositive(self):
        jd_file_name = 'data/jd/JD2.txt'
        data_jd = dp.data_load(jd_file_name)
        actual = dp.spacy_keywords(data_jd) #Returns list of keywords (in lowercase) found in JD
        expected = ['Cloud', 'Data', 'Engineer', 'AI', 'business', 'critical', 'end-to-end', 'solutions', 'strategy', 'governance', 
                'transform', 'design', 'implement', 'scalable', 'Agile', 'DevOps', 'implementation', 'delivery', 'communication', 
                'skills', 'deliver', 'client', 'AWS', 'GCP', 'Azure', 'architecture', 'pipelines', 'Spark', 'Scala', 'Python', 'Java', 
                'Kafka', 'client-facing', 'consulting', 'interpersonal', 'analytical', 'creative', 'team-oriented', 'high-quality', 
                'MDM', 'Metadata', 'Management', 'Data', 'Quality', 'Data', 'Lineage', 'tools', 'E2E', 'non-functional', 'operations', 
                'Regulatory', 'Compliance', 'Lifecycle', 'Solution', 'Prototyping', 'Usability', 'testing', 'data', 'visualization', 'SQL', 
                'NoSQL', 'stores']
        expected = [x.lower() for x in expected] #converting the expected list to lowercase

        count = 0
        for keyword in actual:
            if keyword not in expected:
                count = count+1
        percent_match = round((count / len(actual)) * 100, 1)
        #print('Spacy JD2 FP: ', percent_match)
        self.assertLessEqual(percent_match, 50.0) #Pass testcase if false-positive is less than 50%



    #==========================================================================
    #Testing NLTK library's capability in capturing correct JD keywords

    def test_jd1_nltk_truepositive(self):
        jd_file_name = 'data/jd/JD1.txt'
        data_jd = dp.data_load(jd_file_name)
        actual = dp.nltk_keywords(data_jd) #Returns list of keywords (in lowercase) found in JD
        expected = ['BODS', 'ETL', 'Consultant', 'SME', 'Data', 'BAU', 'BO', 'Services', 'Information', 'Steward', 'profiling', 
                    'BI', 'Management', 'Business', 'Objects', 'Reporting', 'Microsoft', 'Office', 'Teams', 'Power', 'Azure']
        expected = [x.lower() for x in expected] #converting the expected list to lowercase

        count = 0
        for keyword in expected:
            if keyword in actual:
                count = count+1
        percent_match = round((count / len(expected)) * 100, 1)
        #print('NLTK JD1 TP: ', percent_match)
        self.assertGreaterEqual(percent_match, 75.0) #Pass testcase if true-positive is greater than 75%

    
    def test_jd1_nltk_falsepositive(self):
        jd_file_name = 'data/jd/JD1.txt'
        data_jd = dp.data_load(jd_file_name)
        actual = dp.nltk_keywords(data_jd) #Returns list of keywords (in lowercase) found in JD
        expected = ['BODS', 'ETL', 'Consultant', 'SME', 'Data', 'BAU', 'BO', 'Services', 'Information', 'Steward', 'profiling', 
                    'BI', 'Management', 'Business', 'Objects', 'Reporting', 'Microsoft', 'Office', 'Teams', 'Power', 'Azure']
        expected = [x.lower() for x in expected] #converting the expected list to lowercase

        count = 0
        for keyword in actual:
            if keyword not in expected:
                count = count+1
        percent_match = round((count / len(actual)) * 100, 1)
        #print('NLTK JD1 FP: ', percent_match)
        self.assertLessEqual(percent_match, 50.0) #Pass testcase if false-positive is less than 50%

    
    def test_jd2_nltk_truepositive(self):
        jd_file_name = 'data/jd/JD2.txt'
        data_jd = dp.data_load(jd_file_name)
        actual = dp.nltk_keywords(data_jd) #Returns list of keywords (in lowercase) found in JD
        expected = ['Cloud', 'Data', 'Engineer', 'AI', 'business', 'critical', 'end-to-end', 'solutions', 'strategy', 'governance', 
                    'transform', 'design', 'implement', 'scalable', 'Agile', 'DevOps', 'implementation', 'delivery', 'communication', 
                    'skills', 'deliver', 'client', 'AWS', 'GCP', 'Azure', 'architecture', 'pipelines', 'Spark', 'Scala', 'Python', 'Java', 
                    'Kafka', 'client-facing', 'consulting', 'interpersonal', 'analytical', 'creative', 'team-oriented', 'high-quality', 
                    'MDM', 'Metadata', 'Management', 'Data', 'Quality', 'Data', 'Lineage', 'tools', 'E2E', 'non-functional', 'operations', 
                    'Regulatory', 'Compliance', 'Lifecycle', 'Solution', 'Prototyping', 'Usability', 'testing', 'data', 'visualization', 'SQL', 
                    'NoSQL', 'stores']
        expected = [x.lower() for x in expected] #converting the expected list to lowercase

        count = 0
        for keyword in expected:
            if keyword in actual:
                count = count+1
        percent_match = round((count / len(expected)) * 100, 1)
        #print('NLTK JD2 TP: ', percent_match)
        self.assertGreaterEqual(percent_match, 75.0) #Pass testcase if true-positive is greater than 75%


    def test_jd2_nltk_falsepositive(self):
        jd_file_name = 'data/jd/JD2.txt'
        data_jd = dp.data_load(jd_file_name)
        actual = dp.nltk_keywords(data_jd) #Returns list of keywords (in lowercase) found in JD
        expected = ['Cloud', 'Data', 'Engineer', 'AI', 'business', 'critical', 'end-to-end', 'solutions', 'strategy', 'governance', 
                'transform', 'design', 'implement', 'scalable', 'Agile', 'DevOps', 'implementation', 'delivery', 'communication', 
                'skills', 'deliver', 'client', 'AWS', 'GCP', 'Azure', 'architecture', 'pipelines', 'Spark', 'Scala', 'Python', 'Java', 
                'Kafka', 'client-facing', 'consulting', 'interpersonal', 'analytical', 'creative', 'team-oriented', 'high-quality', 
                'MDM', 'Metadata', 'Management', 'Data', 'Quality', 'Data', 'Lineage', 'tools', 'E2E', 'non-functional', 'operations', 
                'Regulatory', 'Compliance', 'Lifecycle', 'Solution', 'Prototyping', 'Usability', 'testing', 'data', 'visualization', 'SQL', 
                'NoSQL', 'stores']
        expected = [x.lower() for x in expected] #converting the expected list to lowercase

        count = 0
        for keyword in actual:
            if keyword not in expected:
                count = count+1
        percent_match = round((count / len(actual)) * 100, 1)
        #print('NLTK JD2 FP: ', percent_match)
        self.assertLessEqual(percent_match, 50.0) #Pass testcase if false-positive is less than 50%
    
    
    
    

if __name__ == '__main__':
    unittest.main()
