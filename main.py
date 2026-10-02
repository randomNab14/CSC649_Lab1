def main():
    # Minta pengguna masukkan ayat
    sentence = input("Masukkan satu ayat: ")

    # Semak jika input kosong atau hanya mengandungi ruang kosong
    if not sentence.strip():
        print("Ralat: Anda tidak memasukkan sebarang ayat atau perkataan!")
        return

    # Pecahkan ayat kepada senarai perkataan dan kira karakter (termasuk ruang kosong atau tanpa ruang kosong)
    words = sentence.split()
    word_count = len(words)
    char_count = len(sentence)  # Bilangan karakter keseluruhan termasuk ruang

    # Paparkan hasil
    print(f"Ayat anda: '{sentence}'")
    print(f"Jumlah patah perkataan: {word_count}")
    print(f"Jumlah karakter (termasuk ruang): {char_count}")


if __name__ == "__main__":
    main()