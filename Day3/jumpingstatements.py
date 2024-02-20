# We have two jumping statements Break & Continue
#break is used for "exit from the block"
# if we skip certain conditions then we use continue, Continue will skip that particular part and skip to other

#break
for i in range(1,10):
    if i ==5:
        break
    print(i)
print("Program exited from break statement")
# Continue
for i in range(1,10):
    if i ==5:
        continue
    print(i)
print("Program skipped some value due to continue statement")

# problem2
for i in range(3,7,2):
    print(i)