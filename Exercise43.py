
denomination = input("Enter the denomination of the banknote (e.g., $1, $5): ")


if denomination == '$1':
        print("The individual on the" ,denomination,"banknote is: George Washington ")
elif denomination == '$2':
        print("The individual on the" ,denomination,"banknote is: Thomas Jefferson")
elif denomination == '$5':
        print(f"The individual on the" ,denomination,"banknote is: Abraham Lincoln")
elif denomination == '$10':
        print(f"The individual on the" ,denomination,"banknote is: Alexander Hamilton")
elif denomination == '$20':
        print(f"The individual on the" ,denomination,"banknote is: Andrew Jackson")
elif denomination == '$50':
        print(f"The individual on the" ,denomination,"banknote is: Ulysses S. Grant")
elif denomination == '$100':
        print(f"The individual on the" ,denomination,"banknote is: Benjamin Franklin")
else:
        print("Error: No such banknote exists.")