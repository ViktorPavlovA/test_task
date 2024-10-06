# Test Task 

## Create pipeline for image processing

### Install requirements

`pip3 install -r requrements.txt`

### Run

`python3 main.py`


### Project structure


```
│ 
├── .gitignore
├── main.py
├── modules
│   ├── binarization
│   │   ├── binarization_module.py
│   │   └── __init__.py
│   ├── invert
│   │   ├── __init__.py
│   │   └── invert_module.py
│   ├── light_leveling
│   │   ├── __init__.py
│   │   └── light_leveling_module.py
│   ├── resize
│   │   ├── __init__.py
│   │   └── resize_module.py
│   ├── pipeline_module.py
│   └── __init__.py
|
├── photo
│   └── test.png
├── readme.md
└── requrements.txt

```