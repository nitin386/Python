import csv
import matplotlib.pyplot as plt

def display_menu():
    print("\n--- Electricity Use Dashboard ---")
    print("1. Load electricity data from CSV files")
    print("2. View usage analysis")
    print("3. Plot usage trend")
    print("4. Export results")
    print("5. Exit")

def load_data():
    data = []
    files_input = input("Enter CSV filenames separated by commas (e.g., jan.csv, feb.csv): ")
    file_list = [f.strip() for f in files_input.split(',')]

    print(f"Loading files: {file_list}...")
    
    for filename in file_list:
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append({
                        'Date': row['Date'],
                        'Usage': float(row['Usage'])
                    })
            print(f"Successfully loaded {filename}.")
        except FileNotFoundError:
            print(f"Error: File {filename} not found. Skipping.")
        except ValueError:
            print(f"Error: specific columns not found or invalid data format in {filename}.")
            
    return data

def analyze_data(data):
    if not data:
        print("No data loaded. Please load data first.")
        return None

    total_usage = sum(item['Usage'] for item in data)
    usage_values = [item['Usage'] for item in data]
    
    min_usage = min(usage_values)
    max_usage = max(usage_values)
    avg_usage = total_usage / len(data)

    summary = {
        'Total Usage': total_usage,
        'Average Daily Usage': avg_usage,
        'Min Daily Usage': min_usage,
        'Max Daily Usage': max_usage,
        'Total Days': len(data)
    }

    print("\n--- Usage Analysis ---")
    for key, value in summary.items():
        print(f"{key}: {value:.2f}")
    
    return summary

def plot_trend(data):
    if not data:
        print("No data loaded to plot.")
        return

    dates = [item['Date'] for item in data]
    usage = [item['Usage'] for item in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, usage, marker='o', linestyle='-', color='b')
    
    plt.xlabel('Dates')
    plt.ylabel('Units Consumed')
    plt.title('Household Electricity Usage Trend')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig('usage_plot.png')
    print("Plot saved as 'usage_plot.png'.")
    plt.show()

def export_results(data, summary):
    if not data or not summary:
        print("No data or summary to export.")
        return

    with open('electricity_summary_output.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Usage'])
        writer.writeheader()
        writer.writerows(data)
    print("Data exported to 'electricity_summary_output.csv'.")

    with open('analysis_summary.txt', mode='w') as file:
        file.write("--- Electricity Usage Summary ---\n")
        for key, value in summary.items():
            file.write(f"{key}: {value:.2f}\n")
    print("Summary exported to 'analysis_summary.txt'.")

def main():
    print("Welcome to the Electricity Use Dashboard!")
    
    electricity_data = []
    analysis_summary = None

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            electricity_data = load_data()
        elif choice == '2':
            analysis_summary = analyze_data(electricity_data)
        elif choice == '3':
            plot_trend(electricity_data)
        elif choice == '4':
            export_results(electricity_data, analysis_summary)
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
