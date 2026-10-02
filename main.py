def main():
    sentence = input("Masukkan satu ayat: ")
    words = sentence.split()
    word_count = len(words)

    print(f"Ayat anda: {sentence}")
    print(f"Jumlah patah perkataan: {word_count}")


if __name__ == "__main__":
    main()