# Generating dataset
import pandas as pd
# dictionary words
sf = pd.read_csv("words.txt")
sf["scribble"] = False
sf["label"] = "word"
#scribble words
nsf = pd.read_csv("scibble.txt")
nsf["scribble"] = True
nsf["label"] = "scribble"
word_list = [sf, nsf]
bulk = pd.concat(word_list)
bulk.to_csv("scribble_data.txt")