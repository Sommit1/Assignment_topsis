# Assignment_topsis
This repository contains the complete implementation of the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method as required in the assignment.
The assignment is implemented in three parts:

Part-I: Command Line TOPSIS Program

Part-II: Python Package uploaded on PyPI

Part-III: Web Service deployed on cloud

# Part-I: Command Line TOPSIS Implementation

# Description

A Python program that implements the TOPSIS algorithm and runs from the command line.
The program reads a CSV file, applies TOPSIS using user-defined weights and impacts, and generates a ranked output file.

# Usage

python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>

# Validations Implemented

Correct number of parameters

File not found handling

Minimum three columns required

Numeric validation for criteria columns

Equal number of weights, impacts, and criteria

Impacts must be + or -

Comma-separated weights and impacts

# Input
<img width="339" height="365" alt="Screenshot 2026-02-04 010422" src="https://github.com/user-attachments/assets/839efac2-bed8-4210-8a15-24124665c566" />

# Output
<img width="568" height="349" alt="Screenshot 2026-02-04 010519" src="https://github.com/user-attachments/assets/81fb5ea5-24a2-4edc-8ab8-317123248c7c" />

# Notebook link

https://1drv.ms/f/c/1ede860e09d7ceb6/IgDW0-8_FX_8RbRsE_Pq4YI6AY4ksL4STxqAP3wKXKN6cMk?e=xuLoi5



# Part-II: Python Package (PyPI)

# Description

The TOPSIS program is converted into a Python package and uploaded to PyPI following the given naming convention.

-> Package Name

Topsis-Sommit-102303184

-> Installation

pip install Topsis-Sommit-102303184

-> Usage

topsis Data.csv "1,1,1,2" "+,+,-,+" output.csv

# PyPI Package Link

https://pypi.org/project/Topsis-Sommit-102303184/



# Part-III: TOPSIS Web Service

# Description

A web-based TOPSIS service developed using Flask and deployed on the Render cloud platform.

The user can:

Upload a CSV file

Enter weights and impacts

Enter an email ID

Obtain the TOPSIS result file

# Web Input Example

<img width="391" height="366" alt="image" src="https://github.com/user-attachments/assets/a0598c29-81dc-4ba1-8d44-d6a4722496a1" />


# Result Delivery

Email functionality implemented

On free cloud hosting, outbound SMTP may be restricted

Therefore, a direct download link for the result CSV is provided as a fallback

# Live Web Service Link

https://topsis-web-dt2l.onrender.com

# Project Structure

<img width="524" height="536" alt="image" src="https://github.com/user-attachments/assets/f375c86c-b8ea-4d15-be90-0ab85fb3338e" />


# Author

Sommit

