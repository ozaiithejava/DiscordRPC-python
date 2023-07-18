from pypresence import Presence

client_id = 'BURAYA_APP_ID_GIR'  # Discord Developer Portal'dan aldığınız uygulama kimliği

RPC = Presence(client_id)
RPC.connect()

RPC.update(
    details='Detaylar',
    state='Durum',
    large_image='logo_white',  # Discord Developer Portal'da yüklediğiniz büyük resim anahtarı
    large_text='Büyük Resim Açıklama',
    small_image='logo_2',  # Discord Developer Portal'da yüklediğiniz küçük resim anahtarı
    small_text='Küçük Resim Açıklama'
)

while True:
    pass
