colours_id = {"alice blue": "#f0f8ff", "blanched almond": "#ffebcd", "black": "#00000", "blue": "#0000ff",
              "blue violet": "#8a2be2", "brown": "#a52a2a","cadet blue": "#5f9ea0", "chocolate": "#d2691e",
              "cornflower blue": "#6495ed", "dark green": "#006400", }

# print(colours_id)
for key, value in colours_id.items():
    print("{:<17} is {}".format(key.title(), value))

colour = input("Enter colour name: ").lower()
while colour != "":
    if colour in colours_id:
        print(colour.title(), "is", colours_id[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ").lower()
