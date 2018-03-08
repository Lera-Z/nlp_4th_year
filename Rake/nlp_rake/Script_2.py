from nlp_rake import rake

stoppath = 'data/stoplists/SmartStoplist.txt'

rake_object = rake.Rake(stoppath, 2, 3, 2)

sample_file = open("/Users/Valeriya/Documents/Py/nlp_4th_year/Rake/nlp_rake/text.txt", 'r', encoding="iso-8859-1")
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results

for num, i in enumerate(keywords):
    print(str(num))
    print(i)