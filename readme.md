# Usage

## Environment Setup

In a powershell:

```bash
> conda create -n snowflake_env
> conda activate snowflake_env
> conda install -c conda-forge snowflake-connector-python
```

## Running Script

In a python script, run the following:

```python
from snowflake_connect import Snowflake

user=<insert username>
password=<insert password>
account=<insert account: 'petco.us-east-1'>

query = """
    select * 
    from WHPRD_VW.DWADMIN.FT_UPC_SLS_PALS
    limit 10;
"""

db = Snowflake(user, password, account)
df = db.pyql(query)
print(df.head())
```