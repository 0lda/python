

# text = 'This is my first test.\nThis is the second line.\nThis the third line. '
#
# append_text = '\nThis is appended file.'
#
# my_file = open('my file.txt', 'a')
# # w = wirte r=read
# my_file.write(append_text)
# my_file.close()


file = open('my file.txt', 'r')
content = file.readline()
second_read_time = file.readline()
# python_list = [1, 2, 3, 4, 5, 'lda', 'py']
print(content, second_read_time)

file.close()
