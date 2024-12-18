flow = {
    "north": "🡡",
    "east": "🡢",
    "south": "🡣"
}

# flow["west"] = "🡠"
flow.update({"west": "🡠"})

print(flow)

compass = input('location ')
print(flow[compass])