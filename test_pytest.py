import pytest
from prog_hitung_luas import Luas

class TestLuas():
    @pytest.mark.parametrize("a,b,c",[(2,3,6),(4,5,20)])
    def test_Persegipanjang(self,a,b,c):
        result_Persegipanjang = Luas.luasPersegiPanjang(a,b)
        assert result_Persegipanjang == c
    @pytest.mark.parametrize("a,b",[(2,4),(6,36)])
    def test_Persegi(self,a,b):
        result_Persegi = Luas.luasPersegi(a)
        assert result_Persegi == b
    @pytest.mark.parametrize("a,b,c",[(4,8,16),(7,5,17.5)])
    def test_Segitiga(self,a,b,c):
        result_Segitiga = Luas.luasSegitiga(a,b)
        assert result_Segitiga == c
    @pytest.mark.parametrize("a,b",[(7,154),(14,616)])
    def test_Lingkaran(self,a,b):
        result_Lingkaran = Luas.luasLingkaran(a)
        assert result_Lingkaran == b
    @pytest.mark.parametrize("a,b,c,d",[(8,12,5,50),(5,6,5,27.5)])
    def test_Trapesium(self,a,b,c,d):
        result_Trapesium = Luas.luasTrapesium(a,b,c)
        assert result_Trapesium == d
    @pytest.mark.parametrize("a,b,c,",[(4,8,32),(7,5,35)])
    def test_JajarG(self,a,b,c):
        result_JajarG = Luas.luasJajarG(a,b)
        assert result_JajarG == c
