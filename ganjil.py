def cek_batas(atas,bawah):
    if bawah < atas:
        for i in range(atas,bawah,-1):
            if i % 2 != 0:
                print(i,end=" ")
            else:
                pass
        
    elif atas< bawah:
        for i in range(atas,bawah):
            if i % 2 !=0:
                    print(i,end=" ")
   
                   
# cek_batas(atas=30, bawah=10)
# cek_batas(97,82)
cek_batas(10, 40)

Anda dapat melengkapi fungsi `printDataPertama` dengan cara berikut:

```python
def printDataPertama(stack: Stack):
    # Buat stack sementara untuk menyimpan elemen yang di-pop
    temp_stack = Stack()

    # Pop dan push elemen dari stack awal ke stack sementara sampai stack awal kosong
    while stack.getLen() > 0:
        temp_stack.push(stack.pop())

    # Pop elemen teratas dari stack sementara (paling awal masuk)
    first_element = temp_stack.pop()

    # Tampilkan elemen yang pertama kali dimasukkan ke stack
    print(first_element)

    # Pop dan push kembali elemen-elemen yang ada di stack sementara ke stack awal
    while temp_stack.getLen() > 0:
        stack.push(temp_stack.pop())

# Test Case pada program
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(1.5)
    s.push(5)
    s.push(3)

    print("Data stack")
    s.printData()
    print()
    print("Menampilkan Data stack paling bawah")
    printDataPertama(s)
    print()
    print("Pembuktian bahwa isi stack tidak berubah")
    s.printData()
```

Dengan ini, fungsi `printDataPertama` akan melakukan apa yang diminta yaitu menampilkan elemen yang paling pertama masuk ke dalam stack tanpa mengubah isi stack tersebut.