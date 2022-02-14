names = input('input names: ').split(", ")

title_names = []
not_title_names = []

for name in names:
    if name.istitle():
        title_names.append(name)
    else:
        not_title_names.append(name)

print(title_names, not_title_names)