# \'        singl quote
# \\        Backslash
# \n        newline 
# \r        carring return
# \t        Tab
# \b        backspace 
# \f        form Value
# \000      octal Value
# \xhh      Hex value


print ("\'deep\'")
print ("\\deep padwale\\")
print ("deep \npadwale")
print ("deep\rpadwale")
print("deep\tpadwale")
print("deep padwale is\b")

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 


#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
