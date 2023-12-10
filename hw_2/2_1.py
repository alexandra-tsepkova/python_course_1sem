def generate_latex_table(rows):
    columns_num = len(rows[0])

    rows_formatted = [' & '.join(map(str, row)) for row in rows]

    table = r'\begin{tabular}{'\
            f'|{"|".join(["c" for _ in range(columns_num)])}|'\
            '}\n\\hline\n'
    for row in rows_formatted:
        table += row
        table += ' \\\\ \n\\hline\n'
    table += r'\end{tabular}'

    return table
