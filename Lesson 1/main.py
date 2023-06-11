# def strcount(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)
#
# strcount("fjieoajiognvawopebvoewhrgoptueuifahgeuowibguioesgahfuighwauivgyiuoweaghfuiegbwsi")

def srtcont(s):
    my_dict = {}
    for sym in s:
        my_dict[sym] = my_dict.get(sym, 0) + 1

    for key in my_dict:
        print(key, my_dict.get(key))

stringa = ""
for i in range(100_000):
    stringa += "a" if i < 50_000 else "b"

srtcont(stringa)