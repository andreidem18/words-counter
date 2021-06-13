import json

class File:
    text = ""
    def __init__(self, file_name):
        self.file_name = file_name
        self.get_file()
        
    def get_file(self):
        self.text = open(f"./texts/{self.file_name}.txt", encoding="utf-8").read()
        
    def get_words(self):
        map = {
            ord('.'): None,
            ord(','): None,
            ord('-'): None,
            ord('¿'): None,
            ord('?'): None,
            ord('¡'): None,
            ord('!'): None,
        }
        return self.text.lower().translate(map).split()
        
    def get_top(self, top_num):
        words = self.get_words()
        words_dict = dict()
        
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1
            
        words_tuples = sorted([(v, k) for k, v in words_dict.items()], reverse = True)[:top_num]
        words_dict = dict()
        
        for k, v in words_tuples:
            words_dict[v] = k
        return json.dumps(words_dict, indent=3)
