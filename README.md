# AFL Fuzzing with Gemini AI

This repository contains a script that integrates AFL (American Fuzzy Lop) with Gemini AI to enhance fuzzing efficiency by generating new test cases dynamically.

## Overview
This project uses **AFL** to fuzz a vulnerable binary and leverages **Gemini AI** to generate new fuzzing inputs based on existing test cases. The AI-generated inputs help improve coverage and discover vulnerabilities more effectively.

## Features
- **Automated Fuzzing**: Uses **AFL** to fuzz a binary automatically.
- **AI-Powered Test Case Generation**: Utilizes **Gemini AI** to generate new test inputs dynamically.
- **Continuous Execution**: The script monitors the input corpus and generates new test cases periodically.
- **Customizable**: You can modify the script to integrate different AI models or tweak fuzzing parameters.

## Prerequisites
Ensure you have the following installed:

- Python 3.x
- AFL++ (American Fuzzy Lop)
- Google Gemini AI API key
- A vulnerable binary to fuzz

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/afl-gemini-fuzzing.git
   cd afl-gemini-fuzzing
   ```
2. Install dependencies:
   ```bash
   pip install google-generativeai
   ```
3. Configure **Gemini AI** API key:
   Open the script and add the gemini key to the variable `GEMINI_API_KEY` with your actual API key.
   Get your Gemini API key from here : https://ai.google.dev/gemini-api/docs/api-key#windows

## Usage
1. Ensure AFL++ is installed and available in your system's path.
2. Place the target binary (`vuln`) in the Desktop directory or modify the `TARGET_BINARY` path in the script.
3. Run the script:
   ```bash
   python3 apps.py
   ```
4. The script will:
   - Check for an existing input corpus.
   - Start AFL fuzzing.
   - Use Gemini AI to generate additional test cases dynamically.
   - Continuously monitor and update the input corpus.

## Directory Structure
```
/home/ravi/Desktop/
│-- afl_gemini.py   # Main script
│-- vuln            # Target binary to fuzz
│-- input_corpus/   # Directory for seed inputs
│-- output_dir/     # Directory for AFL results
```


## Important update:

In this part of the code:

def generate_fuzz_input(seed_input):
    """Uses Gemini AI to generate a fuzzing input."""
    try:
        response = model.generate_content(f"Generate a fuzzing input based on: {seed_input}")
        return response.text.strip() if response.text else None
    except Exception as e:
        print(f"Error generating fuzz input: {e}")
        return None

For this text : " Generate a fuzzing input based on: {seed_input}" , It may happen that it can give you a whole answer like response along with the new mutated fuzzing input, hence modify this prompt in a way that you only get mutated seed input and nothing else.

This prompt is just like the prompt which we give in GPT mmodels like ChatGPT and CoPilot.


## Notes
- Ensure AFL is properly set up and working before running the script.
- The Gemini AI API might have rate limits, so consider optimizing requests accordingly.
- Modify the script to suit your fuzzing needs, such as changing the AI prompt or fuzzing parameters.

## License
This project is open-source under the MIT License.

## Contributions
Feel free to submit issues, feature requests, or pull requests to enhance the project!

