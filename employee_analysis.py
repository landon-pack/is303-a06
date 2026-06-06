'''
Landon Pack
Is-303 A06

Employee Satisfaction Survey Data Analysis
-Clean and analyze employee satisfaction data


Inputs: employee_survey.csv 50 rows, 9 columns (employee_id, department, role, years_at_company, satisfaction, work_life_balance, growth_opportunities, would_recommend, salary_range)   )

Processes:- 
- load_data(): reads CSV into DataFrame
- clean_data(): drops rows with missing data, standardizes the format for the department and would recommend columns to be in title case
- validate_data(): asserts that there are no empty rows and that the department and would recommend columns are in titlecase
- analyze_data(): uses groupby statements to grab data and then prints the average satisfaction by salary and the average work life balance by department
- create_chart(): creates a chart titled "Average Employee Satisfaction by Salary" 

Outputs: 
-Average satisfaction by salary (Printed table)
-Average work life balance by departmenet(Printed table)
-Bar chart saved as satisfaction_by_salary.png


'''
import pandas as pd 
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("employee_survey.csv")
    print (f"Loaded {len(df)} rows from employee_survey.csv")
    return df


def clean_data(df):
    df = df.dropna()
    df["department"] = df["department"].str.title()
    df["would_recommend"] = df["would_recommend"].str.title()
    df["salary_range"] = df["salary_range"].str.replace("$", "", regex = False)
    print(f"After cleaning: {len(df)} rows")
    return df
def validate_data(df):
    assert df.notna().all().all(), "There are still null values in the dataset"
    assert "MARKETING" not in df["department"].values, "The department column still needs to be put into titlecase"
    assert "YES" not in df["would_recommend"].values, "The would recommend column still has values that aren't in titlecase."
def analyze_data(df):
    satisfaction_by_salary = df.groupby("salary_range")["satisfaction_1_10"].mean()
    print("====Average employee satisfaction rate by salary====")
    print(satisfaction_by_salary.round(2))

    work_balance_by_department = df.groupby("department")["work_life_balance_1_10"].mean()
    print("\n====Average Work Life Balance by Department ====")
    print(work_balance_by_department.round(2))

    return satisfaction_by_salary

def create_chart(satisfaction_by_salary):
    salary_order = ["40k-60k", "60k-80k", "80k-100k", "100k-120k", "120k+"]
    satisfaction_by_salary = satisfaction_by_salary.reindex(salary_order)
    satisfaction_by_salary.plot(kind="bar", color = "lightblue")
    plt.title("Average Employee Satisfaction by Salary")
    plt.xlabel("Salary Range")
    plt.ylabel("Employee Satisfaction")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.savefig("satisfaction_by_salary.png")
    plt.show()
    print("Chart saved as satisfaction_by_salary.png")



# Main flow



df = load_data()
df = clean_data(df)
validate_data(df)
satisfaction_by_salary = analyze_data(df)
create_chart(satisfaction_by_salary)