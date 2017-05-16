import re, string
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

#the regular expression of HTMLtags, @personName, URLs, numbers and 'NEWLINE'
regex_substr = [
        r'<[^>]+>', # HTML tags
        r'(?:@[\w_]+)', # @personName
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
        r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
        r'NEWLINE' #the special word 'NEWLINE'
        ]
    
regex_str = [
    emoticons_str,
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
del_re = re.compile(r'('+'|'.join(regex_substr)+')', re.VERBOSE | re.IGNORECASE)
hash_re = re.compile(r'(?:\#+)([\w_]+[\w\'_\-]*[\w_]+)') #Hashtags
punc_re = re.compile(r'[%s]' % re.escape(string.punctuation))
puncn_re = re.compile(r'[！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀\
｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟ … ‧﹏.]')
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    s = del_re.sub(r'', s) #delete HTMLtags, @personName, URLs, numbers and 'NEWLINE'
    s = hash_re.sub(r'\1', s) #delete hashtag but leaving the word after hashtag
    s = punc_re.sub(r'', s) #delete english punctuation
    s = punc_re.sub(r'', s) #delete chinese punctuation
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False): #make capital to lowercase except emoji token
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

with open('train_clean.csv', 'r', encoding='utf8') as f:
    for tweet in f:
        print (preprocess(tweet))