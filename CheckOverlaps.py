# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:32:20 2024

@author: micho
"""

import ipaddress

def check_ip_overlap(ip_networks):
    """
    Vérifie s'il y a un chevauchement d'adresses IP.
    :param ip_networks: Liste des adresses IP et masques de sous-réseau (en format string).
    :return: True si les adresses IP se chevauchent, False sinon.
    """
    networks = []
    for ip_net in ip_networks:
        try:
            network = ipaddress.IPv4Network(ip_net)
            for existing_network in networks:
                if network.overlaps(existing_network):
                    return True
            networks.append(network)
        except ValueError:
            # En cas d'adresse IP ou de masque de sous-réseau invalide
            return False
    return False
ip_networks = [
    "172.16.105.96/29",
    "172.16.105.0/26",
    "172.16.104.0/25",
    "172.16.104.128/25",
    "172.16.105.64/27",
    "172.16.68.96/28",
    "172.16.68.64/27",
    "172.16.64.0/23",
    "172.16.66.0/23",
    "172.16.68.0/26",
    "172.16.9.128/28",
    "172.16.9.0/25",
    "172.16.4.0/22",
    "172.16.0.0/22",
    "172.16.8.0/24",
    "172.16.102.128/27",
    "172.16.102.64/26",
    "172.16.100.0/23",
    "172.16.96.0/22",
    "172.16.102.0/26"
]

if check_ip_overlap(ip_networks):
    print("Il y a un chevauchement d'adresses IP.")
else:
    print("Il n'y a pas de chevauchement d'adresses IP.")
