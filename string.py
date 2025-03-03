hello_template = 'Hello, nama saya %s, saya dari %s, saya berumur %i'
print(hello_template % ('budy', 'bandung', 17))

template_2 = 'hello saya {nama} saya berasal dari {address} umur saya {umur}'
print(template_2.format(nama = 'raffi', address = 'sukabumi', umur = 20))

name = 'budiman, aringning, agus, ramdan'
print(name[2:7])
print('😁'.join(name.split(',')))

sentence = 'Tim Hukum KPK meminta penundaan sidang praperadilan jilid II Sekjen PDIP Hasto Kristiyanto terkait penetapan status tersangka. Kuasa hukum Hasto berharap penundaan itu bukan akal-akalan KPK untuk menyelesaikan berkas perkara.'

split = sentence.split(' ')
spread = split[0:6]
print(' '.join(spread))

 # type: ignore

