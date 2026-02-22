import json

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("="*80)
print("{:<50} {:<20} {:<6} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-"*50, "-"*20, "-"*6, "-"*6)

for item in data.get("imdata", []):
    intf = item.get("l1PhysIf", {}).get("attributes", {})
    dn = intf.get("dn", "")
    descr = intf.get("descr", "") or "" 
    speed = intf.get("speed", "")
    mtu = intf.get("mtu", "")
    
    print("{:<50} {:<20} {:<6} {:<6}".format(dn, descr, speed, mtu))
