import numpy as np
import csv
import matplotlib.pyplot as plt

age_data = [(0,4,11.3), (5,9,10.5), (10,14,9.4), (15,19,9.7), (20,24,10.3), (25,29,9.7),
            (30,34,7.8), (35,39,6.1), (40,44,5.5), (45,49,5.0), (50,54,4.4), (55,59,3.6),
            (60,64,2.6), (65,69,1.8), (70,74,1.2), (75,100,1.3)]

def generate_ages(n=1000000):
    ages = []
    total_added = 0
    for i, (min_age, max_age, pct) in enumerate(age_data):
        if i == len(age_data) - 1:  # Last group gets remaining records
            count = n - total_added
        else:
            count = int(n * pct / 100)
        ages.extend(np.random.randint(min_age, max_age + 1, count))
        total_added += count
    np.random.shuffle(ages)
    return np.array(ages)

def save_csv(ages, filename="ages_data_new.csv"):
    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Age'])
            for age in ages: writer.writerow([age])
        print(f"Saved to {filename}")
    except PermissionError:
        print(f"Error: {filename} is locked. Close Excel/other programs using the file.")

def show_chart(filename="ages_data_new.csv"):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        ages = [int(row[0]) for row in reader]
    
    groups = [f"{min_age}-{max_age if max_age<100 else '+'}" for min_age, max_age, _ in age_data]
    pcts = [sum(1 for age in ages if min_age <= age <= max_age) / len(ages) * 100 
            for min_age, max_age, _ in age_data]
    
    plt.figure(figsize=(12, 6))
    plt.bar(groups, pcts, color='steelblue')
    plt.xlabel('Age Groups')
    plt.ylabel('Percentage (%)')
    plt.title('Age Distribution from CSV')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

np.random.seed(123)
ages = generate_ages()
filename = "ages_data_new.csv"
save_csv(ages, filename)
show_chart(filename)
print(f"Generated {len(ages):,} ages")
