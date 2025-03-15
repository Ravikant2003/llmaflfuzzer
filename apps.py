import os
import subprocess
import time
import uuid
import google.generativeai as genai

# Configure Gemini AI
GEMINI_API_KEY = ""
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-lite")

# Directories for AFL fuzzing
DESKTOP_DIR = "/home/ravi/Desktop"
INPUT_DIR = os.path.join(DESKTOP_DIR, "input_corpus")
OUTPUT_DIR = os.path.join(DESKTOP_DIR, "output_dir")
TARGET_BINARY = os.path.join(DESKTOP_DIR, "vuln") 


os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_fuzz_input(seed_input):
    """Uses Gemini AI to generate a fuzzing input."""
    try:
        response = model.generate_content(f"Generate a fuzzing input based on: {seed_input}")
        return response.text.strip() if response.text else None
    except Exception as e:
        print(f"Error generating fuzz input: {e}")
        return None


if not os.listdir(INPUT_DIR):
    print("[-] input_corpus is empty! Adding a default test case.")
    with open(os.path.join(INPUT_DIR, "seed1.txt"), "w") as f:
        f.write("test") 


afl_command = f"afl-fuzz -i {INPUT_DIR} -o {OUTPUT_DIR} -- {TARGET_BINARY} @@"


process = subprocess.Popen(afl_command, shell=True)
time.sleep(5)


while True:
    seed_files = os.listdir(INPUT_DIR)
    for seed in seed_files:
        seed_path = os.path.join(INPUT_DIR, seed)
        
        with open(seed_path, "r") as f:
            seed_input = f.read()

        new_test = generate_fuzz_input(seed_input)
        if new_test:
            new_filename = os.path.join(INPUT_DIR, f"test_case_{uuid.uuid4().hex[:8]}")
            with open(new_filename, "w") as f:
                f.write(new_test)
            print(f"[+] Added new fuzz test case: {new_filename}")

    time.sleep(10)  
