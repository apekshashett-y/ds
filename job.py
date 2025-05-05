def sjf(jobs):
    jobs.sort(key=lambda x: x[1])
    waiting_time = 0
    total_wait = 0
    print("Job\tBurstTime\tWaitingTime")
    for job in jobs:
        print(f"{job[0]}\t{job[1]}\t\t{waiting_time}")
        total_wait += waiting_time
        waiting_time += job[1]
    avg = total_wait / len(jobs)  
    print(f"Average Waiting Time: {avg:.2f}")


jobs = [
    ('J1', 6),
    ('J2', 8),
    ('J3', 7),
    ('J4', 3)
]

sjf(jobs)
