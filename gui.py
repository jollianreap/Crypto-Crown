import tkinter as tk
import customtkinter as ctk

# Настройка темы
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Создание основного окна
root = ctk.CTk()
root.title("Crypto Withdrawal Tool")
root.geometry("880x720")

# Создание табуляции
tab_control = ctk.CTkTabview(root)
tab_control.pack(padx=20, pady=20, fill="both", expand=True)

# Создание вкладок
tab_rpc = tab_control.add("RPC")
tab_gas = tab_control.add("GAZ")
tab_autowithdraw = tab_control.add("Autowithdraw")
tab_checker = tab_control.add("Checker")
tab_my_info = tab_control.add("My Info")

# Вкладка "RPC"
rpc_frame = ctk.CTkFrame(tab_rpc)
rpc_frame.pack(padx=20, pady=20, fill="both", expand=True)

rpc_label = ctk.CTkLabel(rpc_frame, text="Выберите сети, с которыми работать", font=("Arial", 12))
rpc_label.pack(padx=20, pady=10)

rpc_nodes_frame = ctk.CTkFrame(rpc_frame, width=500, height=400)
rpc_nodes_frame.pack(padx=20, pady=20, fill="both", expand=False)

rpc_nodes_canvas = ctk.CTkCanvas(rpc_nodes_frame)
rpc_nodes_canvas.pack(side="left", fill="both", expand=True)

rpc_nodes_scrollbar_y = ctk.CTkScrollbar(rpc_nodes_frame, orientation="vertical", command=rpc_nodes_canvas.yview)
rpc_nodes_scrollbar_y.pack(side="right", fill="y")

rpc_nodes_canvas.configure(yscrollcommand=rpc_nodes_scrollbar_y.set)
rpc_nodes_canvas.bind('<Configure>', lambda e: rpc_nodes_canvas.configure(scrollregion=rpc_nodes_canvas.bbox("all")))

rpc_nodes_frame_inside = ctk.CTkFrame(rpc_nodes_canvas)
rpc_nodes_canvas.create_window((0, 0), window=rpc_nodes_frame_inside, anchor="nw")

rpc_checkboxes = {}

row = 0
col = 0
for network in ["Mainnet", "Layer2", "Non-EVM"]:
    for url in ["URL1", "URL2", "URL3"]:  # Пример URL, замените на реальные данные
        rpc_checkboxes[(network, url)] = ctk.CTkCheckBox(rpc_nodes_frame_inside, text=url, width=20, height=20, font=("Arial", 10))
        rpc_checkboxes[(network, url)].grid(row=row, column=col, padx=10, pady=5, sticky="w")
        col += 1
        if col > 2:
            col = 0
            row += 1
        rpc_checkboxes[(network, url)].select()

# Вкладка "GAZ"
gas_frame = ctk.CTkFrame(tab_gas)
gas_frame.pack(padx=20, pady=20, fill="both", expand=True)

gas_label = ctk.CTkLabel(gas_frame, text="Установите нужные вам значения газа", font=("Arial", 12))
gas_label.pack(padx=20, pady=10)

gas_entries_frame = ctk.CTkFrame(gas_frame)
gas_entries_frame.pack(padx=20, pady=20, fill="both", expand=True)

gas_entries = {}

row = 0
col = 0
for network in ["Mainnet", "Layer2", "Non-EVM"]:
    gas_entries[network] = ctk.CTkEntry(gas_entries_frame, width=100)
    gas_entries[network].insert(0, "0.0")  # Пример значения газа, замените на реальные данные
    gas_entries[network].grid(row=row, column=col, padx=20, pady=10, sticky="e")
    ctk.CTkLabel(gas_entries_frame, text=network, font=("Arial", 12)).grid(row=row, column=col+1, padx=10, pady=10, sticky="w")
    col += 2
    if col > 4:
        col = 0
        row += 1

update_gas_charge_button = ctk.CTkButton(gas_frame, text="Изменить комиссии и применить")
update_gas_charge_button.pack(padx=20, pady=20)

# Вкладка "Autowithdraw"
autowithdraw_frame = ctk.CTkFrame(tab_autowithdraw)
autowithdraw_frame.pack(padx=20, pady=20, fill="both", expand=True)

autowithdraw_label = ctk.CTkLabel(autowithdraw_frame, text="Выберите файл с сид фразами/приватными ключами")
autowithdraw_label.pack(padx=20, pady=10)

autowithdraw_button = ctk.CTkButton(autowithdraw_frame, text="Выбрать файл")
autowithdraw_button.pack(padx=20, pady=10)

autowithdraw_file_label = ctk.CTkLabel(autowithdraw_frame, text="")
autowithdraw_file_label.pack(padx=20, pady=10)

autowithdraw_log_text = ctk.CTkTextbox(autowithdraw_frame)
autowithdraw_log_text.pack(padx=20, pady=20, fill="both", expand=True)

autowithdraw_withdraw_button = ctk.CTkButton(autowithdraw_frame, text="Вывести средства")
autowithdraw_withdraw_button.pack(padx=20, pady=10)

# Вкладка "Checker"
checker_frame = ctk.CTkFrame(tab_checker)
checker_frame.pack(padx=20, pady=20, fill="both", expand=True)

checker_label = ctk.CTkLabel(checker_frame, text="Выберите файл с сид фразами/приватными ключами")
checker_label.pack(padx=20, pady=10)

checker_button = ctk.CTkButton(checker_frame, text="Выбрать файл")
checker_button.pack(padx=20, pady=10)

checker_address_label = ctk.CTkLabel(checker_frame, text="")
checker_address_label.pack(padx=20, pady=10)

checker_check_button = ctk.CTkButton(checker_frame, text="Проверить балансы")
checker_check_button.pack(padx=20, pady=10)

checker_result_text = ctk.CTkTextbox(checker_frame)
checker_result_text.pack(padx=20, pady=20, fill="both", expand=True)

# Вкладка "My Info"
my_info_frame = ctk.CTkFrame(tab_my_info)
my_info_frame.pack(padx=20, pady=20, fill="both", expand=True)

my_info_label = ctk.CTkLabel(my_info_frame, text="Адрес для вывода средств:")
my_info_label.pack(padx=20, pady=10)

my_info_entry = ctk.CTkEntry(my_info_frame)
my_info_entry.pack(padx=20, pady=10)

my_info_amount_label = ctk.CTkLabel(my_info_frame, text="Сумма для вывода средств с учетом комиссии:")
my_info_amount_label.pack(padx=20, pady=10)

my_info_amount_slider = ctk.CTkSlider(my_info_frame, from_=1, to=99, number_of_steps=98)
my_info_amount_slider.pack(padx=20, pady=10)

my_info_amount_label_2 = ctk.CTkLabel(my_info_frame, text="1%")
my_info_amount_label_2.pack(padx=20, pady=10)

# Запуск основного цикла
root.mainloop()