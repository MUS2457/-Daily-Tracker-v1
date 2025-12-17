import input_data
import calculation
import storage


def menu():
    print("\n--- Welcome to Daily Tracker ---")
    print("1. Exit the program")
    print("2. Add new daily data")
    print("3. Load existing data")


while True:
    menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("Goodbye 👋")
        break

    elif choice == "2":
        daily = input_data.daily_data()
        time_task = calculation.time_per_task(daily)
        total_t = calculation.total_time(daily)
        most_task, least_task = calculation.extreme_tasks(daily)
        fq_mood = calculation.mood_frequency(daily)
        avg_mood = calculation.average_mood(daily)

        print("\n--- Daily Summary ---")
        print(
            f"Total time spent: "
            f"{total_t['total minutes']} minutes "
            f"({total_t['total hours']:.2f} hours)"
        )
        print("total time spent per task: ")
        for item,info in time_task.items():
            print(f"{item}: {info}")

        print(f"Most time spent on : {most_task}")
        print(f"Least time spent on: {least_task}")

        print("\nMood frequency:")
        for mood, count in fq_mood.items():
            print(f" - {mood}: {count}")

        print(f"\nAverage mood score: {avg_mood:.2f}")

        storage.save_daily(daily)
        print("\nData saved successfully ✅")

    elif choice == "3":
        history = storage.load_daily()
        print("\n--- Saved History ---")
        print(history)

    else:
        print("Invalid choice ❌ Please try again.")
