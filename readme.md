# Usage

## Environment Setup

### USING CONDA

In a powershell:

```bash
> conda create -n snowflake_env
> conda activate snowflake_env
> conda install -c conda-forge snowflake-connector-python
```

### USING PIP

```bash
> python -m venv venv
> source venv/bin/activate
(venv) > pip install --upgrade pip
(venv) > pip install -r requirements.txt
```
## Running Script

In a python script, run the following:

```python
from snowflake_connect import Snowflake

user=<insert username>
password=<insert password>
account=<insert account>

query = """
    select * 
    from WHPRD_VW.DWADMIN.FT_UPC_SLS_PALS
    limit 10;
"""

db = Snowflake(user, password, account)
df = db.pyql(query)
print(df.head())
```