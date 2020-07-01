import xlsxwriter


class XLS:
    """
    Classe responsável por criar e preencher a planilha. O método build_xls preenche com dados default.
    Já o método write_mean_value é executado ao longo do programa com o objetivo de preencher a tabela
    com os valores médios.
    O método closse_sheet serve apenas para fechar a tabela
    """
    def __init__(self):
        self.workbook = None
        self.worksheet = None

    def build_xls(self):
        self.workbook = xlsxwriter.Workbook('Results.xlsx')  # Cria um arquivo chamado Results
        self.worksheet = self.workbook.add_worksheet()  # Adiciona uma planilha
        """Preenche com informações default"""
        self.worksheet.write('B1', 1000)
        self.worksheet.write('C1', 10000)
        self.worksheet.write('D1', 100000)
        self.worksheet.write('E1', 1000000)
        self.worksheet.write('F1', 10000000)
        self.worksheet.write('A2', 'Merge Sort')
        self.worksheet.write('A3', 'Buble Sort')
        self.worksheet.write('A4', 'Insertion Sort')
        self.worksheet.write('A5', 'Quick Sort')
        self.worksheet.write('A6', 'Counting Sort')

    def write_mean_value(self, column, mean_value):
        """Recebe o valor médio e preenche nas colunas respectivas"""
        self.worksheet.write('B'+column, mean_value[2])
        self.worksheet.write('C'+column, mean_value[3])
        self.worksheet.write('D'+column, mean_value[4])
        self.worksheet.write('E'+column, mean_value[5])
        self.worksheet.write('F'+column, mean_value[6])

    def close_sheet(self):
        """Fecha a planilha"""
        self.workbook.close()

