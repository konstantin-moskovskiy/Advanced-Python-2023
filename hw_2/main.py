def generate_latex_table(data):
    with open('artifacts/table.tex', 'w') as f:
        f.write('\\begin{table}\n')
        f.write('\\centering\n')
        f.write('\\begin{tabular}{|')
        for i in range(len(data[0])):
            f.write('c|')
        f.write('}\n')
        f.write('\\hline\n')
        for i in range(len(data)):
            for j in range(len(data[i])):
                f.write(str(data[i][j]))
                if j != len(data[i]) - 1:
                    f.write(' & ')
                else:
                    f.write(' \\\\\n')
            if i == 0 or i == len(data) - 1: f.write('\\hline\n')
        f.write('\\end{tabular}\n')
        f.write('\\caption{Latex}\n')
        f.write('\\label{tab:latex_table}\n')
        f.write('\\end{table}\n')


data = [['Name', 'Age', 'Gender'],
    ['Andrew', '23', 'Male'],
    ['Jane', '50', 'Female'],
    ['Mark', '38', 'Male']]

generate_latex_table(data)
