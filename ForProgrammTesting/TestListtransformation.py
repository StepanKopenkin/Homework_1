
import QuickSort as q

a = open("K1")
b = {"stem": "", "normal_form": [], "frequency": ([],[])}
for x in a:
    x = x.replace("\n","").split(" ")
    b["stem"] = x[0]
    b["normal_form"].append(x[1])
    b["frequency"][1].append(int(x[2]))

[b["frequency"][0].append(x)for x in range(len(b["normal_form"]))]
print(b["frequency"])
q.quickSort(b["frequency"],1, True)
print(b["frequency"])
q.quickSort(b["frequency"],1, False)
print(b["frequency"])