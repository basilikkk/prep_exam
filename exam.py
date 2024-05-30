from utils import unzip_with_7z
import string

zip_file_path = 'congrats.7z'  # keep as is
dest_path = '.'  # keep as is

base_password = 'bcmpda' 

# Generate all possible combinations of two lowercase letters
for first_letter in string.ascii_lowercase:
    for second_letter in string.ascii_lowercase:
        # Form the potential password
        find_me = first_letter + second_letter
        secret_password = find_me + base_password
        
        # Try to unzip with the generated password
        if unzip_with_7z(zip_file_path, dest_path, secret_password):
            print(f"The password is: {secret_password}")
            exit()  # Exit the loop once the password is found