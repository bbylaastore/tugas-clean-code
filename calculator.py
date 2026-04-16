BONUS_TAMBAHAN = 10000
MAKSIMAL_HARGA = 100000

def hitung_diskon(harga, persen_diskon, pakai_bonus):
    """
    Menghitung harga setelah diskon dengan opsi bonus tambahan.
    """

    if harga < 0:
        raise ValueError("Harga tidak boleh negatif.")

    if persen_diskon < 0 or persen_diskon > 100:
        raise ValueError("Diskon harus antara 0-100.")

    hasil = harga - (harga * persen_diskon / 100)

    if pakai_bonus:
        hasil += BONUS_TAMBAHAN

    if hasil > MAKSIMAL_HARGA:
        hasil = MAKSIMAL_HARGA

    return hasil