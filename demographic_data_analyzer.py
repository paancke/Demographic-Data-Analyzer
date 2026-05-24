import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult_data.csv', skipinitialspace=True)  
    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    ## Q1 How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    race_count.index.name = None

    ## Q2 What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    ## Q3 What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df['education'].value_counts(normalize=True)['Bachelors'] * 100, 1)

    ## Q4 What percentage of people with advanced education make more than 50K?
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_edu]['salary'] == '>50K').mean() * 100, 1)

    ## Q5 What percentage of people without advanced education make more than 50K?
    lower_education_rich = round((df[~higher_edu]['salary'] == '>50K').mean() * 100, 1)

    ## Q6 What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    ## Q7 What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    ## Q8 What country has the highest percentage of people that earn >50K and what is that percentage?
    cty_count = df['native-country'].value_counts()
    cty_rich_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    percent_cty_rich = (cty_rich_count / cty_count * 100).fillna(0)    
    highest_earning_country = percent_cty_rich.idxmax()
    highest_earning_country_percentage = round(percent_cty_rich.max(), 1)

    ## Q9 Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # DO NOT MODIFY: Optional terminal print function built into freeCodeCamp template
    if print_data:
        print("People each race:\n", race_count)
        print(f"Average age of men: {average_age_men}")
        print(f"Percentage with Bachelor's degree: {percentage_bachelors}%")
        print(f"Percentage with advanced education that make more than 50K: {higher_education_rich}%")
        print(f"Percentage without advanced education that make more than 50K: {lower_education_rich}%")
        print(f"Minimum number of hours of work per week: {min_work_hours}")
        print(f"Percentage who work minimum hours per week with salary more than 50K: {rich_percentage}%")
        print(f"Highest earning country: {highest_earning_country}")
        print(f"Highest earning country percentage: {highest_earning_country_percentage}%")
        print(f"Top occupation for high earners in India: {top_IN_occupation}")

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
