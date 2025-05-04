import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def xl2sql(xl_file, output_file):
    try:
        xls = pd.ExcelFile(xl_file)
        sql = "set define off;\n"

        for sheet in xls.sheet_names:
            df = pd.read_excel(xl_file, sheet_name=sheet)
            col_with_dt = []

            for col_name, dtype in df.dtypes.items():
                if dtype == 'int64' or dtype == 'float64':
                    col_with_dt.append(f'{col_name} NUMBER')
                elif dtype == 'object':
                    max_length = df[col_name].apply(lambda x: len(str(x)) if x is not None else 0).max()
                    col_with_dt.append(f'{col_name} VARCHAR({max_length if max_length < 255 else 255})')
                elif dtype == 'datetime64[ns]':
                    col_with_dt.append(f'{col_name} DATE')

            col_sql = ", ".join(col_with_dt)
            sql += f"CREATE TABLE {sheet.lower()} ({col_sql});\n"

            # Prepare INSERT statements in a more efficient manner
            for row in df.itertuples(index=False, name=None):
                values = []
                for val, col_type in zip(row, df.dtypes):
                    if col_type == 'datetime64[ns]':
                        values.append(f"TO_DATE('{val.strftime('%d-%m-%Y')}', 'DD-MM-YYYY')")
                    elif isinstance(val, str):
                        values.append(f"'{val}'")
                    else:
                        values.append(str(val))
                val_sql = ", ".join(values)
                sql += f'INSERT INTO {sheet.lower()} ({", ".join(df.columns)}) VALUES ({val_sql});\n'

            sql += "COMMIT;\n"

        # Write to output file
        with open(output_file, 'w') as f:
            f.write(sql)
        logging.info(f"Schema conversion completed successfully, SQL written to {output_file}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.info("DEVELOPED WHOLLY & SOLELY BY FURQAN AHMED 22FA-006-CS")

    excel_file = "Employee Data.xlsx"
    output_file = "data.sql"

    xl2sql(excel_file, output_file)