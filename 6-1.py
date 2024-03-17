people = {"first_name": "Kevin", "last_name": "knightKevin", "age": 20, "city": "SuZhou"}
for i, j in people.items():
    print(i, j)
print(people.keys())
print("wowowowo")
print("maybe i can do this")
print("yaaaa hoooooo")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(my_foods)
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append("ice cream")

# prompt = "\nTell me something,and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message!='quit':
#     message=input(prompt)
#
#     if message !='quit':
#         print(message)

prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())