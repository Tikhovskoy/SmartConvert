import tkinter as tk
from tkinter import filedialog, messagebox
from app.converter import convert_pdf

def run_app():
    window = tk.Tk()
    window.title("SmartConvert — PDF в Word")
    window.geometry("400x200")
    window.resizable(False, False)

    label = tk.Label(window, text="Выберите PDF-файл для конвертации", font=("Arial", 12))
    label.pack(pady=20)

    def choose_file():
        filepath = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")],
            title="Выберите PDF"
        )
        if not filepath:
            return

        try:
            docx_path = convert_pdf(filepath)
            messagebox.showinfo("Успешно", f"Файл сохранён как:\n{docx_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось конвертировать файл:\n{e}")

    button = tk.Button(window, text="Выбрать PDF", command=choose_file, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)
    button.pack()

    window.mainloop()
