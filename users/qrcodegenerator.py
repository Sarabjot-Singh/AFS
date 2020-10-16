def qrcode(username, mobile):
    import qrcode

    img = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size=2,
        border=2
    )
    data = username + mobile
    img.add_data(data=data)
    img.make()
    qr = img.make_image(fill_color='black', back_color='white')
    qr.save(f'C:\\Users\Olive\django_prject\media\qr_codes\\{data}.png')



