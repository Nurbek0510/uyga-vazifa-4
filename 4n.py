def foydalanuvchi_nomini_ol(foydalanuvchi):
    if "username" in foydalanuvchi:
        return foydalanuvchi["username"]
    else:
        return "Username topilmadi"


print(foydalanuvchi_nomini_ol({"username": "eshmat"}))
print(foydalanuvchi_nomini_ol({"name": "Eshmat"}))