# def my_print(*args, sep=" ", end="\n", file=None, flush=False):
#     text = ""
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = 80 - len(text) // 2
#     print(' ' * left_margin, text, end=end, file=file, flush=flush)
#
#
# with open('centered_text.txt','w') as file_to:
#     my_print('print this with tab to next',end='\t', file=file_to)
#     my_print('first','second',3,4, sep='->',file=file_to)
#     my_print('more I write the more it prints, but still in center', file=file_to)
#     my_print('first','second',3,4, file=file_to)


def my_centered_print(*args, sep=" "):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = 80 - len(text) // 2
    return ' ' * left_margin + text


print(my_centered_print('first','second',3,4,sep=' : '))

to_print = my_centered_print('more I write the more it prints, but still in center')
print(to_print)
