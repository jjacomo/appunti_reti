#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# btw ti serve la libreria dnspython

import tkinter as tk
from tkinter import ttk
import dns.resolver
from dns import reversename


# ==========================
# FORWARD DNS QUERY
# ==========================

def forward_query():

    domain = domain_entry.get()
    record = record_var.get()

    output_forward.delete(1.0, tk.END)

    resolver = dns.resolver.get_default_resolver()
    nameserver = resolver.nameservers[0]

    output_forward.insert(tk.END, "=== FORWARD DNS QUERY ===\n\n")
    output_forward.insert(tk.END, f"Domain: {domain}\n")
    output_forward.insert(tk.END, f"Record type: {record}\n")
    output_forward.insert(tk.END, f"Resolver used: {nameserver}\n\n")

    try:

        answers = dns.resolver.resolve(domain, record)

        for rdata in answers:

            if record == "A":
                output_forward.insert(tk.END, f"IPv4 address: {rdata.address}\n")

            elif record == "AAAA":
                output_forward.insert(tk.END, f"IPv6 address: {rdata.address}\n")

            elif record == "MX":
                output_forward.insert(tk.END,
                    f"Mail server: {rdata.exchange} (priority {rdata.preference})\n")

            elif record == "NS":
                output_forward.insert(tk.END,
                    f"Name server: {rdata.target}\n")

            elif record == "TXT":
                output_forward.insert(tk.END,
                    f"TXT record: {rdata}\n")

            else:
                output_forward.insert(tk.END, f"{rdata}\n")

        ttl = answers.rrset.ttl
        output_forward.insert(tk.END, f"\nTTL: {ttl} seconds\n")

    except dns.resolver.NXDOMAIN:
        output_forward.insert(tk.END, "Error: domain does not exist\n")

    except dns.resolver.NoAnswer:
        output_forward.insert(tk.END, "No record found\n")

    except dns.resolver.Timeout:
        output_forward.insert(tk.END, "DNS query timeout\n")

    except Exception as e:
        output_forward.insert(tk.END, f"Error: {e}\n")


# ==========================
# REVERSE DNS
# ==========================

def reverse_query():

    ip = ip_entry.get()

    output_reverse.delete(1.0, tk.END)

    try:

        reverse_domain = reversename.from_address(ip)

        output_reverse.insert(tk.END, "=== REVERSE DNS QUERY ===\n\n")
        output_reverse.insert(tk.END, f"IP address: {ip}\n")
        output_reverse.insert(tk.END, f"Reverse domain: {reverse_domain}\n\n")

        answers = dns.resolver.resolve(reverse_domain, "PTR")

        for rdata in answers:
            output_reverse.insert(tk.END, f"Hostname: {rdata}\n")

    except Exception as e:
        output_reverse.insert(tk.END, f"Error: {e}\n")


# ==========================
# CLEAR OUTPUT
# ==========================

def clear_forward():
    output_forward.delete(1.0, tk.END)

def clear_reverse():
    output_reverse.delete(1.0, tk.END)


# ==========================
# GUI
# ==========================

root = tk.Tk()
root.title("DNS Teaching Tool")
root.geometry("750x500")

title = tk.Label(root, text="DNS Explorer for Networking Labs",
                 font=("Arial",16))
title.pack(pady=10)


# ==========================
# TABS
# ==========================

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

tab_forward = tk.Frame(notebook)
tab_reverse = tk.Frame(notebook)

notebook.add(tab_forward, text="Forward DNS")
notebook.add(tab_reverse, text="Reverse DNS")


# ==========================
# FORWARD TAB
# ==========================

frame1 = tk.Frame(tab_forward)
frame1.pack(pady=10)

tk.Label(frame1, text="Domain").grid(row=0,column=0,padx=5)

domain_entry = tk.Entry(frame1,width=30)
domain_entry.grid(row=0,column=1)
domain_entry.insert(0,"google.com")

tk.Label(frame1, text="Record Type").grid(row=1,column=0,padx=5)

record_var = tk.StringVar()

record_menu = ttk.Combobox(
    frame1,
    textvariable=record_var,
    values=["A","AAAA","MX","NS","TXT"],
    state="readonly"
)

record_menu.grid(row=1,column=1)
record_menu.current(0)

button_frame1 = tk.Frame(tab_forward)
button_frame1.pack()

tk.Button(button_frame1,text="Query DNS",
          command=forward_query).grid(row=0,column=0,padx=5)

tk.Button(button_frame1,text="Clear",
          command=clear_forward).grid(row=0,column=1,padx=5)

output_forward = tk.Text(tab_forward,height=18,width=90)
output_forward.pack(pady=10)


# ==========================
# REVERSE TAB
# ==========================

frame2 = tk.Frame(tab_reverse)
frame2.pack(pady=10)

tk.Label(frame2,text="IP address").grid(row=0,column=0,padx=5)

ip_entry = tk.Entry(frame2,width=30)
ip_entry.grid(row=0,column=1)
ip_entry.insert(0,"8.8.8.8")

button_frame2 = tk.Frame(tab_reverse)
button_frame2.pack()

tk.Button(button_frame2,text="Reverse Lookup",
          command=reverse_query).grid(row=0,column=0,padx=5)

tk.Button(button_frame2,text="Clear",
          command=clear_reverse).grid(row=0,column=1,padx=5)

output_reverse = tk.Text(tab_reverse,height=18,width=90)
output_reverse.pack(pady=10)


root.mainloop()
