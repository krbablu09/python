def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Bablu", power="Study")
print_kwargs(name = "Bablu")
print_kwargs(power = "Study")
print_kwargs(name = "Bablu", power = "Study", Skill = "Coding")        