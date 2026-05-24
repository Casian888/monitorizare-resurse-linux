import time
import multiprocessing
import psutil
import matplotlib.pyplot as plt
import os

def dummy_workload():
    """Aplicatie dummy care ruleaza in fundal și consuma CPU si RAM."""
    print("[Dummy App] A pornit sarcina care consuma resurse (Background)...")
    lista_memorie = []
    while True:
        # Stres CPU
        _ = [x**2 for x in range(10000)]
        # umplere RAM cu elem. din lista
        lista_memorie.append("A" * 100000)
        time.sleep(0.1)

if __name__ == "__main__":
    print("Start Monitorizare")
    
    #Pornim dummy in proces separat
    workload_process = multiprocessing.Process(target=dummy_workload)
    workload_process.start()
    
    # Liste pentru a stoca date pentru grafice
    timpi = []
    cpu_utilizat = []
    ram_utilizat = []
    
    print("\n[Monitorizare in Timp Real]")
    print(f"{'Timp':<10} | {'CPU (%)':<10} | {'RAM (%)':<10}")
    print("-" * 35)
    
    # monitorizare sistem timp de 15 secunde
    for secunda in range(15):
        timp_curent = time.strftime('%H:%M:%S')
        
        # citim procentele (psutil)(timp real)
        cpu_pct = psutil.cpu_percent(interval=1)
        ram_pct = psutil.virtual_memory().percent
        
        # afisare in terminal (timp real)
        print(f"{timp_curent:<10} | {cpu_pct:<10} | {ram_pct:<10}")
        
        # salvare date pentru grafic
        timpi.append(secunda)
        cpu_utilizat.append(cpu_pct)
        ram_utilizat.append(ram_pct)
        
    # oprim fortat aplicatia dummy cand am terminat masuratorile
    workload_process.terminate()
    print("\n Sarcina Dummy a fost oprita.")
    
    #  generam graficul cu Matplotlib
    print("[Grafic] Generam imaginea grafic_resurse.png...")
    plt.figure(figsize=(10, 5))
    plt.plot(timpi, cpu_utilizat, label='CPU Utilizat (%)', color='red', marker='o')
    plt.plot(timpi, ram_utilizat, label='RAM Utilizat (%)', color='blue', marker='s')
    
    plt.title('Evolutia Consumului de Resurse (Container Docker)')
    plt.xlabel('Timp (secunde)')
    plt.ylabel('Procentaj Utilizare (%)')
    plt.ylim(0, 100) # setam axa Y sa fie procent (0-100)
    plt.legend()
    plt.grid(True)
    
    # save la grafic preluare de volumul Docker pe masina Linux
    plt.savefig('/app/grafic_resurse.png')
    print("[Grafic] Imaginea a fost salvata cu succes!")