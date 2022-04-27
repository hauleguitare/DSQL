while True:

    print("""
    XIN CHÀO, ĐÂY LÀ ỨNG DỤNG QUẢN LÝ HỌC SINH:
        VUI LÒNG CHỌN CÁC CHỨC NĂNG SAU:
        0.  THOÁT CHƯƠNG TRÌNH
        1.  THÊM HỌC SINH
        2.  TÌM HỌC SINH
        3.  TRA CỨU HỌC SINH
        4.  TRA CỨU HỌC SINH THEO KHỐI
        5.  TỔNG SỐ HỌC SINH ĐANG HỌC
        6.  XÓA HỌC SINH
    """)
    choose = int(input("VUI LÒNG NHẬP CHỨC NĂNG SAU: "))

    # EXIT PROGRAM
    if choose == 0:
        break
    
    # THÊM HỌC SINH:
    elif choose == 1:
        pass

    # TÌM HỌC SINH:
    elif choose == 2:
        while True:
            print("""
            VUI LÒNG CHỌN CÁC CHỨC NĂNG SAU:
                0.  THOÁT RA
                1.  TÌM HỌC SINH THEO MÃ SỐ
                2.  TÌM HỌC SINH THEO TÊN
            """)
            choose_find = int(input("VUI LÒNG CHỌN CHỨC NĂNG: "))
            # THOÁT RA
            if choose_find == 0:
                break
            # TÌM HỌC SINH THEO MÃ SỐ
            elif choose_find == 1:
                pass
            # TÌM HỌC SINH THEO TÊN
            elif choose_find == 2:
                pass
    
    # TRA CỨU HỌC SINH:
    elif choose == 3:
        pass

    # TÌM TẤT CẢ HỌC SINH THEO KHỐI:
    elif choose == 4:
        pass

    # TỔNG SỐ HỌC SINH ĐANG HỌC:
    elif choose == 5:
        pass

    # XÓA HỌC SINH:
    elif choose == 6:
        pass
        
    


