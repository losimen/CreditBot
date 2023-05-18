import xlsxwriter


def init_folders():
    import os
    if not os.path.exists('reports'):
        os.makedirs('reports')


def create_file(user_id, history_all, type):
    workbook = xlsxwriter.Workbook(f'reports/{type}-{user_id}.xlsx')
    list_name = ['Загальне', 'Витрати', 'Доходи']
    worksheet = workbook.add_worksheet(list_name[0])
    worksheet.write(0, 0, 'Сума')
    worksheet.write(0, 1, 'Опис')
    worksheet.write(0, 2, 'Дата')

    i = 1
    for history in history_all:
        worksheet.write_number(i, 0, int(history.amount))
        worksheet.write(i, 1, history.description)
        worksheet.write_datetime(i, 2, history.date, workbook.add_format({'num_format': 'dd/mm/yy'}))
        i += 1

    chart = workbook.add_chart({'type': 'pie'})
    chart.add_series({
        'categories': f'={list_name[0]}!$B$2:$B${i}',
        'values': f'={list_name[0]}!$A$2:$A${i}',

        'line': {'color': 'blue'},
    })
    chart.set_title({'name': 'Загальний баланс'})
    chart.set_x_axis({'name': 'Дата'})
    chart.set_y_axis({'name': 'Сума'})
    worksheet.insert_chart('E2', chart)

    worksheet = workbook.add_worksheet(list_name[1])
    worksheet.write(0, 0, 'Сума')
    worksheet.write(0, 1, 'Опис')
    worksheet.write(0, 2, 'Дата')

    i = 1

    for expense in history_all:
        if int(expense.amount) < 0:
            worksheet.write_number(i, 0, int(expense.amount))
            worksheet.write(i, 1, expense.description)
            worksheet.write_datetime(i, 2, expense.date, workbook.add_format({'num_format': 'dd/mm/yy'}))
            i += 1

    chart = workbook.add_chart({'type': 'line'})
    chart.add_series({
        'values': f'={list_name[1]}!$A$2:$A${i}',
        'line': {'color': 'blue'},
    })

    chart.set_title({'name': 'Доходи'})
    chart.set_y_axis({'name': 'Сума'})
    worksheet.insert_chart('E2', chart)

    worksheet = workbook.add_worksheet(list_name[2])
    worksheet.write(0, 0, 'Сума')
    worksheet.write(0, 1, 'Опис')
    worksheet.write(0, 2, 'Дата')

    i = 1

    for income in history_all:
        if int(income.amount) > 0:
            worksheet.write_number(i, 0, int(income.amount))
            worksheet.write(i, 1, income.description)
            worksheet.write_datetime(i, 2, income.date, workbook.add_format({'num_format': 'dd/mm/yy'}))
            i += 1

    chart = workbook.add_chart({'type': 'line'})
    chart.add_series({
        'values': f'={list_name[2]}!$A$2:$A${i}',
        'line': {'color': 'blue'},
    })

    chart.set_title({'name': 'Витрати'})
    chart.set_y_axis({'name': 'Сума'})
    worksheet.insert_chart('E2', chart)

    workbook.close()
