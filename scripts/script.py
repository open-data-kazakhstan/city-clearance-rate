
import openpyxl
import csv

# Список путей к файлам Excel и соответствующих регионов
excel_files = [
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Shymkent.XLSX", 'region': 'Shymkent city'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Turkestan_reg.XLSX", 'region': 'Turkestan region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Ulytau_reg.XLSX", 'region': 'Ulytau region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\WestKaz_reg.XLSX", 'region': 'West-Kazakhstan region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Zhambyl_reg.XLSX", 'region': 'Zhambyl region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Zhetysu_reg.XLSX", 'region': 'Zhetisu region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Abay_reg.XLSX", 'region': 'Abay region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Akmola_reg.XLSX", 'region': 'Akmola region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Aktobe_reg.XLSX", 'region': 'Aktobe region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Almaty.XLSX", 'region': 'Almaty city'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Almaty_reg.XLSX", 'region': 'Almaty region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Astana.XLSX", 'region': 'Astana city'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Atyrau_reg.XLSX", 'region': 'Atyrau region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\EastKaz_reg.XLSX", 'region': 'East-Kazakhstan region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Karagandy_reg.XLSX", 'region': 'Karagandy region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Kostanay_reg.XLSX", 'region': 'Kostanay region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Kyzylorda_reg.XLSX", 'region': 'Kyzylorda region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Mangistau_reg.XLSX", 'region': 'Mangistau region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\NortKaz_reg.XLSX", 'region': 'North-Kazakhstan region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Pavlodar_reg.XLSX", 'region': 'Pavlodar region'},

    # Добавьте остальные файлы и их регионы по аналогии
]


# Открываем CSV файл для записи
with open(r'C:\Users\USER\Desktop\practice\city-clearance-rate\data\output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Записываем заголовки столбцов
    writer.writerow(["Region", "Year", "Found criminals"])

    # Обходим каждый файл Excel и его регион
    for item in excel_files:
        excel_file = item['path']
        region = item['region']
        
        # Открываем Excel файл
        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active

      # Поиск строки, начинающейся с "Всего"
        for row in sheet.iter_rows():
            if row[0].value == 'Всего':
                # Записываем данные из нужных столбцов в CSV
                writer.writerow([region, 2023, row[6].value])  # Значения столбцов "Год" и "Выявлено лиц, совершивших уголовные правонарушения"
                break


print("Преобразование завершено.")