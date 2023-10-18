from langchain.document_loaders import TextLoader
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
loaders = UnstructuredURLLoader(urls=[
    "https://www.moneycontrol.com/news/business/markets/wall-street-rises-as-tesla-soars-on-ai-optimism-11351111.html",
    "https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html"
])
data = loaders.load()
text = """Interstellar is a 2014 epic science fiction film co-written, directed, and produced by Christopher Nolan. 
It stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Ellen Burstyn, Matt Damon, and Michael Caine. 
Set in a dystopian future where humanity is embroiled in a catastrophic blight and famine, the film follows a group of astronauts who travel through a wormhole near Saturn in search of a new home for humankind.

Brothers Christopher and Jonathan Nolan wrote the screenplay, which had its origins in a script Jonathan developed in 2007 and was originally set to be directed by Steven Spielberg. 
Kip Thorne, a Caltech theoretical physicist and 2017 Nobel laureate in Physics,[4] was an executive producer, acted as a scientific consultant, and wrote a tie-in book, The Science of Interstellar. 
Cinematographer Hoyte van Hoytema shot it on 35 mm movie film in the Panavision anamorphic format and IMAX 70 mm. Principal photography began in late 2013 and took place in Alberta, Iceland, and Los Angeles. 
Interstellar uses extensive practical and miniature effects, and the company Double Negative created additional digital effects.

Interstellar premiered in Los Angeles on October 26, 2014. In the United States, it was first released on film stock, expanding to venues using digital projectors. The film received generally positive reviews from critics and grossed over $677 million worldwide ($715 million after subsequent re-releases), making it the tenth-highest-grossing film of 2014. 
It has been praised by astronomers for its scientific accuracy and portrayal"""
"""splitter=CharacterTextSplitter(separator="\n",chunk_size=200,chunk_overlap=0)
chunks=splitter.split_text(text)
print(len(chunks))
for chunk in chunks:
    print(len(chunk))"""
r_splitter=RecursiveCharacterTextSplitter(separators=["\n\n","\n"," "],chunk_size=200,chunk_overlap=0)
chunks=r_splitter.split_text(data[0].page_content)
print(len(chunks))
for chunks in chunks:
    print(len(chunks))
"""Working of RecursiveCharacterTextSplitter"""
#chunks=text.split("\n\n")
#for chunks in chunks:
#    print(len(chunks))
#    
#first_split = text.split("\n\n")[0]
#print(len(first_split))#Recursive text splitter uses a list of separators, i.e. separators = ["\n\n", "\n", "."].So now it will first split using \n\n and then if the resulting chunk size is greater than the chunk_size parameter which is 200 in our case, then it will use the next separator which is \n.
#second_split = first_split.split("\n")
#for split in second_split:
#    print(len(split))#Third split exceeds chunk size 200. Now it will further try to split that using the third separator which is ' ' (space).
##When you split this using space (i.e. second_split[2].split(" ")), it will separate out each word and then it will merge those chunks such that their size is close to 200
#