from nlp_rake import rake

stoppath = 'data/stoplists/SmartStoplist.txt'

# rake_object = rake.Rake(stoppath, 1, 3,2) #для улучшенной версии
rake_object = rake.Rake(stoppath, 1, 3,1)

sample_file = open("/Users/Valeriya/Documents/Py/nlp_4th_year/Rake/nlp_rake/text.txt", 'r', encoding="iso-8859-1")
# sample_file = open("/Users/Valeriya/Documents/Py/nlp_4th_year/Rake/nlp_rake/russian.txt", 'r', encoding="utf8")

text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
kw = []
for num, i in enumerate(keywords):
    kw.append(i)

for w in kw[:15]:
    print(w)
