# import the numpy and pandas module from the python library
import numpy as np
import pandas as pd

# dictionary mapping municipality twitter handles to the municipality name
mun_dict = {'@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}

# dictionary of english stopwords
stop_words_dict = {
        'stopwords':['where', 'done', 'if', 'before', 'll', 'very', 'keep',
        'something', 'nothing', 'thereupon', 'may', 'why', 'â€™s', 'therefore',
        'you', 'with', 'towards', 'make', 'really', 'few', 'former', 'during',
        'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming',
        'through', 'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole',
        'down', 'seem', 'whereas', 'to', 'their', 'various', 'thereafter',
        'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein',
        'become', 'last', 'between', 'still', 'was', 'almost', 'twelve',
        'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see',
        'whose', 'everywhere', 'yourselves', 'across', 'myself', 'further',
        'did', 'then', 'is', 'except', 'up', 'take', 'became', 'however',
        'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein',
        'elsewhere', 'behind', 'becomes', 'alone', 'due', 'being', 'neither',
        'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 'forty',
        'what', 'less', 'and', 'please', 'toward', 'about', 'below',
        'hereafter', 'whether', 'yet', 'nor', 'against', 'whereupon', 'top',
        'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything',
        'nowhere', 'ca', 'though', 'least', 'so', 'both', 'otherwise',
        'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its',
        'after', 'bottom', 'call', 'nâ€™t', 'name', 'even', 'eleven', 'by',
        'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 'much', 'another',
        'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full',
        'themselves', 'been', 'in', "'d", 'wherever', 'part', 'someone',
        'therein', 'can', 'seemed', 'hereby', 'others', "'s", "'re", 'most',
        'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as',
        'nobody', 'also', 'along', 'than', 'anything', 'he', 'there', 'does',
        'we', 'â€™ll', 'latterly', 'are', 'ten', 'hers', 'should', 'they',
        'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely',
        'sixty', 'made', "'m", 'always', 'those', 'have', 'again', 'her',
        'once', 'ours', 'herself', 'else', 'has', 'nine', 'more', 'sometimes',
        'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot',
        'â€˜ll', 'too', 'seems', 'â€™m', 'himself', 'latter', 'whither',
        'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say',
        'via', 'but', 'often', 're', 'our', 'because', 'rather', 'using',
        'without', 'throughout', 'on', 'she', 'never', 'eight', 'no',
        'hereupon', 'them', 'whereafter', 'quite', 'which', 'move', 'thru',
        'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t','him', 'could',
        'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several',
        'side', 'whence', 'me', 'same', 'were', 'it', 'every', 'third',
        'together']}

# funtion 1: Metric Dictionary
def dictionary_of_metrics(items):
    ''' Returns a dictionary with the mean, median, variance, standard
        deviation, minimum and the maximum value.

        Keyword argument:
            items (list) -- a list of number values.

        Returns:
            dictionary: mean, median, variance, standard deviation, the
                        minimum and maximum value; rounded to 2 decimal places

        Example:
            >>> dictionary_of_metrics([1,2,3,4,5])
            {'mean': 3.0, 'median': 3, 'variance': 2.5, 'standard deviation': 1.58,
            'min': 1, 'max': 5}
    '''
    # sort the list and create an array
    items.sort()
    items_array = np.array(items)

    # calculating the median
    if len(items)%2==0: # if the length of the list is even
        median = (items[int((len(items)+1)/2)-1]+items[int((len(items)+1)/2)])/2

    else: # length of the list is odd
        median= items[int(len(items)/2)]

    # return a dictionary
    return {'mean':round(items_array.mean(),2),
           'median':round(median,2),
           'variance':round(items_array.var(ddof=1),2),
           'standard deviation':round((items_array.var(ddof=1))**(1/2),2),
           'min':round(items_array.min(),2),
           'max':round(items_array.max(),2)}

### END FUNCTION

# Function 2: Five Number Summary
def five_num_summary(items):
    ''' Returns a dictionary of the five number summary.

        Keyword argument:
        items (list) -- a list of number values.

        Returns:
        dictionary: maximum value (max), median, minimum value (min),
                    first quartile (q1) and the third quartile (q3).

        Example:
        >>> five_num_summary([11,1,3,5,8,9,4,10,2,6,7])
            {'max': 11, 'median': 6, 'min': 1, 'q1': 3, 'q3': 8}
    '''
    # sort the list and create an array
    items.sort()
    items_array = np.array(items)

    med_index =(len(items)+1)/2

    if len(items)%2==0:
        # find the median
        median = (items[int((len(items)+1)/2)-1]+items[int((len(items)+1)/2)])/2

        # first quartile calculation
        q1_index = (int(med_index)+1)/2
        q1_value = (items[int(q1_index)]+items[int(q1_index-1)])/2

        # third quartile calculation
        q3_index = len(items)- q1_index + 1
        q3_value = (items[int(q3_index-2)]+items[int(q3_index-1)])/2

    else:
        median= items[int(len(items)/2)]

        q1_index = (int(med_index)+1)/2
        q1_value = items[int(q1_index)-1]

        q3_index = len(items) - q1_index + 1
        q3_value = items[int(q3_index)-1]

    # return a dictionary of the five number summary
    return {'max':round(items_array.max(),2),
            'median':round(median,2),
            'min':round(items_array.min(),2),
            'q1':round(q1_value,2),
            'q3':round(q3_value,2)}

### END FUNCTION
# Function 3: Date Parser
def date_parser(dates):
    ''' Returns a list of the dates

        Keyword argument:
        dates (list) - a list with the date & time string in the format:
                     'yyyy-mm-dd hh:mm:ss'

        Returns:
        list: list of string with the 'yyyy-mm-dd' date format

        Example:
        >>> date_parser(['2019-11-29 12:50:54', '2019-11-29 12:46:10'])
        ['2019-11-29', '2019-11-29']
    '''
    return[date.split(' ')[0] for date in dates]

### END FUNCTION

# Function 4: Municipality & Hashtag Detector
def extract_municipality_hashtags(df):
    ''' Returns a modified dataframe with two new columns.

        Keyword argument:
        df (pandas dataframe): pandas dataframe with Eskom dataframe

        Returns:
        dataframe: modified dataframe with 2 new columns 'municipality' and
                    'hastags'. The column data will be determined from the
                    initial 'df' dataframe.
    '''

    # clean the Date column to return the date only
    df['Date']=df['Date'].apply(lambda x: x.split(' ')[0])

    # define a function that will return the municipality name
    def mun_func(df):
        if '@CityofCTAlerts' in df:
            return mun_dict['@CityofCTAlerts']

        elif '@CityPowerJhb' in df:
            return mun_dict['@CityPowerJhb']

        elif '@eThekwiniM' in df:
            return mun_dict['@eThekwiniM']

        elif '@EMMInfo' in df:
            return mun['@EMMInfo']

        elif '@centlecutility' in df:
            return mun_dict['@centlecutility']

        elif '@NMBmunicipality' in df:
            return mun_dict['@NMBmunicipality']

        elif '@CityTshwane' in df:
            return mun_dict['@CityTshwane']
        else:
            return np.nan

    # create a new column 'municipality'
    df['municipality'] = df['Tweets'].apply(lambda y: mun_func(y))

    # define a function to find the # phrases from the 'Tweets' column
    def hh(df):
        
        uu = [] # empty list to store the hastag phrases
        if '#' in df:
            uu.append(df.split())
            rr=[]
            for mm in uu[0]:
                if '#' in mm:
                    rr.append(mm.lower())
            return rr

        # if there isn't any hashtags return 'NaN'
        else:
            return np.nan
            
    # create a new column 'hastags'
    df['hastags'] = df['Tweets'].apply(lambda y: hh(y))

    # return the modified dataframe
    return df

### END FUNCTION
