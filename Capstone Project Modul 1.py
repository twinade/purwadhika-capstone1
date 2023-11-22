#Capstone Project Modul 1
#Case Study --> Gudang (stok data)

daftarBarang = [
    {'Kode Barang' : '202301',
    'Nama Barang' : 'MotorAssy',
    'Tipe Barang' : 'Elektrikal',
    'Harga Barang' : 80000,
    'Stok Barang' : 100},

    {'Kode Barang' : '202302',
    'Nama Barang' : 'FrameAssy',
    'Tipe Barang' : 'BodySection',
    'Harga Barang' : 50000,
    'Stok Barang' : 25},

    {'Kode Barang' : '202303',
    'Nama Barang' : 'Louver',
    'Tipe Barang' : 'BodySection',
    'Harga Barang' : 30000,
    'Stok Barang' : 50},

    {'Kode Barang' : '202304',
    'Nama Barang' : 'Kapasitor',
    'Tipe Barang' : 'Elektrikal',
    'Harga Barang' : 20000,
    'Stok Barang' : 175},
    ]

def divider():
    print('\t-------------------------------------------------------------------------------')

#fungsi khusus showBarang
def showBarang(x):
    print('\n\t**********************Daftar Stok Barang Kipas Angin***************************')
    divider()
    print('\t| Kode Barang\t| Nama Barang\t| Tipe Barang\t| Harga Barang\t| Stok Barang |')
    divider()
    for y in range(len(x)):
            print('\t| {} \t| {}\t| {}\t| {}\t\t| {}\t|'.format(
                     x[y]["Kode Barang"],
                     x[y]["Nama Barang"],
                     x[y]["Tipe Barang"],
                     x[y]["Harga Barang"],
                     x[y]["Stok Barang"]))
    divider()

#Fungsi khusus searchBarang Read
def searchBarang(input):
    searchBarang = (list(filter(lambda data: data['Kode Barang'] == str(input), daftarBarang)))
    return searchBarang

#fungsi khusus input update Kode Barang
def inUpKodeBarang():
    while True:
        kodeBarang = input('\n\tMasukkan Kode Barang: ')
        i = kodeBarang.isnumeric()
        if i == True:
            i = kodeBarang
            return i
        else:
            print('\tINPUT TIDAK SESUAI !')

#fungsi khusus input update Nama Barang
def inUpNamaBarang(barang):
    namaBarang = input('\n\tMasukkan Nama Barang Baru: ')   
    barang[0]["Nama Barang"] = namaBarang
    
#fungsi khusus input update tipe barang
def inUpTipeBarang(barang):
    tipeBarang = input('\n\tMasukkan Tipe Barang Baru: ')   
    barang[0]["Tipe Barang"] = tipeBarang

#fungsi khusus input update harga barang
def inUpHargaBarang(barang):
    hargaBarang = input('\n\tMasukkan Harga Barang Baru: ')   
    barang[0]["Harga Barang"] = hargaBarang

#fungsi khusus input update stok barang
def inUpStokBarang(barang):
    stokBarang = input('\n\tMasukkan Stok Barang Baru: ')   
    barang[0]["Stok Barang"] = stokBarang

#Fungsi Read
def Read():
    inputRead = input(
        '''
        Menu Menampilkan Daftar Barang:
        1. Tampilkan Semua Barang
        2. Tampilkan Barang Tertentu
        3. Kembali ke Menu Utama
                           
        Masukkan angka menu yang ingin dijalankan (1-3): ''')

    if inputRead == '1' and len(daftarBarang):
        showBarang (daftarBarang)
    elif inputRead == '2' and len(daftarBarang):
        inKode = input('\n\tMasukan Kode Barang yang ingin dicari: ')
        searchBarang (inKode)
        if len(searchBarang(inKode)):
            showBarang(searchBarang(inKode))
        else:
            print('\n\t>>  BARANG YANG DICARI TIDAK ADA !\t<<')
    elif inputRead == '3':
        return Menu()
    else:
        print('\n\t#### ANGKA YANG ANDA MASUKKAN TIDAK SESUAI !####')
    Read()

#Fungsi Create
def Create():
    inputCreate = input(
        '''
        Menu Menambahkan Daftar Barang:
        1. Menambahkan Daftar Barang
        2. Kembali ke Menu Utama
                           
        Masukkan angka menu yang ingin dijalankan (1-2): ''')
    if inputCreate == '1':
        inCreKode = input('\n\tMasukkan Kode Barang Baru: ')
        if any(i.get('Kode Barang') == inCreKode for i in daftarBarang):
            print("\n\t>>>DATA SUDAH ADA !<<<")
        else:
            inNamaBarang = input('\tMasukkan Nama Barang yang ingin ditambahkan: ').capitalize()
            inTipeBarang = input('\tMasukkan Tipe Barang yang ingin ditambahkan: ').capitalize()
            inHargaBarang = input('\tMasukkan Harga Barang yang ingin ditambahkan: ')
            inStokBarang = input('\tMasukkan Stok Barang yang ingin ditambahkan: ')
            indaftarBarang = (
                {'Kode Barang' : inCreKode,
                'Nama Barang' : inNamaBarang,
                'Tipe Barang' : inTipeBarang,
                'Harga Barang' : inHargaBarang,
                'Stok Barang' : inStokBarang})
            SaveCreate = input('\n\tApakah penambahan barang akan disimpan? (Ya/Tidak): ').lower()
            if SaveCreate == 'ya':
                daftarBarang.append(indaftarBarang)
                showBarang(daftarBarang)
                print('\n\t=== DATA BERHASIL TERSIMPAN ===')
            else:
                print('\n\t!!! DATA BARANG TIDAK TERSIMPAN !!!')
    elif inputCreate == '2':
        return Menu()
    else:
        print('\n\t#### ANGKA YANG ANDA MASUKKAN TIDAK SESUAI !####')
    Create()

#Fungsi Update
def Update():
    inputUpdate = input(
        '''
        Menu Mengubah Daftar Barang:
        1. Mengubah Daftar Barang
        2. Kembali ke Menu Utama
                           
        Masukkan angka menu yang ingin dijalankan (1-2): ''')
    if inputUpdate == '1':
        showBarang(daftarBarang)
        kodeBarang = inUpKodeBarang()
        cariBarang = list(filter(lambda data: data['Kode Barang'] == kodeBarang, daftarBarang))
        if len(cariBarang):
            showBarang(cariBarang)
            while True:
                upData = input('\n\tApakah anda ingin mengubah data? (Ya/Tidak)').lower()
                if upData == 'ya':
                    
                    updateBarang = input('\n\tMasukkan kategori barang yang ingin diubah (Nama Barang/Tipe Barang/Harga Barang/Stok Barang): ').lower()
                    if updateBarang == 'nama barang':
                            inUpNamaBarang(cariBarang)
                            showBarang(cariBarang)
                            print("\n\t>>>DATA BERHASIL DIUBAH ! <<<")
                            break
                    elif updateBarang == "tipe barang":
                            inUpTipeBarang(cariBarang)
                            showBarang(cariBarang)
                            print("\t>>>DATA BERHASIL DIUBAH ! <<<")
                            break
                    elif updateBarang == "harga barang":
                            inUpHargaBarang(cariBarang)
                            showBarang(cariBarang)
                            print("\t>>>DATA BERHASIL DIUBAH ! <<<")
                            break
                    elif updateBarang == "stok barang":
                            inUpStokBarang(cariBarang)
                            showBarang(cariBarang)
                            print("\t>>>DATA BERHASIL DIUBAH ! <<<")
                            break
                    else:
                            print('\n\tKATEGORI TIDAK SESUAI !')
                            break
                    
                else:
                    print('\n\t >>>DATA TIDAK BERHASIL DIUBAH<<<')
                    break
    elif inputUpdate == '2':
        return Menu()
    else:
        print('\n\t#### ANGKA YANG ANDA MASUKKAN TIDAK SESUAI !####')
    Update()  

#Fungsi Delete
def Delete():
    inputDel = input(
        '''
        Menu Menghapus Daftar Barang:
        1. Menghapus Daftar Barang
        2. Kembali ke Menu Utama

        Masukkan angka menu yang ingin dijalankan (1-2): ''')
    if inputDel == '1':
        showBarang (daftarBarang)
        inDelKode = input('\n\tMasukkan Kode Barang yang ingin dihapus: ')
        if not any(i.get('Kode Barang') == inDelKode for i in daftarBarang):
            print("\n\t!!! DATA TIDAK TERSEDIA !!!")
        else:
            searchBarang(inDelKode)
            showBarang(searchBarang(inDelKode))
            delete = input('\n\tIngin menghapus data? (Ya/Tidak): ').lower()
            if delete == 'ya':
                for i in searchBarang(inDelKode):
                    daftarBarang.remove(i)
                    print('\n\t>>>DATA BERHASIL TERHAPUS<<<')
                    showBarang(daftarBarang)
            else:
                print('\n\t>>>DATA TIDAK BERHASIL TERHAPUS<<<')
    elif inputDel == '2':
        return Menu()
    else:
        print('\n\t#### ANGKA YANG ANDA MASUKKAN TIDAK SESUAI !####')
    Delete()

#Fungsi penerimaan barang
def stockIn():
    inputUpdate = input(
        '''
        Menu Penerimaan Barang:
        1. Penerimaan Barang
        2. Kembali ke Menu Utama
                           
        Masukkan angka menu yang ingin dijalankan (1-2): ''')
    if inputUpdate == '1':
        showBarang(daftarBarang)
        kodeBarang = inUpKodeBarang()
        cariBarang = list(filter(lambda data: data['Kode Barang'] == kodeBarang, daftarBarang))
        if len(cariBarang):
            showBarang(cariBarang)
            while True:
                upData = input('\n\tApakah anda ingin menerima barang? (Ya/Tidak)').lower()
                if upData == 'ya':
                    
                    jumlahBarang = int(input('\n\tBerapa jumlah yang ingin diterima: '))
                    cariBarang[0]["Stok Barang"] += jumlahBarang
                    showBarang(cariBarang)
                    print("\n\tBarang berhasil diterima sebanyak {} pcs!".format(jumlahBarang))
                    break

                else:
                    print('\n\t >>>DATA TIDAK BERHASIL DIUBAH<<<')
                    break
    elif inputUpdate == '2':
        return Menu()
    else:
        print('\n\t#### ANGKA YANG ANDA MASUKKAN TIDAK SESUAI !####')
    stockIn()  

#Fungsi pengeluaran barang
def stockOut():
    inputUpdate = input(
        '''
        Menu Pengambilan Barang:
        1. Pengambilan Barang
        2. Kembali ke Menu Utama
                           
        Masukkan angka menu yang ingin dijalankan (1-2): ''')
    if inputUpdate == '1':
        showBarang(daftarBarang)
        kodeBarang = inUpKodeBarang()
        cariBarang = list(filter(lambda data: data['Kode Barang'] == kodeBarang, daftarBarang))
        if len(cariBarang):
            showBarang(cariBarang)
            while True:
                upData = input('\n\tApakah anda ingin mengambil barang? (Ya/Tidak)').lower()
                if upData == 'ya':
                    
                    jumlahBarang = int(input('\n\tBerapa jumlah yang ingin diambil: '))
                    cariBarang[0]["Stok Barang"] -= jumlahBarang
                    showBarang(cariBarang)
                    print("\n\tBarang berhasil diambil sebanyak {}pcs!".format(jumlahBarang))
                    break

                else:
                    print('\n\t >>>DATA TIDAK BERHASIL DIUBAH<<<')
                    break
    elif inputUpdate == '2':
        return Menu()
    else:
        print('\n\t#### ANGKA YANG ANDA MASUKKAN TIDAK SESUAI !####')
    stockOut() 

#Menu Utama
def Menu():
    while True:
        daftarmenu = input(
    '''
    Selamat Datang di Gudang Stok Barang Kipas Angin
                     
    Daftar Menu:
    1. Menampilkan Daftar Barang
    2. Menambahkan Daftar Barang
    3. Mengubah Daftar Barang
    4. Menghapus Daftar Barang
    5. Penerimaan Barang
    6. Pengambilan Barang
    7. Exit

    Masukkan angka (1-7) menu yang ingin dijalankan: ''')
        if daftarmenu == '1':
            Read()
        elif daftarmenu == '2':
            Create()
        elif daftarmenu == '3':
            Update()
        elif daftarmenu == '4':
            Delete()
        elif daftarmenu == '5':
            stockIn()
        elif daftarmenu == '6':
            stockOut()
        elif daftarmenu == '7':
            print('\n\tTerima kasih sudah menggunakan program ini')
            break
        else:
            print('\n\t>>>ANGKA YANG ANDA MASUKKAN TIDAK SESUAI !<<<')

Menu()