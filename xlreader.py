import xlrd
book = xlrd.open_workbook("backupdb.xls")
print("# numero de cosas {0}".format(book.nsheets))
print("nombre de pagina {0}".format(book.sheet_names()))
sh = book.sheet_by_index(2)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("info C11 : {0}".format(sh.cell_value(rowx=29, colx=2)))
for rx in range(sh.nrows):
    print(sh.row(rx))
