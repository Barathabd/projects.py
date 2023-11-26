print("Welcome to the treassure map!")
row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]
Map=[row1,row2,row3]
print(f" {row1}\n {row2}\n {row3}\n")
position=(input("Where do you want to place the tressure?\n"))
Horizontal=int(position[0])
Vertical=int(position[1])
selected_column=Map[Vertical-1]
selected_column[Horizontal-1]="x"
print(f" {row1}\n {row2}\n {row3}\n")