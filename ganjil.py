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