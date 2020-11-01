play_list = {
    "radiohead": 156,
    "kishore kumar": 141,
    "wilco": 111,
    "black keyes": 35,
    "neutral milk hotel": 94,
    "the strokes": 61,
    "beck": 88
}


def find_smallest_in_dict(playlist):
    listen_times = list(play_list.values())
    current = listen_times[0]

    for idx in range(1, len(listen_times)):
        if current > listen_times[idx]:
            current = listen_times[idx]

    for key, val in list(play_list.items()):
        if val == current:
            return key


def selection_sort_dict(playlist):
    new_arr = []

    for song in play_list:
        smallest = find_smallest_in_dict(playlist)
        song = play_list.pop(smallest, None)
        new_arr.append(song)

    return new_arr


selection_sort_dict(play_list)
