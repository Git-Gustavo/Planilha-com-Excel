import openpyxl
#Carregando arquivo
book = openpyxl.load_workbook('Planilha de Compras.xlsx')
#Selecionando uma página
frutas_page = book['Frutas']
#Imprimindo os dados de cada linha
for rows in frutas_page.iter_rows(min_row=2,max_row=5):
        #print(rows[0].value,rows[1].value,rows[2].value)
        for cell in rows:
                #print(cell.value)
                if cell.value =='Banana':
                        cell.value = 'Fruta 1'
#Sempre salvar caso queira alteração na planilha
book.save('Planilha de Compras.xlsx')