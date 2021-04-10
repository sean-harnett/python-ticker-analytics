# python-ticker-analytics

Command Line script that outputs a new mplFinance candlestick graph with specific indicators plotted along it. It takes
four inputs: (1) csv file location, (2) yaml file location, (3) ticker name, (4) destination folder.

### What are the inputs for?
    
The csv file location is a csv file containing data about a ticker. 
An example is in the MSFT.txt file.

The yaml file provided takes a specific format to determine what stock indicators to plot on the generated candlestick. For an example, see src/propertiesFiles/indicatorProperties.yaml.

The ticker name is given as the title of the graph.

Destination folder is where a png of the graph will be saved.
### Error reporting:
        
At the moment, only fatal errors will be thrown, and are outputted to the terminal in red, before the script exits with a python code of 1(failure).
