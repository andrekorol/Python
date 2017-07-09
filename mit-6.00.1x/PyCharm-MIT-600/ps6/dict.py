class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        dict1 = {}
        str1 = string.ascii_uppercase
        for s in str1:
            if (ord(s)+shift-65) < 26 :
                dict1[s] = chr(ord(s)+shift)
            elif (ord(s)+shift-65) >= 26 :
                dict1[s] = chr(ord(s)+shift-26)

        str1 = string.ascii_lowercase
        for s in str1:
            if (ord(s)+shift-97) < 26 :
                dict1[s] = chr(ord(s)+shift)
            elif (ord(s)+shift-97) >= 26 :
                dict1[s] = chr(ord(s)+shift-26)

        return dict1    

    def apply_shift(self, shift):
        msg = self.get_message_text()
        newMsg = ""
        dict1 = self.build_shift_dict(shift)
        for i in range(len(msg)):
            if dict1.has_key(msg[i]):
                newMsg += dict1.get(msg[i])
            else:
                newMsg += msg[i]
        return newMsg