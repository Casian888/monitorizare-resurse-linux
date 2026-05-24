import time
import multiprocessing
import psutil
import matplotlib.pyplot as plt
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

    # Plot live (nu in terminal)
    plt.ion() 
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.canvas.manager.set_window_title('Dashboard Resurse Docker') # Titlul ferestrei

    for secunda in range(16): # De la 0 la 15
        timp_curent = time.strftime('%H:%M:%S')
        
        cpu_pct = psutil.cpu_percent(interval=1)
        ram_pct = psutil.virtual_memory().percent
        
        timpi.append(secunda)
        cpu_utilizat.append(cpu_pct)
        ram_utilizat.append(ram_pct)
        
        with open(fisier_log, 'a') as f:
            f.write(f"{timp_curent} | CPU: {cpu_pct}% | RAM: {ram_pct}%\n")
        
        # live plot
        ax.clear() 
        
        #
        ax.plot(timpi, cpu_utilizat, label='CPU Utilizat (%)', color='#ff3333', marker='o', linewidth=2.5)
        ax.plot(timpi, ram_utilizat, label='RAM Utilizat (%)', color='#00bfff', marker='s', linewidth=2.5)
        
        ax.set_title('Evoluția Consumului de Resurse (Live)', fontsize=14, pad=15)
        ax.set_xlabel('Timp (secunde)', fontsize=12)
        ax.set_ylabel('Procentaj Utilizare (%)', fontsize=12)
        
        # 
        ax.set_xlim(left=0, right=15)  # timp 0-15
        ax.set_ylim(bottom=0, top=100) #
        
        ax.legend(loc='upper left')
        ax.grid(True, linestyle='--', alpha=0.6) # 
        
        plt.pause(0.1) 
        
    workload_process.terminate()
    print("\n Sarcina a fost oprită. Salvăm graficul final (PNG)...")
    
    plt.ioff() # Oprim modul interactiv
    plt.savefig('/app/grafic_resurse.png', bbox_inches='tight')
    print("[Succes] Imaginea a fost salvată!")