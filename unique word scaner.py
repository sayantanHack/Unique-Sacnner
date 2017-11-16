
print "OPENing a new file."
fname = raw_input("Enter file name: ")
file_text = open(fname,"r")
file_read = file_text.read()
file_text.close()
unique_list = []
word_list=file_read.split()

for word in word_list:
    if word not in unique_list:
        unique_list.append(word)   

print  word_list        # word list with duplication
print  unique_list          # word list without redundency

