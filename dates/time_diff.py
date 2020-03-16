def time_diff(f, s):
    if f > s:
        duration = f - s
    else:
        duration = s - f
    return int(duration.total_seconds() // 60)
