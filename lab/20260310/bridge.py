#!/usr/bin/env python3
"""
Esercizio Interattivo: Bridge Linux con due client
Versione Python con visualizzazione dello stato
"""

import os
import subprocess
import time
import sys

class BridgeExercise:
    def __init__(self):
        self.client1 = "client1"
        self.client2 = "client2"
        self.bridge = "br-test"
        self.ip1 = "192.168.1.10"
        self.ip2 = "192.168.1.20"
        self.netmask = "24"
        self.gateway = "192.168.1.1"
        
    def check_root(self):
        """Verifica privilegi di root"""
        if os.geteuid() != 0:
            print("❌ Questo script richiede privilegi di root!")
            print("   Esegui con: sudo python3 bridge_exercise.py")
            sys.exit(1)
    
    def run_cmd(self, cmd, description=""):
        """Esegue un comando e gestisce l'output"""
        if description:
            print(f"\n{description}")
        print(f"   $ {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0 and "already exists" not in result.stderr:
            print(f"   ⚠️  Errore: {result.stderr}")
        return result
    
    def create_bridge_topology(self):
        """Crea la topologia: bridge + 2 client"""
        print("\n" + "="*60)
        print("🏗️  CREAZIONE TOPOLOGIA DI RETE")
        print("="*60)
        
        # 1. Crea i namespace
        print("\n📦 FASE 1: Creazione namespace client")
        self.run_cmd(f"ip netns add {self.client1}", f"Creazione {self.client1}...")
        self.run_cmd(f"ip netns add {self.client2}", f"Creazione {self.client2}...")
        
        # 2. Crea il bridge
        print("\n🌉 FASE 2: Creazione bridge")
        self.run_cmd(f"ip link add name {self.bridge} type bridge", f"Creazione {self.bridge}...")
        self.run_cmd(f"ip link set {self.bridge} up", f"Attivazione {self.bridge}...")
        
        # 3. Crea le veth pair
        print("\n🔌 FASE 3: Creazione veth pair")
        self.run_cmd(f"ip link add veth1 type veth peer name veth1-br", 
                    f"Creazione coppia per client1...")
        self.run_cmd(f"ip link add veth2 type veth peer name veth2-br",
                    f"Creazione coppia per client2...")
        
        # 4. Collega le estremità
        print("\n🔗 FASE 4: Collegamento estremità")
        self.run_cmd(f"ip link set veth1 netns {self.client1}", 
                    f"Spostamento veth1 in {self.client1}...")
        self.run_cmd(f"ip link set veth2 netns {self.client2}",
                    f"Spostamento veth2 in {self.client2}...")
        self.run_cmd(f"ip link set veth1-br master {self.bridge}",
                    f"Collegamento veth1-br al bridge...")
        self.run_cmd(f"ip link set veth2-br master {self.bridge}",
                    f"Collegamento veth2-br al bridge...")
        
        # 5. Configura IP
        print("\n🌐 FASE 5: Configurazione indirizzi IP")
        self.run_cmd(f"ip netns exec {self.client1} ip addr add {self.ip1}/{self.netmask} dev veth1",
                    f"Configurazione {self.client1} ({self.ip1})...")
        self.run_cmd(f"ip netns exec {self.client1} ip link set veth1 up",
                    f"Attivazione interfaccia {self.client1}...")
        self.run_cmd(f"ip netns exec {self.client1} ip link set lo up",
                    f"Attivazione loopback {self.client1}...")
        
        self.run_cmd(f"ip netns exec {self.client2} ip addr add {self.ip2}/{self.netmask} dev veth2",
                    f"Configurazione {self.client2} ({self.ip2})...")
        self.run_cmd(f"ip netns exec {self.client2} ip link set veth2 up",
                    f"Attivazione interfaccia {self.client2}...")
        self.run_cmd(f"ip netns exec {self.client2} ip link set lo up",
                    f"Attivazione loopback {self.client2}...")
        
        # 6. Attiva le estremità del bridge
        print("\n⚡ FASE 6: Attivazione collegamenti")
        self.run_cmd(f"ip link set veth1-br up", f"Attivazione veth1-br...")
        self.run_cmd(f"ip link set veth2-br up", f"Attivazione veth2-br...")
        
        print("\n✅ TOPOLOGIA CREATA CON SUCCESSO!")
    
    def show_status(self):
        """Mostra lo stato della topologia"""
        print("\n" + "="*60)
        print("📊 STATO DELLA TOPOLOGIA")
        print("="*60)
        
        # Mostra namespace
        print("\n📦 Namespace attivi:")
        result = self.run_cmd("ip netns list")
        if result.stdout:
            for line in result.stdout.split('\n'):
                if line:
                    print(f"   • {line}")
        
        # Mostra bridge
        print("\n🌉 Bridge e interfacce:")
        result = self.run_cmd(f"ip link show {self.bridge}")
        if result.stdout:
            print(result.stdout)
        
        # Mostra tabella MAC
        print("\n📇 Tabella MAC del bridge:")
        result = self.run_cmd(f"bridge fdb show {self.bridge}")
        if result.stdout:
            for line in result.stdout.split('\n'):
                if line:
                    print(f"   {line}")
        
        # Mostra IP client
        print("\n🌐 Configurazione client:")
        result = self.run_cmd(f"ip netns exec {self.client1} ip addr show veth1")
        if result.stdout:
            print(f"   {self.client1}:")
            for line in result.stdout.split('\n'):
                if 'inet ' in line:
                    print(f"      {line.strip()}")
        
        result = self.run_cmd(f"ip netns exec {self.client2} ip addr show veth2")
        if result.stdout:
            print(f"   {self.client2}:")
            for line in result.stdout.split('\n'):
                if 'inet ' in line:
                    print(f"      {line.strip()}")
    
    def test_connectivity(self):
        """Test di connettività tra i client"""
        print("\n" + "="*60)
        print("🔄 TEST DI CONNETTIVITÀ")
        print("="*60)
        
        # Test ping client1 → client2
        print(f"\n📤 Test ping da {self.client1} ({self.ip1}) a {self.client2} ({self.ip2}):")
        result = self.run_cmd(f"ip netns exec {self.client1} ping -c 4 -W 1 {self.ip2}")
        if "1 received" in result.stdout or "4 received" in result.stdout:
            print("   ✅ CONNESSIONE RIUSCITA")
        else:
            print("   ❌ CONNESSIONE FALLITA")
        
        # Test ping client2 → client1
        print(f"\n📤 Test ping da {self.client2} ({self.ip2}) a {self.client1} ({self.ip1}):")
        result = self.run_cmd(f"ip netns exec {self.client2} ping -c 4 -W 1 {self.ip1}")
        if "1 received" in result.stdout or "4 received" in result.stdout:
            print("   ✅ CONNESSIONE RIUSCITA")
        else:
            print("   ❌ CONNESSIONE FALLITA")
    
    def interactive_shell(self, client):
        """Apre una shell interattiva in un client"""
        print(f"\n🚀 Apertura shell in {client}...")
        print("   (digita 'exit' per tornare al menu principale)")
        os.system(f"sudo ip netns exec {client} bash")
    
    def cleanup(self):
        """Pulisce tutte le risorse create"""
        print("\n" + "="*60)
        print("🧹 PULIZIA RISORSE")
        print("="*60)
        
        self.run_cmd(f"ip netns del {self.client1} 2>/dev/null", f"Rimozione {self.client1}...")
        self.run_cmd(f"ip netns del {self.client2} 2>/dev/null", f"Rimozione {self.client2}...")
        self.run_cmd(f"ip link del {self.bridge} 2>/dev/null", f"Rimozione bridge...")
        self.run_cmd(f"ip link del veth1 2>/dev/null", f"Rimozione veth1...")
        self.run_cmd(f"ip link del veth2 2>/dev/null", f"Rimozione veth2...")
        
        print("\n✅ PULIZIA COMPLETATA")
    
    def menu(self):
        """Menu interattivo"""
        while True:
            print("\n" + "="*60)
            print("🏠 MENU PRINCIPALE - BRIDGE EXERCISE")
            print("="*60)
            print("1. Crea topologia (bridge + 2 client)")
            print("2. Mostra stato")
            print("3. Test connettività (ping)")
            print("4. Entra in client1 (shell)")
            print("5. Entra in client2 (shell)")
            print("6. Pulisci risorse")
            print("7. Esci")
            print("-"*60)
            
            choice = input("Scegli un'opzione (1-7): ").strip()
            
            if choice == "1":
                self.create_bridge_topology()
            elif choice == "2":
                self.show_status()
            elif choice == "3":
                self.test_connectivity()
            elif choice == "4":
                self.interactive_shell(self.client1)
            elif choice == "5":
                self.interactive_shell(self.client2)
            elif choice == "6":
                self.cleanup()
            elif choice == "7":
                print("\nArrivederci!")
                break
            else:
                print("❌ Opzione non valida")
    
    def run(self):
        """Esegue l'esercizio"""
        self.check_root()
        print("\n" + "="*60)
        print("🎓 ESERCIZIO: BRIDGE LINUX CON DUE CLIENT")
        print("="*60)
        print("\nObiettivo: Creare un bridge virtuale e collegare")
        print("due client in namespace separati.")
        print("\nConcetti chiave:")
        print("  • Network namespace")
        print("  • Bridge Linux (switch virtuale)")
        print("  • veth pair (cavo virtuale)")
        print("  • Routing e connettività")
        
        self.menu()


if __name__ == "__main__":
    exercise = BridgeExercise()
    exercise.run()