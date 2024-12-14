#Write a program to fill in a letter template given below  with name and date 
letter = '''Dear <|Name|>,
your are seleected!
<|Date|>'''
           
print(letter.replace("<|Name|>","Abhy").replace("<|Date|>","24 september 2050"))