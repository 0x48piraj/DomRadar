def creator(domain_name, is_available):
    with open("available.txt", "w") as f:
        _name = is_available(domain_name)
        if _name:
            print(f"{_name} is AVAILABLE")
            f.write(f"{_name}\n")
