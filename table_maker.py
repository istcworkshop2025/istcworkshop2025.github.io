import pandas as pd

df = pd.read_excel("the_file_2.xlsx")

markdown_table = df.to_markdown(index=False)

# Save the Markdown table to a file
with open("output_table_2.md", "w") as f:
    f.write(markdown_table)

print("Markdown table saved as output_table.md")
