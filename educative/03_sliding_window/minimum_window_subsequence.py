def min_window(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    min_window = float("inf")
    min_window_subseqence = ""

    for i in range(n1):
        if str1[i] == str2[-1]:
            # print(f"i = {i}")
            j1 = i
            j2 = n2 - 1
            while j1 >= 0 and j2 >= 0:
                if str1[j1] == str2[j2]:
                    j2 -= 1

                j1 -= 1
                # print(f"j1 = {j1}, j2 = {j2}")

            if j2 < 0:
                curr_window = i - j1
                if curr_window < min_window:
                    # print(f"j1 = {j1}, i = {i}")
                    min_window_subseqence = str1[j1 + 1 : i + 1]
                    min_window = curr_window
                    # print(
                    #     f"min_window = {min_window}, min_window_subseqence = {min_window_subseqence}"
                    # )

    return min_window_subseqence


if __name__ == "__main__":
    inputs = [
        {"str1": "this is a test string", "str2": "tis"},
        {"str1": "asbfgedasfbdaaf", "str2": "bfd"},
        {"str1": "azssstaszaztf", "str2": "saz"},
    ]

    for input in inputs:
        output = min_window(input["str1"], input["str2"])
        print(f"str1 = {input['str1']}, str2 = {input['str2']}")
        print(f"output = {output}")
        print()
