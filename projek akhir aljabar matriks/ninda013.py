def tambah_matriks(A, B):
    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            hasil[i][j] = A[i][j] + B[i][j]
            
    return hasil

def kurang_matriks(A, B):
    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            hasil[i][j] = A[i][j] - B[i][j]
            
    return hasil

def kali_matriks(A, B):
    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):      
        for j in range(3):   
            for k in range(3): 
                hasil[i][j] += A[i][k] * B[k][j]
                
    return hasil