def changeface(Text):
    Text= Text.replace(":)","🙂")
    Text=Text.replace(":(","🙁")
    return Text
Text=input("Text: ")
print(changeface(Text))

