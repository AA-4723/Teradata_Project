# Age Data Generator using NumPy
import numpy as np
import csv

def generate_age_data(num_rows=1000000):
    """
    Generate random ages based on detailed age distribution:
    0–4: 11.3%, 5–9: 10.5%, 10–14: 9.4%, 15–19: 9.7%, 20–24: 10.3%,
    25–29: 9.7%, 30–34: 7.8%, 35–39: 6.1%, 40–44: 5.5%, 45–49: 5.0%,
    50–54: 4.4%, 55–59: 3.6%, 60–64: 2.6%, 65–69: 1.8%, 70–74: 1.2%, 75+: 1.3%

    Args:
        num_rows (int): Number of age records to generate

    Returns:
        numpy.ndarray: Array of random ages
    """
    # Define age ranges and their probabilities (as percentages)
    age_groups = [
        (0, 4, 11.3),    # 0-4 years: 11.3%
        (5, 9, 10.5),    # 5-9 years: 10.5%
        (10, 14, 9.4),   # 10-14 years: 9.4%
        (15, 19, 9.7),   # 15-19 years: 9.7%
        (20, 24, 10.3),  # 20-24 years: 10.3%
        (25, 29, 9.7),   # 25-29 years: 9.7%
        (30, 34, 7.8),   # 30-34 years: 7.8%
        (35, 39, 6.1),   # 35-39 years: 6.1%
        (40, 44, 5.5),   # 40-44 years: 5.5%
        (45, 49, 5.0),   # 45-49 years: 5.0%
        (50, 54, 4.4),   # 50-54 years: 4.4%
        (55, 59, 3.6),   # 55-59 years: 3.6%
        (60, 64, 2.6),   # 60-64 years: 2.6%
        (65, 69, 1.8),   # 65-69 years: 1.8%
        (70, 74, 1.2),   # 70-74 years: 1.2%
        (75, 100, 1.3)   # 75+ years: 1.3% (capped at 100)
    ]

    # Convert percentages to probabilities
    probabilities = [group[2] / 100.0 for group in age_groups]

    # Calculate number of samples for each age group
    samples_per_group = [int(prob * num_rows) for prob in probabilities]

    # Adjust for rounding errors to ensure exact total
    total_samples = sum(samples_per_group)
    if total_samples < num_rows:
        # Add remainder to the largest group (20-24 age group)
        largest_group_index = 4  # 20-24 years has 10.3%
        samples_per_group[largest_group_index] += (num_rows - total_samples)
    elif total_samples > num_rows:
        # Remove excess from the largest group
        largest_group_index = 4
        samples_per_group[largest_group_index] -= (total_samples - num_rows)

    ages = []

    # Generate ages for each group
    for i, (min_age, max_age, _) in enumerate(age_groups):
        if samples_per_group[i] > 0:
            group_ages = np.random.randint(min_age, max_age + 1, size=samples_per_group[i])
            ages.extend(group_ages)

    # Convert to numpy array and shuffle
    ages_array = np.array(ages)
    np.random.shuffle(ages_array)

    return ages_array

def save_to_csv(ages, filename="ages_data.csv"):
    """
    Save ages data to CSV file

    Args:
        ages (numpy.ndarray): Array of ages
        filename (str): Output CSV filename
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Age'])  # Header

        # Write ages one per row
        for age in ages:
            writer.writerow([age])

    print(f"Successfully saved {len(ages):,} age records to {filename}")

def print_distribution_stats(ages):
    """
    Print statistics about the generated age distribution

    Args:
        ages (numpy.ndarray): Array of ages
    """
    total = len(ages)

    # Define the same age groups for statistics
    age_groups = [
        (0, 4, 11.3, "0-4"),
        (5, 9, 10.5, "5-9"),
        (10, 14, 9.4, "10-14"),
        (15, 19, 9.7, "15-19"),
        (20, 24, 10.3, "20-24"),
        (25, 29, 9.7, "25-29"),
        (30, 34, 7.8, "30-34"),
        (35, 39, 6.1, "35-39"),
        (40, 44, 5.5, "40-44"),
        (45, 49, 5.0, "45-49"),
        (50, 54, 4.4, "50-54"),
        (55, 59, 3.6, "55-59"),
        (60, 64, 2.6, "60-64"),
        (65, 69, 1.8, "65-69"),
        (70, 74, 1.2, "70-74"),
        (75, 100, 1.3, "75+")
    ]

    print("\nDetailed Age Distribution Statistics:")
    print("-" * 60)
    print(f"Total records: {total:,}")
    print("-" * 60)
    print(f"{'Age Group':<10} {'Count':<10} {'Actual %':<10} {'Target %':<10} {'Diff':<8}")
    print("-" * 60)

    for min_age, max_age, target_pct, label in age_groups:
        count = np.sum((ages >= min_age) & (ages <= max_age))
        actual_pct = (count / total) * 100
        diff = actual_pct - target_pct

        print(f"{label:<10} {count:<10,} {actual_pct:<10.2f} {target_pct:<10.1f} {diff:<+8.2f}")

    print("-" * 60)
    print(f"Mean age:      {np.mean(ages):.1f}")
    print(f"Median age:    {np.median(ages):.1f}")
    print(f"Min age:       {np.min(ages)}")
    print(f"Max age:       {np.max(ages)}")

def main():
    """Main function to generate age data and save to CSV"""
    print("Generating 1,000,000 random ages with specified distribution...")

    # Set random seed for reproducibility (optional)
    np.random.seed(42)

    # Generate age data
    ages = generate_age_data(1000000)

    # Print statistics
    print_distribution_stats(ages)

    # Save to CSV
    save_to_csv(ages, "ages_data.csv")

    print("\nAge data generation complete!")

if __name__ == "__main__":
    main()
