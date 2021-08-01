# Resume Compatibility Checker
Resume Compatibility Checker is a simple python program to check the compatibility between a job description(JD) and a resume. It matches your resume/CV with the given job description that could help customise the resume/CV for a specific job. The program uses the NLTK and spacy libraries to extract keywords from resume/CV and JD. Then, it matches the JD-keywords in the resume/CV to give the comparison result. The program generates a detailed report based on the keywords match and cosine similarity between the JD and resume/CV.

## Installation

Pre-Requisite: Python 3.1 or higher
1. Clone the source code into your local directory.
2. Create a virtual environment.
3. Install required libraries (given in requirements.txt) in the virtual environment.

```python
git clone https://github.com/sumitprdrsh/Resume_Compatibility.git #For cloning the source code in local directory
pip install virtualenv #For Unix/Linux
pip install virtualenvwrapper-win #For windows
mkvirtualenv [Env name] #Create virtual environment
workon [Env name] #Activate virtual environment
pip install -r requirements.txt  #Install required libraries
```

## Execution
1. Place a single resume file in the directory - data/resume/. The program automatically picks the resume from this directory. The program will throw an error if more than one resume file is placed in this directory.
2. Place job description(JD) files in the directory - data/jd/. The program automatically picks all the JD files from this directory. Note: Multiple JD files can be placed in this directory.
3. Run the below command in cmd from the root directory, i.e. from the Resume_Compatibility folder.

```python
python src/main.py
```

## Usage
The program will generate a detailed comparison report (as shown below) in the directory - data/Result/. The JD-CV compatibility can be improved by adding the keywords in the CV which are present in JD but not in the CV. An example JD, CV and their comparison report is provided with this program.

```python
Match Result between JD and CV Keywords
+----------+--------------+----------------------+
|   Serial | JD Keyword   | JD-CV Match Result   |
|----------+--------------+----------------------|
|        0 | company      | No Match             |
|        1 | client       | No Match             |
|        2 | bods         | Match                |
|        3 | etl          | Match                |
|        4 | consultant   | No Match             |
|        5 | sme          | No Match             |
|        6 | month        | Match                |
|        7 | contract     | No Match             |
|        8 | basis        | No Match             |
|        9 | role         | No Match             |
|       10 | time         | Match                |
|       11 | ir35         | No Match             |
|       12 | data         | Match                |
|       13 | team         | Match                |
|       14 | bau          | Match                |
|       15 | experience   | Match                |
|       16 | bo           | Match                |
|       17 | extract      | No Match             |
|       18 | transform    | No Match             |
|       19 | load         | Match                |
|       20 | tool         | No Match             |
|       21 | strong       | No Match             |
|       22 | information  | Match                |
|       23 | steward      | Match                |
|       24 | bi           | Match                |
|       25 | management   | Match                |
|       26 | business     | Match                |
|       27 | microsoft    | Match                |
|       28 | office       | No Match             |
|       29 | inc          | No Match             |
|       30 | power        | Match                |
|       31 | azure        | No Match             |
+----------+--------------+----------------------+

-------------------------------------------------------------------------

Match percentage based on Keywords: 53.12%

-------------------------------------------------------------------------

Match percentage based on Cosine Similarity: 42.5%

-------------------------------------------------------------------------

Try to include unmatched keywords in your CV to improve the JD-CV compatibility.

-------------------------------------------------------------------------
```

## Testing
1. The program currently uses the spacy library to pick keywords from JD and uses the NLTK library to select keywords from resumes.
2. The true-positive(TP) and False-positive(FP) rates in spacy are less than NLTK. Hence, Spacy is used to capture keywords from the JD. It ensures that fewer incorrect keywords are captured from the JD. For resume, NLTK is used as FP rate doesn't matter there.
3. The table below shows the percentage of TP and FP for multiple combinations of test JD and NLP libraries.

```python
+--------+---------------------+----------------------+--------------------+---------------------+	
|TEST JD | SPACY TRUE POSITIVE | SPACY FALSE POSITIVE | NLTK TRUE POSITIVE | NLTK FALSE POSITIVE |
+--------+---------------------+----------------------+--------------------+---------------------+
|  JD1   |        76.2	       |         50.0	      |       90.5	       |        52.5         |
|  JD2   |        64.5	       |         48.6	      |       77.4	       |        60.9         |
+--------+---------------------+----------------------+--------------------+---------------------+

```

## Open Issues and Future Scope
1. The program is currently unable to handle pdf files as input in the Windows operating system. This problem is a result of an open issue of the python textract library in the Windows environment.
2. There is a plan to use Stanford NLP for JD/CV data processing to improve the result's accuracy.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)