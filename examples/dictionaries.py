#dictornaries are created with curly bracets, like a object in JS
# keys must be unique,can be numbers
monthConversions = {
    "Jan":"January",
    "Feb": "Feburary",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}
# refer to the key and it return the value of it
print(monthConversions["Nov"])
# also use to get they value of a key, get allows you to set a default value
# if a key is not a mappable value
print(monthConversions.get("Luv","Not a valid key"))