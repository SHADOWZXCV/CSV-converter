"""

    @author: Ezzeldin Husen
    @package: csv_to_json
    @version: 0.0.15
    @description: A module that converts csv files to formated JSON readable files
    @dependencies: { regex }

"""
from lib.path import extractAllCsv

# All available csv files on `Ready` folder, are going to be converted and added to `Extracted` folder.
# Standard separator: ,
# Examples of non-standard separators: ( ; : )
# Note: all csv files that have non-standard separators must pass its details as an argument like below, 
# otherwise the conversion would not return the expected results!
extractAllCsv([{ 'name': 'email.csv', 'separator': ';' }])
