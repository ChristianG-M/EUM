#!/usr/bin/python3
import json
import re

json_data =[
	{
		"Name": "Debian",
		"Version": "9",
		"Install": "apt",
		"Owner": "SPI",
		"Kernel": "4.9"
	},
	{
		"Name": "Ubuntu",
		"Version": "17.10",
		"Install": "apt",
		"Owner": "Canonical",
		"Kernel": "4.13"
	},
	{
		"Name": "Fedora",
		"Version": "26",
		"Install": "dnf",
		"Owner": "Red Hat",
		"Kernel": "4.13"
	},
	{
		"Name": "CentOS",
		"Version": "7",
		"Install": "yum",
		"Owner": "Red Hat",
		"Kernel": "3.10"
	},
	{
		"Name": "OpenSUSE",
		"Version": "42.3",
		"Install": "zypper",
		"Owner": "Novell",
		"Kernel": "4.4"
	},
	{
		"Name": "Arch Linux",
		"Version": "Rolling Release",
		"Install": "pacman",
		"Owner": "SPI",
		"Kernel": "4.13"
	},
	{
		"Name": "Gentoo",
		"Version": "Rolling Release",
		"Install": "emerge",
		"Owner": "Gentoo Foundation",
		"Kernel": "4.12"
	}
]

with open('data.json', 'w') as conf:
	json.dump(json_data, conf, separators=(',', ':'), indent=4, sort_keys=True)


with open('data.json', 'r+') as f:
	data = json.load(f)
	for x in data:
		print("%s: %d", (x, data[x]))