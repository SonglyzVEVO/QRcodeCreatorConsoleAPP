
import qrcode


def qrcode_create(link, file_name):
    qr = qrcode.QRCode(version=1,
                       box_size=10,
                       border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black',
                        back_color='white')
    file_save_name = f"{file_name}.png"
    img.save(file_save_name)


def main():
    link = input("Enter Your link Here:")
    file_name = input("Enter Your File Name Here:")
    confirm = input("Confirm if You want to Create QRcode from previous input link (Y/N)")

    if confirm == "Y" or confirm == "y":
        qrcode_create(link=link, file_name=file_name)
    elif confirm == "N" or confirm == "n":
        print("-----------------------------------")
    else:
        Exception("Error something")


if __name__ == "__main__":
    print("This is QrcodeCreateApplication No Expire Date")
    print("Create By Naraebase Mutthakarn contact me : +66933232808")
    while True:
        main()
        close = input("Close?(Y/N)")
        if close == "Y" or close == "y":
            break
        elif close == "N" or close == "n":
            print("---------------------------")
        else:
            Exception("Error something")
