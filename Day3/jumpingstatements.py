# We have two jumping statements Break & Continue
#break is used for "exit from the block"
# if we skip certain conditions then we use continue, Continue will skip that particular part and skip to other
for i in range(1,10):
    if i ==5:
        break
    print(i)
print("Program exited from break statement")
for i in range(1,10):
    if i ==5:
        continue
    print(i)
print("Program skipped some value due to continue statement")