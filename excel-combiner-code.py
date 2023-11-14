import pandas as pd

df = pd.concat(pd.read_excel(r'/Users/sparshgarg/Downloads/FILE_5721.xlsx', skiprows=[0], sheet_name = None), ignore_index=True)

writer = pd.ExcelWriter('new_file.xlsx')
df.to_excel(writer, sheet_name='my_analysis', index=False, na_rep='NaN')
for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['my_analysis'].set_column(col_idx, col_idx, column_width)

writer.save()
