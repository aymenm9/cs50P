    # Encryption and Decryption Program from Csv file
    #### Video Demo:  <https://youtu.be/8G9_QxyQ0Qw>
    #### Description:
        This Python program encrypts and decrypts data from a CSV file using the `cryptography` library's `Fernet` class for encryption. It takes command-line arguments for input file, output file, operation type (encryption or decryption), and encryption code.

        ## Overview
        This program provides a simple and secure way to encrypt and decrypt data in CSV files. It ensures that sensitive information remains protected during storage or transmission.

        ## Files
        - `project.py`: Contains the main functionality of the program, including encryption and decryption functions.
        - `ArgsManager.py`: Manages command-line arguments for the program.
        - `AppCsv.py`: Handles CSV file operations.
        - `test_project.py`: Contains unit tests for the program functions.

        ## Design Choices
        - Used the `cryptography` library for encryption due to its strong security features.
        - Implemented command-line argument parsing using the `argparse` module for ease of use.
        - Encoded keys using base64 for compatibility with the `Fernet` class.

        ## How to Use
        1. Clone the project repository to your local machine.
        2. Install the required dependencies using `pip install -r requirements.txt`.
        3. Run the program using the command `python project.py -i input.csv -o output.csv -d e -c <encryption_code>` for encryption or `python project.py -i input.csv -o output.csv -d d -c <encryption_code>` for decryption.

        ## Future Improvements
        - Add support for different encryption algorithms.
        - Improve error handling and input validation.
        - Implement key management and rotation for enhanced security.

        ## Conclusion
        This program provides a convenient way to encrypt and decrypt data in CSV files, ensuring that sensitive information is protected. It can be used in various applications where data security is crucial.