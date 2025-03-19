# Web_Launcher

This Python program is designed to open URLs from a text file automatically in your web browser. It first checks if an internet connection is available, reads the URLs from a specified file, and then opens each URL in a new tab of the default web browser.

## Features

- Check internet connectivity before launching URLs.
- Extract valid URLs from a text file using regular expressions.
- Open each URL in a new browser tab.
- Command-line interface to specify the input file.
- Support for help and usage instructions via command-line arguments.

## Prerequisites

- Python 3.x
- `webbrowser` and `urllib` libraries (Both are included by default in Python)

## Usage

1. **Repository** to your local machine:
   ```bash
   https://github.com/Rishikeshgawali/Web_Launcher
   ```

2. **Create a text file (e.g., `urls.txt`)** with one URL per line. For example:
   ```txt
   https://www.google.com
   https://www.github.com
   https://www.python.org
   ```

3. **Run the Program** with the file path as an argument:
   ```bash
   python Web_Launcher.py urls.txt
   ```

4. **Command-Line Arguments**:
   - `-h` or `-H`: Display help information about the program.
   - `-u` or `-U`: Display usage information (how to use the program).

   Example:
   ```bash
   python Web_Launcher.py -h
   ```

   This will display the help message.

## How it Works

1. **Checks for internet connectivity** by attempting to connect to Google’s website.
2. If the internet is available:
   - The program reads each line of the specified text file.
   - It finds valid URLs using regular expressions.
   - Opens each valid URL in a new browser tab using the `webbrowser` module.
3. If no internet connection is detected, the script will show an error message and stop.

## Example

Given a text file `urls.txt` with the following content:

```txt
https://www.google.com
https://www.github.com
https://www.python.org
```

Run the program like this:

```bash
python Web_Launcher.py urls.txt
```

This will open all three URLs in separate browser tabs.

## Error Handling

- **Invalid File**: If the provided file is not found or cannot be opened, the script will show an error message.
- **Invalid URL Format**: If the URL format is incorrect, the script will skip that URL and continue with others.

## Author

**RISHIKESH BHARAT GAWALI**
