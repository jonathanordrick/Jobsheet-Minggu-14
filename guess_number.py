def guess_number():
    secret_number = 9
    guess = 0
    guess_limit = 3
    found = False

    while guess < guess_limit:
        user = int(input("Masukan angka > "))
        if user == secret_number:
            print("Selamat, anda berhasil menemukan angka rahasianya")
            found = True
            break
        else:
            print("Salah! Awokawok")
            guess += 1

    if not found:
        print(f"Anda tidak menemukan angkanya, angka rahasianya adalah {secret_number}")


    