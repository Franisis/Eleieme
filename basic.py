import lexer
while True:
    text = input ('basic >')
    result, error = lexer.run(text)

    if error: print (error.as_string()) 
    else: print(result)
    