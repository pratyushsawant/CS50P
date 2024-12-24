n=input("File Name: ").strip().lower()
if n.endswith(".gif"):
    print("image/gif")
elif n.endswith(".jpeg") or n.endswith(".jpg"):
    print("image/jpeg")
elif n.endswith(".png"):
    print("image/png")
elif n.endswith(".pdf") or n.endswith(".txt.pdf") or n.endswith(".PDF") :
    print("application/pdf")
elif n.endswith(".txt"):
    print("text/plain")
elif n.endswith(".zip"):
    print("application/zip")
elif n.endswith(".bin"):
    print("application/octet-stream")
else:
    print("application/octet-stream")



