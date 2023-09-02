from io import StringIO

import pandas as pd
import numpy as np

def p(msg):
    print(msg)
    print("\n")
    

url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"
p(pd.read_html(url))

html_str = """
         <table>
             <tr>
                 <th>A</th>
                 <th colspan="1">B</th>
                 <th rowspan="1">C</th>
             </tr>
             <tr>
                 <td>a</td>
                 <td>b</td>
                 <td>c</td>
             </tr>
         </table>
     """
     
with open("tmp.html", "w") as f:
    f.write(html_str)
    
df = pd.read_html("tmp.html")
p(df[0])

dfs = pd.read_html(StringIO(html_str))

p(dfs[0])

# https://pandas.pydata.org/docs/user_guide/io.html
