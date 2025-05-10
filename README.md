# txthandwritten ✍️📄

**txthandwritten** is a Python-based utility that converts text-based documents (PDF or DOCX) into a **handwritten-style format**. It's built to save time for students who need to submit handwritten assignments — simply convert, print, and submit!

---

## 🧰 Features

- 📝 Converts PDF and DOCX files to handwritten-style images or PDFs  
- 📚 Supports multi-page documents  
- 🖨️ Output can be directly printed and submitted as handwritten assignments  
- ⏱️ Saves hours of manual writing  
- 🔤 Uses pre-trained handwriting-style fonts for natural appearance  

---

## 📁 Project Structure

txthandwritten/  
│  
├── hand_written.py         # Main script for handling the conversion logic  
└── README.md               # Project documentation (this file)  

> Optional: You can include a `fonts/` folder for custom handwriting fonts.

---

## 🛠️ Requirements

- Python 3.7+  
- fpdf  
- opencv-python  
- pillow  
- python-docx  
- PyMuPDF (fitz) or pdfplumber  

Install dependencies:
```bash
    pip install fpdf opencv-python pillow python-docx PyMuPDF
```
## 🖥️ How to Use

1. Place your `.pdf` or `.docx` file in the project directory.  
2. Run the script:
``` bash
python hand_written.py
```


3. Follow on-screen prompts or modify `hand_written.py` to use default input/output paths.  
4. The script generates a handwritten-style PDF or image pages.  
5. Print it out and submit as your assignment!

---

## 🔍 How It Works

- Extracts text from the input document (PDF or DOCX)  
- Converts each line of text into an image using a handwriting-style font  
- Assembles the images into a PDF file that mimics handwritten notes  

---

## ⚠️ Disclaimer

This tool is intended for **educational and personal use only**.  
Please use responsibly and ensure compliance with your institution's academic policies.  
The developer is not responsible for misuse or unethical applications.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Developed by @princemehta-git  
https://github.com/princemehta-git




