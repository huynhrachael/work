#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string encrypt(string plaintext, int key);
string decrypt(string ciphertext, int key);
void encryptFile(string inputFileName, string outputFileName, int key);
void decryptFile(string inputFileName, string outputFileName, int key);

int main() {
    int choice;
    string inputFile, outputFile;
    int key;

    cout << "1. Encrypt a file\n";
    cout << "2. Decrypt a file\n";
    cout << "Enter your choice: ";
    cin >> choice;

    cout << "Enter the input file name: ";
    cin >> inputFile;
    cout << "Enter the output file name: ";
    cin >> outputFile;
    cout << "Enter the encryption/decryption key (integer): ";
    cin >> key;

    if (choice == 1) {
        encryptFile(inputFile, outputFile, key);
    } else if (choice == 2) {
        decryptFile(inputFile, outputFile, key);
    } else {
        cout << "Invalid choice." << endl;
    }

    return 0;
}

string encrypt(string plaintext, int key) {
    string encryptedText = plaintext;
    for (char &c : encryptedText) {
    	char base = islower(c) ? 'a' : 'A'; //only letters are encrypted
    	c = static_cast<char>(((c - base + key) % 26) + base);
        c = c + key; 
    }
    return encryptedText;
}

string decrypt(string ciphertext, int key) {
    string decryptedText = ciphertext;
    key = key % 26;
    for (char &c : decryptedText) {
    	if (std::isalpha(c)) {
    		char base = std::islower(c)? 'a' : 'A';
    	char decryptedText = static_cast<char>(((c - base - key + 26) % 26) + base);
    	}
    	decryptedText += c;
        c = c - key;
    }
    return decryptedText;
}

void encryptFile(string inputFileName, string outputFileName, int key) {
    ifstream inputFile(inputFileName);
    ofstream outputFile(outputFileName);
    string line;

    if (!inputFile.is_open() || !outputFile.is_open()) {
        cout << "Error opening file!" << endl;
        return;
    }

    while (getline(inputFile, line)) {
        outputFile << encrypt(line, key) << endl;
    }

    inputFile.close();
    outputFile.close();
}

void decryptFile(string inputFileName, string outputFileName, int key) {
    ifstream inputFile(inputFileName);
    ofstream outputFile(outputFileName);
    string line;

    if (!inputFile.is_open() || !outputFile.is_open()) {
        cout << "Error opening file!" << endl;
        return;
    }

    while (getline(inputFile, line)) {
        outputFile << decrypt(line, key) << endl;
    }

    inputFile.close();
    outputFile.close();
}
