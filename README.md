# IEC Voting Data Analysis

## Summary
A task given at the first Go Digital Data Analytics Hackerthon. Analysing the data of the National Elections in South Africa. In line with ci / cd, this project is still in progress and contributers are welcome
The objective this project aims to address:
1. Analysing voter registration vs turnout rates
2. Looking at individual parties and provinces they get majority of their votes


## Output ([gallery](project-output/Gallery.md))
![Demo](project-output/1.png)


## Features
- Automated script for cleaning the given spreadsheets
- Automated script for data analysis
- Bar graph plotting from data
- Pie chart plotting from data


## Data cleaning
An approach to properly clean and format the data was needed to be able to perform analysis on it. The data was cleaned and formatted using the following steps:
1. Removed all the columns with no data
2. Removed text and formatting not part of the data set
3. Converted all cells to strings
4. Removed rows with no data
5. Generating a cleaned csv file
6. From the cleaned csv file generating a formatted csv file


## System Requirements:
- A linux operating system
- Python3
- Pip


## Additional requirements:
- Internet access (for dependency installation)


## Getting Started
1. Clone the repository
2. Navigate to the project directory


## Setup:
1. Install dependencies
        
        sudo apt-get install python3-tk
        pip install -r dependencies/requirements.txt


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Contributor

Nkosikhona Mlaba (nkosimlaba397@gmail.com)