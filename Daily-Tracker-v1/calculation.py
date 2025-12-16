def total_time(data):
    total = 0

    if data:
        for info in data:
            total += info["duration"]
        return {
            "total minutes": total,
            "total hours": total / 60
        }
    else:
        return {}


def time_per_task(data):
    total_task = {}

    if data:
        for info in data:
            if info["task"] not in total_task:
                total_task[info["task"]] = info["duration"]
            else:
                total_task[info["task"]] += info["duration"]
        return total_task
    else:
        return {}


def extreme_tasks(data):
    task = {}

    if data:
        for info in data:
            if info["task"] not in task:
                task[info["task"]] = info["duration"]
            else:
                task[info["task"]] += info["duration"]

        most_consuming_task = max(task, key=task.get)
        least_consuming_task = min(task, key=task.get)

        return most_consuming_task, least_consuming_task
    else:
        return None


def mood_frequency(data):
    frequency_mood = {}
    count = 1

    if data:
        for info in data:
            if info["mood"] not in frequency_mood:
                frequency_mood[info["mood"]] = count
            else:
                frequency_mood[info["mood"]] += count
        return frequency_mood
    else:
        return {}


def average_mood(data):
    mood_score = {
        "tired": 1,
        "okay": 2,
        "good": 3
    }

    total_score = 0
    count = 0

    if data:
        for info in data:
            total_score += mood_score[info["mood"]]
            count += 1
        return total_score / count
    else:
        return 0

