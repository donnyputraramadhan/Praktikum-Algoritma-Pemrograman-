data = "ini adalah string"
print(data)
print(type(data))
# 1. cara membuat string
'''
1. dengan menggunakan single quote'...'
2. dengan menggunakan double qoute"..."
'''
data = 'menggunakan single qoute'
print(data)
data = 'menggunakan single qoute'
print(data)
print("halo, apa kabar?")
print("halo, apa kabar?")
print("nama saya ucok")
# 2. menggunakan tanda \
# membuat tannda' menjadi string
print("mari shalat jum\'at")
print('g\'day,isn\'t it')
# backlash
print("c:\\user\\ucok")
# tab
print("ucok\t\t\totong, semakin jauhan")
# backspace
print("ucok \botong, jadi deketan")
# newline
print("baris pertama.\nbaris kedua.") # lf -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # cr -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # crlf -> line feed carriage return -> dipakai oleh windows
# 3. string literal atau raw
# hati-hati
print('c:\new foleder') # akan salah pathnya
# menggunakan raw string
print(r'c:\new folder')
# multiline literal string
print("""
nama : ucok
kelas : kuliah
""")
# multiline literal string dan raw
print(r"""
nama : ucok
kelas : kuliah \ new normal
website : www.ucok.com/newid
""")
