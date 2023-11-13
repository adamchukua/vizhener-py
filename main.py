import time
import sys


def get_ascii_symbols():
    ascii_symbols = ""

    for i in range(128):
        ascii_symbols += chr(i)

    return ascii_symbols


def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


def write_in_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Successfully wrote to {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def apply_cipher(text, key, alphabet, operation="encrypt"):
    result = ""
    key_code = generate_key_code(key, alphabet)
    key_code_index = 0

    for char in text:
        if operation == "encrypt":
            result_char_index = alphabet.find(char) + key_code[key_code_index % len(key)]
        elif operation == "decrypt":
            result_char_index = alphabet.find(char) - key_code[key_code_index % len(key)]

        result_char = alphabet[result_char_index % len(alphabet)]
        result += result_char
        key_code_index += 1

    return result


def encryption(text, key, alphabet):
    return apply_cipher(text, key, alphabet, operation="encrypt")


def decryption(text, key, alphabet):
    return apply_cipher(text, key, alphabet, operation="decrypt")


def generate_key_code(key, alphabet):
    return [alphabet.find(char) for char in key]


if len(sys.argv) != 4:
    print("Usage: python main.py <operation_type> <input_file_path> <key>")
    sys.exit(1)

operation_type = int(sys.argv[1])
input_file_path = sys.argv[2]
key = sys.argv[3]

output_file_path = input_file_path + ("_enc" if operation_type == 1 else "_dec")
text_from_file = read_text_from_file(input_file_path)
output_text = ""
alphabet = get_ascii_symbols()

start_time = time.time()
if operation_type == 1:
    output_text = encryption(text_from_file, key, alphabet)
elif operation_type == 2:
    output_text = decryption(text_from_file, key, alphabet)
else:
    print("Please try again. You have only two options:\n1 - Encryption\n2 - Decryption")
    exit(1)
end_time = time.time()

write_in_file(output_file_path, output_text)

elapsed_time = end_time - start_time
elapsed_time_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

print(f"Path for {"encrypted" if operation_type == 1 else "decrypted"} file: {output_file_path}")
print(f"Completed in {elapsed_time_str}")
