from nltk.tokenize import sent_tokenize

text = """I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in
the history of our nation. Five score years ago, a great American, in whose symbolic shadow we stand today, signed the 
Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who 
had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long 
night of their captivity. But one hundred years later, the Negro still is not free. One hundred years later, 
the life of the Negro is still sadly crippled by 
the manacles of segregation and the chains of discrimination. One hundred years later, the Negro lives on a lonely 
island of poverty in the midst of a vast ocean of material prosperity. One hundred years later, the Negro is still 
languished in the corners of American society and finds 
himself an exile in his own land. And so we've come here today to dramatize a shameful condition. In 
a sense we've come to our nation's capital to cash a check. When the architects of our republic wrote the magnificent 
words of the Constitution and the Declaration of Independence, they were signing a promissory note to which every 
American was to fall heir. This note was a promise that all men, yes, black men as well as white men, would be 
guaranteed the "unalienable Rights" of "Life, Liberty and the pursuit of Happiness." It is obvious today that 
America has defaulted on this promissory 
note, insofar as her citizens of color are concerned. Instead of honoring this sacred obligation, 
America has given the Negro people a bad check, a check which has come back marked "insufficient funds." """


def gen_split_overlap(text_input, chunk_size, overlap):
    if chunk_size < 1 or overlap < 0:
        raise ValueError('size must be >= 1 and overlap >= 0')

    for i in range(0, len(text_input) - overlap, chunk_size - overlap):
        yield text_input[i:i + chunk_size]


print(sent_tokenize(text))

