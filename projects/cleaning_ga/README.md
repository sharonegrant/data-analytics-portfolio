\# Customer Orders — Data Cleaning \& QA Showcase



\*\*Goal\*\*

\- Turn a messy CSV export into an analysis-ready dataset for dashboards and modeling.

\- Fix data types, handle missing values, remove duplicates, and standardize categories/dates.

\- Document decisions and prove quality with simple, auditable checks.



\*\*Inputs\*\*

\- `data/raw/orders\_raw.csv` — a sample raw export with columns like:

&nbsp; `order\_id`, `customer\_id`, `order\_date`, `ship\_date`, `status`, `quantity`, `unit\_price`, `discount`, …



\*\*Outputs\*\*

\- `outputs/data/orders\_clean.csv` — cleaned, tidy table (one row = one order).

\- `outputs/reports/profile.html` — HTML profiling report (distributions, missingness, warnings).

\- `projects/cleaning\_ga/notebooks/01\_cleaning.ipynb` or `projects/cleaning\_ga/src/cleaning.py` — full workflow.



\*\*Quality checks\*\*

\- \*\*Keys\*\*: `order\_id` unique and not null.

\- \*\*Types\*\*: `order\_date`/`ship\_date` parsed to dates; numeric fields coerced to numbers.

\- \*\*Allowed values\*\*: `status ∈ {shipped, pending, cancelled}`.

\- \*\*Hygiene\*\*: trimmed strings; consistent casing; duplicates removed.



\*\*How to run\*\*

```bash

\# (optional) create a virtual env

python -m venv .venv

source .venv/Scripts/activate  # on Windows Git Bash



\# install requirements (add profiling if needed)

pip install -r requirements.txt || (echo pandas>>requirements.txt \& echo ydata-profiling>>requirements.txt \& pip install -r requirements.txt)



\# put a sample file at:

\# data/raw/orders\_raw.csv



\# run the script (or open the notebook)

python projects/cleaning\_ga/src/cleaning.py

```



\*\*Before → After snapshot (fill in after first run)\*\*

\- Rows: `\[raw\_count]` → `\[clean\_count]` (removed `\[n]` duplicates)

\- Nulls in critical fields: `order\_id` `\[x%→0%]`, `order\_date` `\[y%→0%]`

\- Invalid `status` values: `\[k]` → `0`

\- Type fixes: `\[list of columns]` cast to `date/float/int`



