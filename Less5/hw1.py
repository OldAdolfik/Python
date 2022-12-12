example = 'шозртзшор абв шототыавш абв гршзоабв абвщшршг'
result = ' '.join(list(filter(lambda x: not 'абв' in x, example.split())))
print(result)