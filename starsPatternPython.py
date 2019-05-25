def xprint(size):
    i,j = 0, size - 1

    while j>= 0 and i<size:
        inisial_spasi = ' '*min(i,j)
        tengah_spasi = ' '*(abs(i-j)-1)
        final_spasi = ' '*(size-1-max(i,j))

        if j==i:
            print inisial_spasi + '*' + final_spasi
        else:
            print inisial_spasi + '*' + tengah_spasi + '*' + final_spasi    
        i += 1
        j -= 1
xprint(5)
