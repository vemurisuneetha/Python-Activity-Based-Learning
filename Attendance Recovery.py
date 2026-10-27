held=int(input("Held: "))
att=int(input("Attended: "))
perc=att/held*100
print(f"{perc:.1f}%")
if perc<75:
  need=(0.75*held-att)/0.25
  print(f"Need {need:.0f}more")
else:
  bunk=int(att-0.75*held)/0.75
  print(f"Can bunk {bunk}")