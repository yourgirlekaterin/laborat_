# TODO Найдите количество книг, которое можно разместить на дискете
value = 1.44 # объем дискеты в мегабайтах
count_of_pages = 100 # количество страниц в книге
count_of_str = 50 # число строк на странице
count_of_sym = 25 # число символов на строке

value_in_bytes = value * 1024 * 1024 # объем дискеты в байтах
mem_sym = count_of_sym * 4 # хранение символов в книге
mem_str = mem_sym * count_of_str # хранение строк
mem_pag = mem_str * count_of_pages # хранение страниц
count_of_books = round(value_in_bytes / 500000, )
print("Количество книг, помещающихся на дискету:", count_of_books)
