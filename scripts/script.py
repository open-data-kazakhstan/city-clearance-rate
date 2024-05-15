
import openpyxl
import csv

# Список путей к файлам Excel и соответствующих регионов
excel_files = [
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Shymkent city.XLSX", 'region': 'Shymkent city'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Turkistan region.XLSX", 'region': 'Turkistan Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Ulytau region.XLSX", 'region': 'Ulytau Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\West Kazakhstan region.XLSX", 'region': 'West Kazakhstan Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Jambyl region.XLSX", 'region': 'Jambyl Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Jetisu region.XLSX", 'region': 'Jetisu Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Abay region.XLSX", 'region': 'Abai Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Akmola region.XLSX", 'region': 'Akmola Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Aktobe region.XLSX", 'region': 'Aktobe Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Almaty city.XLSX", 'region': 'Almaty city'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Almaty region.XLSX", 'region': 'Almaty Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Astana city.XLSX", 'region': 'Astana city'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Atyrau region.XLSX", 'region': 'Atyrau Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\East Kazakhstan region.XLSX", 'region': 'East Kazakhstan Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Karaganda region.XLSX", 'region': 'Karaganda Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Kostanay region.XLSX", 'region': 'Kostanay Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Kyzylorda region.XLSX", 'region': 'Kyzylorda Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Mangystau region.XLSX", 'region': 'Mangystau Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\North Kazakhstan region.XLSX", 'region': 'North Kazakhstan Region'},
    {'path': r"C:\Users\USER\Desktop\practice\city-clearance-rate\archive\Pavlodar region.XLSX", 'region': 'Pavlodar Region'},

    # Добавьте остальные файлы и их регионы по аналогии
]


# Открываем CSV файл для записи
with open(r'C:\Users\USER\Desktop\practice\city-clearance-rate\data\output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Записываем заголовки столбцов
    writer.writerow(["Region", "Value"])

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
                writer.writerow([region, row[9].value])  # Значения столбцов "Год" и "Выявлено лиц, совершивших уголовные правонарушения"
                break


print("Преобразование завершено.")