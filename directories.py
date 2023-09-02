from pathlib import Path

path = Path("module/ecommerce")


print(path.iterdir())


for p in path.iterdir():
    print(p)
