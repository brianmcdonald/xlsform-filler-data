# XLSform filler data

A commandline tool for creating dummy/test data from XLSform surveys.

## Installation
```pip install xlsform-filler-data```

## Usage
To create a dummy dataset, with a default number of rows(100) from a XLSform source:
```xlsform-filler-data <source-file-path>/<filename.xlsx>```

To specify the number of rows to create, use the *-r* flag. Example:
```xlsform-filler-data <source-file-path>/<filename.xlsx> -r 200```

To specify the output path and filename, pass the *-o* flag. Example:
```xlsform-filler-data <source-file-path>/<filename.xlsx> -o <./myfile.xlsx>```

## Roadmap
As of version *0.1.1* the tool does not properly randomise multiple choice questions; omits some variables such as 'start' and 'end'; does not maintain the order of the variables; and does not incorporate constraints or cascading choice lists. These limitations will be adddressed in future releases.