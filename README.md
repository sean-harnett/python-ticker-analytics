# python-ticker-analytics Cli

This is a simple command line script which plots indicators on candlestick charts, and saves the output. Specifically it outputs a new mplFinance candlestick graph with specific indicators plotted along it, using a few libraries.
It takes two inputs in the cli: (1) Location of a yaml properties file, which contains two fields (see below), and (2) a directory to save the resulting .png file(s). For a list of libraries used see requirements.txt.

### Usage:
    
Put the ticker csv files into a directory, and create two yaml files mimicking the structure of the two examples included in src/propertiesFiles (also outlined below).
The output is not distributed into sub-directories, all the pngs will be outputted into a single directory - this is by design.

### What are the inputs for?
    
The csv file location is a csv file containing data about a ticker.
An example is in the MSFT.txt file.

The csv file name is given as the title of the graph, along with subtitles of the indicators used.

Destination folder is where output of the graph(s) will be saved.


### Required Formats:
Csv files need to contain columns for: 'Date', 'Open', 'High', 'Low', 'Close'


####yaml format:
Yaml properties:
    
    file_properties:
        csv_source_directory: <path to directory>
        indicator_yaml_location: <path to file>
The indicator_yaml_location:
        
    indicators:
        EMA:
         use: True
         period: 2
         color: green

        ... next currently implemented indicators...

Both yaml files have examples in src/propertiesFiles/

All the indicators are calculated using the pandas-ta library, which I just call with wrapper functions, for the ones I need to use.



### Error reporting:
        
At the moment, only fatal errors will be thrown, and are outputted to the terminal in red, before the script exits with a python code of 1(failure).
