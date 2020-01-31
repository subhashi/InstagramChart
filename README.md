# Instragram Data to Chart

Draw a bar chart of a given public Instagram account

>Note: Only works for public Instagram accounts

## How to run

Assign the account to `IGACCOUNTNAME` to run the project with a desired account

## Function description

- findDataInIg(igAccountName)

    Find followers, following and posts of a given public Instagram account. Account name is passed as a parameter.

    `igAccountName`: Instagram account username

    eg: eye.tattoo.girl

- cleanNumbers(numericValue)

    If the numeric values contain m, k or ',', convert them to int values

    `numericValue`: Raw string values of numeric data

    eg: 1.3m, 1,340, 13k

- drawBarChart(y_data, fetchedData, igAccount)

    Draw the bar chart.

    `y_data`: A list of numbers of followers, following and posts
    `fetchedData`: The raw strings of followers, following and posts inclusing 'm', 'k', and ','
    `igAccount`: Instagram account username
    
    
    
