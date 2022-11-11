listt = [102, 6.6, '77', '564', 75, '3.92', 'E', 2.77, 7.66, 'C', '408', 605, '690', 'Z', '134', 'S', 'K', 148, '68', '654', 'U', '537', 0.64, 905, 5.75, 302, '7.57', '834', '0.64', '29', '709', '8.28', 'Y', 640, 'U', '0.92', 4.63, '259', '245', '5.1', 'Z', 'D', '5.58', 1.26, 6.95, '2.87', '9.25', 'F', 273, '852']
checked = []
total1, total2, concatstring = 0,0,''
for x in listt:
    if x not in checked:
        try:
            if x == int(str(x)) or x == str(int(x)):
                total1 += int(x)
                checked.append(x)
        except:pass
        if x not in checked:
            try:
                if x == float(str(x)) or x == str(float(x)):
                    total2 += float(x)
            except:
                concatstring += x
                
print(f"""Total value of integers: {total1}
Total value of floats: {total2}
Concatenated string : {concatstring}""")
