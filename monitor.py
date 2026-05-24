import time

def get_memory_stats():
    """Citeste si extrage statisticile de memorie din /proc/meminfo."""
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
            # Extragem MemTotal si MemFree (primele doua linii)
            mem_total = lines[0].strip()
            mem_free = lines[1].strip()
            return f"{mem_total} | {mem_free}"
    except FileNotFoundError:
        return "Eroare: Fisierul /proc/meminfo nu a fost gasit."

def get_cpu_stats():
    """Citeste si extrage modelul procesorului si numarul de core-uri din /proc/cpuinfo."""
    try:
        with open('/proc/cpuinfo', 'r') as f:
            lines = f.readlines()
            
            model_name = "Necunoscut"
            core_count = 0
            
            # Parcurgem liniile fisierului pentru a gasi detaliile dorite
            for line in lines:
                if line.startswith("model name"):
                    # Salvam modelul doar la prima potrivire
                    if model_name == "Necunoscut":
                        # Separam stringul si eliminam spatiile goale
                        model_name = line.split(':')[1].strip()
                elif line.startswith("processor"):
                    # Fiecare intrare 'processor' reprezinta un core / thread logic
                    core_count += 1
                    
            return f"Model CPU: {model_name} | Numar Core-uri: {core_count}"
    except FileNotFoundError:
        return "Eroare: Fisierul /proc/cpuinfo nu a fost gasit."

if __name__ == "__main__":
    print("=== Start Monitorizare Container ===")
    
    # 1. Extragem si afisam informatiile despre CPU (statice)
    cpu_info = get_cpu_stats()
    print("\n[Info Hardware]")
    print(cpu_info)
    print("-" * 50)
    
    # 2. Incepem monitorizarea in timp real pentru memorie
    print("[Monitorizare Memorie]")
    count = 0
    while count < 5:
        mem_stats = get_memory_stats()
        print(f"[{time.strftime('%H:%M:%S')}] {mem_stats}")
        
        time.sleep(2) # Pauza de 2 secunde intre citiri
        count += 1
        
    print("\n=== Monitorizare Finalizata ===")