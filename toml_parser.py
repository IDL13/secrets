req = open("requirements.txt", "w")

with open("pyproject.toml") as toml:
    counter = 9
    for i in toml:
        counter -= 1

        if counter < 0 and "[build-system]" not in i:
            req = open("requirements.txt", "a")
            req.write(i.split("=")[0] + "\n")

        if "[build-system]" in i:
            req.close()
            break
        