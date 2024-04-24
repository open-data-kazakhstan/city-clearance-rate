"# city-clearance-rate" 

## Installation

Clone the repository
```shell
$ https://github.com/open-data-kazakhstan/city-clearance-rate.git
```

Requires Python 3.11.3 

Create a virtual environment and activate it 
```bash
pip install venv
python -m venv /path/to/localrepo
```

Swicth to venv directory by using cd comand
```bash
cd /path/to/localrepo
Scripts/activate
```

Install dependecies in venv by using pip
```bash
pip install -r requirements.txt
```

Run the project:
```bash
python scripts/main.py
```

## Data 

Salary data collected by hand from qamqor.gov.kz stats: https://qamqor.gov.kz/crimestat/statistics

We downoladed data from this source and placed it in the data folders 

We have processed the source data to make it normalized and derived  several aggregated datasets from it:

* `data/output.csv` - final combined data
* `datapackage.json` - conatins all of the key information about our dataset

## Scripts

* `scripts/script.py` - our main script
* `datapack.py` - creating datapckage.json file that conatinsall meatadata

## License

This dataset is licensed under the Open Data Commons [Public Domain and Dedication License][pddl].

[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/


