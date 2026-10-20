guest_list = ["khin", "zawzaw", "khant", "may", "lynn", "zarchi", "bhone", "zinmar"]
print("Unfortunately, I can only invite two people for dinner.")

print(f"Dear {guest_list[0]}, unfortunately I won't be able to invite you due to limited space.")
guest_list.pop(0)

print(f"Dear {guest_list[0]}, unfortunately I won't be able to invite you due to limited space.")
guest_list.pop(0)

print(f"Dear {guest_list[3]}, unfortunately I won't be able to invite you due to limited space.")
guest_list.pop(3)

print(f"Dear {guest_list[4]}, unfortunately I won't be able to invite you due to limited space.")
guest_list.pop(4)

print(f"Dear {guest_list[1]}, unfortunately I won't be able to invite you due to limited space.")
guest_list.pop(1)

print(f"Dear {guest_list[1]}, unfortunately I won't be able to invite you due to limited space.")
guest_list.pop(1)

print(f"Hi {guest_list[0]}, just letting you know that you are still on the guest list.")
print(f"Hi {guest_list[1]}, just letting you know that you are still on the guest list.")

del guest_list[0]
del guest_list[0]
print(guest_list)