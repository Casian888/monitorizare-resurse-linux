import time
import multiprocessing
import psutil
import matplotlib.pyplot as plt
import plotext as plt_term
import os

def dummy_workload():
    """Aplicație care rulează în fundal și consumă intenționat resurse CPU și RAM."""
    lista_memorie = []
    while True:
        _ = [x**2 for x in range(5000)]
        lista_memorie.append("A" * 50000)
        time.sleep(0.1)

if __name__ == "__main__":
    workload_process = multiprocessing.Process(target=dummy_workload)
    workload_process.start()
    
    timpi = []
    cpu_utilizat = []
    ram_utilizat = []
    
    fisier_log = '/app/rezultate_statistici.txt'
    with open(fisier_log, 'w') as f:
        f.write("Timp | CPU (%) | RAM (%)\n")
        f.write("-" * 30 + "\n")

    for secunda in range(15):
        timp_curent = time.strftime('%H:%M:%S')
        
        cpu_pct = psutil.cpu_percent(interval=1)
        ram_pct = psutil.virtual_memory().percent
        
        timpi.append(secunda)
        cpu_utilizat.append(cpu_pct)
        ram_utilizat.append(ram_pct)
        
        with open(fisier_log, 'a') as f:
            f.write(f"{timp_curent} | CPU: {cpu_pct}% | RAM: {ram_pct}%\n")
        
        # --- PLOTARE LIVE ÎN TERMINAL (ÎMBUNĂTĂȚITĂ) ---
        plt_term.clear_terminal() 
        plt_term.theme("pro") # Temă elegantă adaptată pentru terminal
        
        # Folosim markerul 'braille' pentru linii mai fluide și continue
        plt_term.plot(timpi, cpu_utilizat, label='CPU (%)', color='red', marker='braille')
        plt_term.plot(timpi, ram_utilizat, label='RAM (%)', color='cyan', marker='braille')
        
        plt_term.title("Monitorizare Live Resurse (Container Docker)")
        plt_term.xlabel("Timp (secunde)")
        plt_term.ylabel("Procentaj Utilizare (%)")
        plt_term.ylim(0, 100)
        plt_term.grid(True, True) # Adăugăm grilă pe ambele axe
        plt_term.show() 
        
    workload_process.terminate()
    print("\n=== Sarcina a fost oprită. Salvăm graficul final (PNG)... ===")
    
    plt.figure(figsize=(10, 5))
    plt.plot(timpi, cpu_utilizat, label='CPU Utilizat (%)', color='red', marker='o')
    plt.plot(timpi, ram_utilizat, label='RAM Utilizat (%)', color='blue', marker='s')
    plt.title('Evoluția Consumului de Resurse')
    plt.xlabel('Timp (secunde)')
    plt.ylabel('Procentaj Utilizare (%)')
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True)
    plt.savefig('/app/grafic_resurse.png')