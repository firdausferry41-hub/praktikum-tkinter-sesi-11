
import tkinter as tk
from tkinter import ttk, messagebox


# Fungsi Submit
def submit_form(event=None):
    nama = entry_nama.get().strip()

    # Validasi nama tidak boleh kosong
    if nama == "":
        messagebox.showwarning(
            "Peringatan",
            "Nama lengkap tidak boleh kosong!"
        )
        entry_nama.focus()
        return

    prodi = combo_prodi.get()
    gender = jenis_kelamin.get()
    alasan = text_alasan.get("1.0", tk.END).strip()

    # Mengambil pilihan dari Checkbutton
    kegiatan = []

    if var_seminar.get():
        kegiatan.append("Seminar")

    if var_workshop.get():
        kegiatan.append("Workshop")

    if var_lomba.get():
        kegiatan.append("Lomba")

    if var_organisasi.get():
        kegiatan.append("Organisasi")

    # Mengambil pilihan dari Listbox
    pilihan_listbox = listbox_kegiatan.curselection()

    for index in pilihan_listbox:
        pilihan = listbox_kegiatan.get(index)

        if pilihan not in kegiatan:
            kegiatan.append(pilihan)

    # Membuat ringkasan pendaftaran
    ringkasan = (
        "RINGKASAN PENDAFTARAN\n"
        "================================\n"
        f"Nama: {nama}\n"
        f"Program Studi: {prodi if prodi else '-'}\n"
        f"Jenis Kelamin: {gender}\n"
        f"Kegiatan: {', '.join(kegiatan) if kegiatan else '-'}\n"
        f"Alasan Mengikuti:\n{alasan if alasan else '-'}\n"
        "================================"
    )

    # Menampilkan hasil
    area_informasi.config(state="normal")
    area_informasi.delete("1.0", tk.END)
    area_informasi.insert(tk.END, ringkasan)
    area_informasi.config(state="disabled")

    messagebox.showinfo(
        "Berhasil",
        "Pendaftaran berhasil ditampilkan!"
    )


# Fungsi Reset
def reset_form():
    entry_nama.delete(0, tk.END)
    combo_prodi.set("")

    jenis_kelamin.set("Laki-laki")

    var_seminar.set(False)
    var_workshop.set(False)
    var_lomba.set(False)
    var_organisasi.set(False)

    listbox_kegiatan.selection_clear(0, tk.END)

    text_alasan.delete("1.0", tk.END)

    area_informasi.config(state="normal")
    area_informasi.delete("1.0", tk.END)
    area_informasi.config(state="disabled")

    entry_nama.focus()


# Fungsi About
def show_about():
    about = tk.Toplevel(root)
    about.title("About")
    about.geometry("350x200")
    about.resizable(False, False)

    ttk.Label(
        about,
        text="Pendaftaran Kegiatan Mahasiswa",
        font=("Arial", 12, "bold")
    ).pack(pady=20)

    ttk.Label(
        about,
        text="Aplikasi GUI menggunakan Python Tkinter.\n"
             "Dibuat untuk memenuhi tugas praktikum.",
        justify="center"
    ).pack(pady=5)

    ttk.Button(
        about,
        text="Tutup",
        command=about.destroy
    ).pack(pady=15)


# Fungsi Bantuan
def show_help():
    messagebox.showinfo(
        "Bantuan",
        "Petunjuk Penggunaan Aplikasi:\n\n"
        "1. Masukkan nama lengkap.\n"
        "2. Pilih program studi.\n"
        "3. Pilih jenis kelamin.\n"
        "4. Pilih kegiatan menggunakan Checkbutton atau Listbox.\n"
        "5. Masukkan alasan mengikuti kegiatan.\n"
        "6. Klik Submit untuk melihat hasil.\n"
        "7. Klik Reset untuk menghapus data."
    )


# Fungsi Keluar
def exit_app():
    if messagebox.askyesno(
        "Keluar",
        "Apakah Anda yakin ingin keluar?"
    ):
        root.destroy()


# Membuat jendela utama
root = tk.Tk()
root.title("Pendaftaran Kegiatan Mahasiswa")
root.geometry("750x850")
root.resizable(False, False)


# Menu aplikasi
menu_bar = tk.Menu(root)

menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(
    label="Keluar",
    command=exit_app
)

menu_bar.add_cascade(
    label="File",
    menu=menu_file
)

menu_bantuan = tk.Menu(menu_bar, tearoff=0)
menu_bantuan.add_command(
    label="Petunjuk Penggunaan",
    command=show_help
)
menu_bantuan.add_command(
    label="About",
    command=show_about
)

menu_bar.add_cascade(
    label="Bantuan",
    menu=menu_bantuan
)

root.config(menu=menu_bar)


# Judul aplikasi
ttk.Label(
    root,
    text="FORMULIR PENDAFTARAN KEGIATAN MAHASISWA",
    font=("Arial", 15, "bold")
).pack(pady=15)


# Frame utama formulir
form = ttk.LabelFrame(
    root,
    text="Data Pendaftaran",
    padding=12
)

form.pack(fill="x", padx=20, pady=5)
form.columnconfigure(1, weight=1)


# 1. Entry nama
ttk.Label(
    form,
    text="Nama Lengkap"
).grid(row=0, column=0, sticky="w", padx=5, pady=7)

entry_nama = ttk.Entry(form, width=45)
entry_nama.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=5,
    pady=7
)


# 2. Combobox program studi
ttk.Label(
    form,
    text="Program Studi"
).grid(row=1, column=0, sticky="w", padx=5, pady=7)

combo_prodi = ttk.Combobox(
    form,
    values=[
        "Teknik Informatika",
        "Sistem Informasi",
        "Manajemen",
        "Akuntansi",
        "Teknik Industri"
    ],
    state="readonly"
)

combo_prodi.grid(
    row=1,
    column=1,
    sticky="ew",
    padx=5,
    pady=7
)


# 3. Radiobutton jenis kelamin
ttk.Label(
    form,
    text="Jenis Kelamin"
).grid(row=2, column=0, sticky="w", padx=5, pady=7)

jenis_kelamin = tk.StringVar(value="Laki-laki")

frame_gender = ttk.Frame(form)
frame_gender.grid(
    row=2,
    column=1,
    sticky="w",
    padx=5,
    pady=7
)

ttk.Radiobutton(
    frame_gender,
    text="Laki-laki",
    variable=jenis_kelamin,
    value="Laki-laki"
).pack(side="left", padx=5)

ttk.Radiobutton(
    frame_gender,
    text="Perempuan",
    variable=jenis_kelamin,
    value="Perempuan"
).pack(side="left", padx=5)


# 4. Checkbutton pilihan kegiatan
ttk.Label(
    form,
    text="Pilihan Kegiatan"
).grid(row=3, column=0, sticky="nw", padx=5, pady=7)

frame_kegiatan = ttk.Frame(form)
frame_kegiatan.grid(
    row=3,
    column=1,
    sticky="w",
    padx=5,
    pady=7
)

var_seminar = tk.BooleanVar()
var_workshop = tk.BooleanVar()
var_lomba = tk.BooleanVar()
var_organisasi = tk.BooleanVar()

ttk.Checkbutton(
    frame_kegiatan,
    text="Seminar",
    variable=var_seminar
).grid(row=0, column=0, sticky="w")

ttk.Checkbutton(
    frame_kegiatan,
    text="Workshop",
    variable=var_workshop
).grid(row=0, column=1, sticky="w", padx=12)

ttk.Checkbutton(
    frame_kegiatan,
    text="Lomba",
    variable=var_lomba
).grid(row=1, column=0, sticky="w")

ttk.Checkbutton(
    frame_kegiatan,
    text="Organisasi",
    variable=var_organisasi
).grid(row=1, column=1, sticky="w", padx=12)


# 5. Listbox pilihan kegiatan
ttk.Label(
    form,
    text="Daftar Kegiatan"
).grid(row=4, column=0, sticky="nw", padx=5, pady=7)

frame_listbox = ttk.Frame(form)
frame_listbox.grid(
    row=4,
    column=1,
    sticky="w",
    padx=5,
    pady=7
)

scrollbar = ttk.Scrollbar(frame_listbox)
scrollbar.pack(side="right", fill="y")

listbox_kegiatan = tk.Listbox(
    frame_listbox,
    height=4,
    width=35,
    selectmode=tk.MULTIPLE,
    exportselection=False,
    yscrollcommand=scrollbar.set
)

listbox_kegiatan.pack(side="left")

scrollbar.config(command=listbox_kegiatan.yview)

daftar_kegiatan = [
    "Seminar",
    "Workshop",
    "Lomba",
    "Organisasi"
]

for kegiatan in daftar_kegiatan:
    listbox_kegiatan.insert(tk.END, kegiatan)


# 6. Text alasan mengikuti kegiatan
ttk.Label(
    form,
    text="Alasan Mengikuti"
).grid(row=5, column=0, sticky="nw", padx=5, pady=7)

text_alasan = tk.Text(
    form,
    width=45,
    height=4,
    wrap="word"
)

text_alasan.grid(
    row=5,
    column=1,
    sticky="ew",
    padx=5,
    pady=7
)


# 7. Tombol Submit dan Reset
frame_tombol = ttk.Frame(root)
frame_tombol.pack(pady=12)

ttk.Button(
    frame_tombol,
    text="Submit",
    command=submit_form
).pack(side="left", padx=8)

ttk.Button(
    frame_tombol,
    text="Reset",
    command=reset_form
).pack(side="left", padx=8)


# 8. Area informasi
hasil = ttk.LabelFrame(
    root,
    text="Area Informasi",
    padding=10
)

hasil.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 15)
)

area_informasi = tk.Text(
    hasil,
    height=10,
    wrap="word",
    state="disabled"
)

area_informasi.pack(
    fill="both",
    expand=True
)


# Event keyboard Enter
entry_nama.bind("<Return>", submit_form)
combo_prodi.bind("<Return>", submit_form)


# Menjalankan aplikasi
root.mainloop()
