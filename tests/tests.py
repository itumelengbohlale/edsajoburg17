from edsajoburg17 import myModule

# test the dictionary metrics function
def test_dictionary_of_metrics():
    '''
    Test if dictionary_of_metrics functions works correctly
    '''
    assert myModule.dictionary_of_metrics([1,2,3,4,5]) ==  {'mean': 3.0,
        'median': 3.0, 'var': 2.5, 'std': 1.58, 'min': 1, 'max': 5},
        'incorrect'

    assert myModule.dictionary_of_metrics([25,25,8,7,8,9,6,2,5,8,9,6,2,5,2,4])==
    {'mean': 8.19, 'median': 6.5, 'var': 48.7, 'std': 6.98, 'min': 2,
    'max': 25}, 'incorrect'

# test the five number summary funaction
def test_five_num_summary():
    '''
    Test if the five number summary function works properly.
    '''
    assert myModule.five_num_summary([1,2,3,4,5,6,7,8,9,10,11]) == {'max': 11,
        'median': 6.0, 'min': 1, 'q1': 3.5, 'q3': 8.5}, 'incorrect'

    assert myModule.five_num_summary([11,785,15214,415,8889,12548,1000,1250,35,
                8,7,900,10504]) == {'max': 15214, 'median': 900.0, 'min': 7,
                'q1': 35.0, 'q3': 8889.0}, 'incorrect'

# test the date parser function
def test_date_parser():
    '''
    Test if the date parser function works properly.
    '''
    assert myModule.date_parser(['2019-11-29 12:50:54','2019-11-29 12:46:53',
    '2019-11-29 12:46:10'])== ['2019-11-29', '2019-11-29', '2019-11-29'],
    'incorrect'

    assert myModule.date_parser(['2015-12-20 11:05:01','2030-11-02 10:05:41'])==
    ['2015-12-20','2030-11-02'], 'incorrect'

# test the municipality_hashtags function
def test_extract_municipality_hashtags():
    '''
    Test if the extract municipality and hashtags function works properly.
    '''
    assert myModule.extract_municipality_hashtags(twitter_df.copy())['hashtags'].loc[4] ==
    ['#eskomfreestate', '#mediastatement'], 'incorrect'

    assert myModule.extract_municipality_hashtags(twitter_df.copy())['municipality'].loc[5] ==
    'Johannesburg', 'incorrect'

# test the number of tweets function
def test_number_of_tweets_per_day():
    '''
    Test if the number_of_tweets_per_day function works properly.
    '''
    assert myModule.number_of_tweets_per_day(twitter_df.copy())['Tweets'].loc['2019-11-20'] == 18,
    'incorrect'
    assert myModule.number_of_tweets_per_day(twitter_df.copy())['Tweets'].loc['2019-11-26'] == 32,
    'incorrect'

# test the word splitter function
def test_word_splitter():
    '''
    Test if the word splitter function works properly.
    '''
    assert myModule.word_splitter(twitter_df.copy())['Split Tweets'].loc[2] ==
    ['@bongadlulane', 'query', 'escalated', 'to', 'media', 'desk.'], 'incorrect'

    assert myModule.word_splitter(twitter_df.copy())['Split Tweets'].loc[90] ==
    ['rt','@sagovnews:', 'president', '@cyrilramaphosa', 'is', 'this', 'morning',
    'at', 'eskom’s', 'flagship', 'medupi', 'power', 'station.', 'he', 'will',
    'tour', 'the', 'plant', 'and', 'later', 'address…'], 'incorrect'

# test the stop_words remover function
def test_stop_words_remover():
    '''
    Test if the stop_words_remover function works correctly.
    '''
    assert myModule.stop_words_remover(twitter_df.copy())['Without Stop Words'].loc[42]==
    ['rt','@citypowerjhb:','#westfieldplannedoutage','progress','16:00.',
    'note',"it's",'necessary', 'essential', 'maintenance', 'work','ou…'],
    'incorrect'

    assert myModule.stop_words_remover(twitter_df.copy())['Without Stop Words'].loc[1] ==
    ['@saucy_mamiie', 'pls', 'log', '0860037566'], 'incorrect'
