responses = {}

polling_active = True

while polling_active:
    print("Press 'no' without '' to exit and see the poll results.")
    name = input("\n Hey what is your name?: ")
    answer = input("If you could visit on place in the World, Where would you go?: ")

    responses[name] = answer
    repeat = input("would you like others to poll? (Yes / No): ")
    if repeat == 'no':
        polling_active = False

print("\n---poll-- results")

for name, answer in responses.items():
    print(f"{name} opt to visit in  {answer}")
