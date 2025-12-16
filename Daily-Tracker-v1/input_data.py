def daily_data() :
    data = []
    track = ["coding","gym","work","study"]
    mood = ["tired","okay","good"]
    while True :
        track_user = input(f"Enter one of the following options : {track} ,'done' to finish or 'exit' to quit.").lower().strip()
        if track_user == "exit" :
            print("Quitting...")
            break
        if track_user == "done" :
            break
        if track_user not in track :
            continue
        try :
            duration =int(input("Enter duration in minutes : "))
            if duration < 0 :
                print("the duration cannot be negative.")
                continue
        except ValueError :
            print("Please enter a valid duration.")
            continue
        mood_user = input(f"Enter one of the following options : {mood} .").lower().strip()
        if mood_user not in mood :
            continue
        note = input("Enter note : ").strip()
        data.append({"task": track_user, "duration": duration, "mood": mood_user,"note": note})

    return data






